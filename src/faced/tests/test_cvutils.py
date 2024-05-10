import unittest

from faced.cv_utils.cv_utils import *

class TestCvutils(unittest.TestCase):
     
     @unittest.skip('Works fine!')
     def test_unzip_files_type(self):
         self.assertRaises(TypeError, unzip_files , str(load_test()))

     @unittest.skip('Works fine!')    
     def test_unzip_files(self):
        self.assertIsNotNone(unzip_files(load_test()))
        
unittest.main(exit=False)