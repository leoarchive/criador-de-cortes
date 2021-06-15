from CriadorDeCortes.podcast import Archive
import json


with open('config.json') as f:
    config = json.load(f)

durationCutTime = config["cut-time"] / 2
time = config["init-cuts"]
arch = Archive()
arch.set(input("Video link: "))
videoDuration = arch.duration


while time <= videoDuration:
    arch.cutInitTime = time
    arch.cutEndTime = time + 40
    arch.generationCut()
    arch.recognizedVoiceCut()
    if arch.isContain():
        arch.cutInitTime -= durationCutTime
        arch.cutEndTime += durationCutTime
        if arch.cutEndTime > videoDuration:
            arch.cutEndTime = videoDuration
        if arch.cutInitTime < 0:
            arch.cutInitTime = 0
        arch.setThumb()
        arch.save()
    time += 40
    if time + 40 > videoDuration:
        arch.close()
        break
