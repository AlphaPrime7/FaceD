from setuptools import setup, Command
import os
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

setup(
    name='faced',
    version='0.0.5',
    author = "Tingwei Adeck",
    author_email = "awesome.tingwei@outlook.com",
    description = "FaceD for Static face detection",
    long_description = long_description,
    url = 'https://github.com/AlphaPrime7/faced',
    license = 'LICENSE',
    package_dir={"": "src"},
    package_data = {"faced.data": ['*.zip','*.png']},
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
        classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)