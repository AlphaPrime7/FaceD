from __future__ import absolute_import

from faced.convert.converters import *
from faced.classifiers.face_classifier import *

def extract_faces(img): 
    img_arr = convert_pil_arr(img)
    gray_image = cv.cvtColor(img_arr, cv.COLOR_BGR2GRAY)
    haar_classifier = use_builtin_face_classifier()
    face_cascade = cv.CascadeClassifier(haar_classifier) 
    face_square = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=3)
    return face_square