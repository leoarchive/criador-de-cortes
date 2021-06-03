from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw
from moviepy.tools import verbose_print
import speech_recognition as sr
import json


with open('config.json') as f:
    config = json.load(f)

class Cut:
    item = config["init-items"]
    fps = config["fps"]
    list = config["keywords"]
    dir = config["video-directory"]
    text = ""
    frame = ""
    init = 0
    end = 0    

    def duration(self):
        return int(self.cut.duration)

    def set(self):
        print("⏳ Video está sendo carregado, isso pode demorar um pouco...")
        self.cut = VideoFileClip(self.dir)
        print("🎥 Video carregado")

    def generation(self):
        print("🔍 Analisando {0:.1f} até {1:.1f}...".format(self.init/60, self.end/60))
        self.cut = VideoFileClip(self.dir).subclip(self.init, self.end)
        self.cut.write_videofile("Temp/cut.mp4", self.fps, logger=None)

    def save(self):
        self.cut = VideoFileClip(self.dir).subclip(self.init, self.end)
        self.cut.write_videofile(f"Cuts/cut{self.item}.mp4", self.fps, logger=None)
        self.item += 1
        print("💾 Corte salvo")

    def close(self):
        self.cut.reader.close()
        self.cut.audio.reader.close_proc()

    def thumb(self):    
        frame = (self.end - self.init) / 2 
        self.cut.save_frame("Thumbs/thumb.png", frame)
        image = Image.open("Thumbs/thumb.png")
        font = ImageFont.truetype("arial.ttf", 70)
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), f"{self.frame[0]} {self.frame[1]} {self.frame[2]} {self.frame[3]}...",(255,255,255),font=font)
        image.save(f'Thumbs/thumb{self.item}.png')
        image.close()
        print("🖼️ Thumbnail salva")

    def contain(self):
        for word in self.list:
            with open(self.text, 'r') as a:
                for line in a:
                    line = line.strip('\n')
                    if word in line.split():
                        self.frame = line.split()
                        print("✔️ Keyword encontrada")
                        return True
        print("❌ Keyword não encontrada")                    
        return False                    
                                    
    def recognized(self):
        self.cut.audio.write_audiofile(r"Temp/audio.wav", logger=None)
        r = sr.Recognizer()
        audio = sr.AudioFile("Temp/audio.wav")
        with audio as source:
            audio_file = r.record(source)
        result = r.recognize_google(audio_file, language="pt-BR")
        file = open('Temp/text.txt', mode ='w')
        with file as f: 
            f.write(result) 
        file.close()
        self.text = 'Temp/text.txt'
        try:
            print("🔊 "+result)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
