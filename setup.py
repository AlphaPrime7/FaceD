from setuptools import setup, Command
import os
import sys
import subprocess
import platform

class CleanCommand(Command):
    description = "Cleanup after build" #./*.tgz kept
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        if platform.system() == "Windows":
            os.system('del /s *.tmp *.pyc *.egg-info *.egg dist build -r -Force')
        elif platform.system() == "Darwin":
            os.system('rm -vrf ./build ./dist ./*.pyc ./*.egg-info')

with open("README.md", "r", encoding = "utf-8") as rme:
    long_description = rme.read()

if not sys.version_info[0] == 3 and sys.version_info[1] == 8:
    sys.exit("Python >=3.8 is required to run this package")

#subprocess.check_call([sys.executable, "-m", "pip", "install", 'opencv-python-headless'])

#COMMANDS = ['x = y']
setup(
    name='faced',
    version='0.0.8',
    author = "Tingwei Adeck",
    author_email = "awesome.tingwei@outlook.com",
    description = "FaceD for Static face detection",
    long_description = long_description,
    url = 'https://github.com/AlphaPrime7/faced',
    license = 'LICENSE',
    #packages=find_packages(),
    package_dir={"": "src"},
    package_data = {"faced.data": ['*.zip','*.png']},
    include_package_data=True,
    python_requires='>=3.12.9',
    install_requires=[
        'opencv-contrib-python-headless',
        'opencv-python-headless',
        'opencv-python',
        'pytesseract>=0.3.10',
        'pillow>=10.3.0',
        'matplotlib>=3.9.0'
    ],
    #py_modules=['main'], #where the modules are found
    #test_suite='tests',
    zip_safe=False,
        classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)