import os
import cv2 as cv

def use_builtin_eye_classifier():
    opencv_base_dir = os.path.dirname(os.path.abspath(cv.__file__))
    haar_algo = os.path.join(opencv_base_dir, 'data/haarcascade_eye.xml')
    return haar_algo