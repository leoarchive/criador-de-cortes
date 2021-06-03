from CutsGeneration import podcast
import json


with open('config.json') as f:
    config = json.load(f)

cut = podcast.Cut
time = config["cut-time"] / 2
c = cut

i = config["init-cuts"]
cut.set(c)
d = cut.duration(c)
while i <= d:
    c.init = i
    c.end = i + 40
    cut.generation(c)
    cut.recognized(c)
    if cut.contain(c):
        c.init -= time
        c.end += time
        if c.end > d:
            c.end = d
        elif c.init < 0: 
            c.init = 0 
        cut.thumb(c)    
        cut.save(c)
    i += 40
    if i + 40 > d:
        cut.close(c)
        break 