[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/AlphaPrime7/faced)
[![Demandez moi n’importe quoi
!](https://img.shields.io/badge/Demandez%20moi-n'%20importe%20quoi-1abc9c.svg)](mailto:awesome.tingwei@outlook.com)

# FaceD

- A program for basic frontal face detection using Pillow and OpenCV.

## ✍️ Introduction

- A package inspired by UMich Coursera's Python Specialization.
- [`{FaceD}`](https://github.com/AlphaPrime7/faced) is simply a package that will take in a zip file of images in any format (.JPG or .PNG) and attempt to detect faces. This will crop the faces and return them to a canvas. Try out the package using the data sample zip files provided with the package.
- This package is highly experimental and might be totally useless for some people.
- Hope this helps someone as much as it helped me in mastering python.


## ⏬ Installation

- See below for installation details.

### Development version

``` 
pip install -i https://test.pypi.org/simple/ faced==0.0.4
```

### PyPi Version

``` 
pip install faced
import faced
```

## 🛂 Quality Control (QC)

- Utilized inbuilt unit testing to test results vs expectations and everything seems to work just fine.

## Warning

- Running this package means you will need your own tesseract engine for text identification. Install it and point your system to the executable.

- The program also requires an in built classifier and this might or might not work for OS other than windows. I will check on that later but that is all for now.

## 🎇 Epilogue

- Working on CamFaceD which is a dynamic faced platform. CamFaceD can be used to train face detection although on a limited capacity. More to learn on this but steadily making progress and grateful for what I have learned so far.
