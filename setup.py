import pathlib
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="CriadorDeCortes",
    version="0.0.6",
    author="Leonardo Zamboni",
    author_email="leonardonunes169@gmail.com",
    description="Para você que deseja farmar dinheiro com conteúdo de terceiros sem precisar ter esforço algum",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leozamboni/GeradorDeCortes",
    project_urls={
        "Bug Tracker": "https://github.com/leozamboni/GeradorDeCortes/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["CriadorDeCortes"],
    install_requires=["pytube3", "SpeechRecognition", "moviepy"],
    python_requires=">=3.6",
)