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

## Install dependencies

### Ubuntu

```{bash}
sudo apt install tesseract-ocr
pip install opencv-python-headless #we put work into defining dependencies but for this to work it is mandatory to install the headless version
```

### Windows

```{bash}
winget install --id=UB-Mannheim.TesseractOCR -e
```

There are a few links to check for tesseract-ocr:

[windows_tesseract_ocr](https://github.com/Nayan-Gajjar/wondows_tesseract_ocr)

[Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)

[windows_tesseract_ocr Exes](https://digi.bib.uni-mannheim.de/tesseract/)

[windows_tesseract_ocr Downloads](https://tesseract-ocr.github.io/tessdoc/Downloads.html)

[How install Tesseract — ORC and Pytesseract on Windows](https://medium.com/@marioruizgonzalez.mx/how-install-tesseract-orc-and-pytesseract-on-windows-68f011ad8b9b)

### Development version

```{python}
pip install -i https://test.pypi.org/simple/ faced==0.0.4
```

### PyPi Version

```{python}
pip install faced
```

### Using faced

```{python}
import faced
from faced.load_data import *
from faced.cv_utils import *
from faced.main import *

x = load_data('lab.zip')
y = load_lab() #to avoid any issues

faced(x)
faced_keyword(y, "mark") #takes a long time
```

## 🛂 Quality Control (QC)

- Utilized inbuilt unit testing to test results vs expectations and everything seems to work just fine. This package right now focuses on learning python and seeing how packaging works in python.

## Warning

- Running this package means you will need your own tesseract engine for text identification. Install it and point your system to the executable.

- The program also requires an in built classifier and this might or might not work for OS other than windows. I will check on that later but that is all for now.

- It is confirmed that this package should work on Ubuntu as well so far as you have `opencv-python-headless` and your tesseract engine set then this should work.

## Publishing

### install build and build

```{bash}
pip install build
python -m build
```

### Install twine and upload to TestPyPi

Before the next steps, you need to setup an account with TestPyPi, and obtain a `token`.

Next you need to learn how to setup a `pypirc` file (repo config file) and that will be read by twine in the upload process.

```{bash}
pip install twine #python3 -m pip install --upgrade twine
python -m twine upload --repository testpypi dist/* #the repo name in pypirc is testpypi
```

### Upload to PyPi

If `pypirc` is well setup then this should go fine.

```{bash}
python -m twine upload --repository pypi dist/* #if repo is blank twine defaults to pypi so works either way
```

## Addon

We are authors of high level packages in `R` and `faced` is a gateway into the python world. Very little effort has been put into perfecting the functions here because there are more important projects to work on than `tesseract` and `opencv`. I still find time to polish my `python` and practice publishing as with this update but this is not a main project.

We learn this because some projects might entail in house built python packages so knowing how to package and publish is relevant.

## 🎇 Epilogue

- Working on CamFaceD which is a dynamic faced platform. CamFaceD can be used to train face detection although on a limited capacity. More to learn on this but steadily making progress and grateful for what I have learned so far.
