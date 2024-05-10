import unittest

from faced.classifiers.eye_classifier import *
from faced.classifiers.face_classifier import *

class TestClassifiers(unittest.TestCase):
     def test_face_classifiers(self):
        self.assertIsNotNone(use_builtin_face_classifier())

     def test_eye_classifiers(self):
        self.assertIsNotNone(use_builtin_eye_classifier())
        
unittest.main(exit=False)