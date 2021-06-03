# Gerador de cortes

Se você deseja ganhar muito dinheiro com o conteúdo de terceiros e ao mesmo tempo compactuar com a disseminação de informações falsas e opiniões duvidosas e com a decadência da qualidade do conteúdo existente na internet, eu ajudo você!

Com o gerador de cortes você pode criar cortes e thumbnails automaticamente a partir de algumas keywords 

Basta baixar o video, colocar o link do diretório dentro do arquivo json:

```
"video-directory": "directory/video.mp4",
```
keywords:
``` 
"keywords":
    [
        "palavras", "polêmicas"
    ],
```

e executar. 

```
python cuts.py
```

Você também precisa: 
```
pip install SpeechRecognition 
pip install moviepy
```

v0.1 -- initial release 