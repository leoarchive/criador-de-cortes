from CutsGeneration.podcast import Video
import json


with open('config.json') as f:
    config = json.load(f)

durationCutTime = config["cut-time"] / 2
time = config["init-cuts"]
v = Video()
v.set(input("Video link: "))
videoDuration = v.duration


while time <= videoDuration:
    v.cutInitTime = time
    v.cutEndTime = time + 40
    v.generationCut()
    v.recognizedVoiceCut()
    if v.isContain():
        v.cutInitTime -= durationCutTime
        v.cutEndTime += durationCutTime
        if v.cutEndTime > videoDuration:
            v.cutEndTime = videoDuration
        if v.cutInitTime < 0:
            v.cutInitTime = 0
        v.setThumb()
        v.save()
    time += 40
    if time + 40 > videoDuration:
        v.close()
        break
