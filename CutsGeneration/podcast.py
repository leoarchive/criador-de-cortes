from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw
from moviepy.tools import verbose_print
from pytube import YouTube
import speech_recognition as sr
import json


with open('config.json') as f:
    config = json.load(f)


class Video:
    item = config["init-items"]
    fps = config["fps"]
    list = config["keywords"]
    duration = 0
    cutInitTime = 0
    cutEndTime = 0

    def set(self, link):
        youtube = YouTube(link)
        self.dir = youtube.title + config["extension"]
        youtube.streams.first().download()
        print("⏳ Video está sendo carregado, isso pode demorar um pouco...")
        self.cut = VideoFileClip(self.dir)
        self.duration = int(self.cut.duration)
        print("🎥 Video carregado")

    def generationCut(self):
        print("🔍 Analisando {0:.1f} até {1:.1f}...".format(
            self.cutInitTime/60, self.cutEndTime/60))
        self.cut = VideoFileClip(self.dir).subclip(self.cutInitTime, self.cutEndTime)
        self.cut.write_videofile("Temp/cut.mp4", self.fps, logger=None)

    def save(self):
        self.cut = VideoFileClip(self.dir).subclip(self.cutInitTime, self.cutEndTime)
        self.cut.write_videofile(
            f"Cuts/cut{self.item}.mp4", self.fps, logger=None)
        self.item += 1
        print("💾 Corte salvo")

    def close(self):
        self.cut.reader.close()
        self.cut.audio.reader.close_proc()

    def setThumb(self):
        frame = (self.cutEndTime - self.cutInitTime) / 2
        self.cut.save_frame("Thumbs/thumb.png", frame)
        image = Image.open("Thumbs/thumb.png")
        font = ImageFont.truetype("arial.ttf", 70)
        draw = ImageDraw.Draw(image)
        draw.text(
            (0, 0), f"{self.frame[0]} {self.frame[1]} {self.frame[2]} {self.frame[3]}...", (255, 255, 255), font=font)
        image.save(f'Thumbs/thumb{self.item}.png')
        image.close()
        print("🖼️ Thumbnail salva")

    def isContain(self):
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

    def recognizedVoiceCut(self):
        self.cut.audio.write_audiofile(r"Temp/audio.wav", logger=None)
        r = sr.Recognizer()
        audio = sr.AudioFile("Temp/audio.wav")
        with audio as source:
            audio_file = r.record(source)
        result = r.recognize_google(audio_file, language="pt-BR")
        file = open('Temp/text.txt', mode='w')
        with file as f:
            f.write(result)
        file.close()
        self.text = 'Temp/text.txt'
        try:
            print("🔊 "+result)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
