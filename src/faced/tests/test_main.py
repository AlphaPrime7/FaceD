import unittest
import time

from faced.cv_utils.cv_utils import *
from faced.main.faced import *
from faced.main.faced_by_keyword import *

class TestMain(unittest.TestCase):

   def time_it (func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + ' took ' + str(str((end - start) * 1000) + ' mil sec'))
        return result
    return wrapper

   @unittest.skip('Works fine, resource intensive')
   def test_faced(self):
      self.assertIsNotNone(faced(load_test()))

   @unittest.skip('Works fine, resource intensive')
   @time_it
   def test_facedbk(self):
      self.assertIsNotNone(faced_keyword(load_lab(), 'Mark'))
    
unittest.main(exit=False)
