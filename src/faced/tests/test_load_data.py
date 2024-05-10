import unittest

from faced.cv_utils.cv_utils import *

class TestLoadData(unittest.TestCase):
   def test_testzip(self):
      self.assertIsNotNone(load_test())

   def test_labzip(self):
      self.assertIsNotNone(load_lab())

   def test_png(self):
      self.assertIsNotNone(load_mark())

   def test_load_test(self):
      print(load_test())

   def test_load_lab(self):
      print(load_lab())

   def test_load_mark(self):
      print(load_mark())
    
unittest.main(exit=False)

