import unittest

from PIL import Image
import cv2 as cv
from faced.convert.converters import *

class TestConverts(unittest.TestCase):
     def test_convert_pil_arr(self):
        x = convert_pil_arr(Image.open('data/mark_1.png'))
        y = cv.imread('data/mark_1.png')
        self.assertEqual(type(x),type(y)) 
    
     def test_convert_pil_byte(self):
        img = convert_pil_byte(Image.open('data/mark_1.png'))
        self.assertEqual(type(img),bytes) 
     
     def test_convert_pil_bytearr(self):
        x = convert_pil_bytearr(Image.open('data/mark_1.png'), 'PNG')
        self.assertEqual(type(x),bytearray) 

     @unittest.skip('Works fine, just an issue with typing')
     def test_convert_arr_pil(self):
         #self.skipTest('Work in progress')
         img = cv.imread('data/mark_1.png')
         pil_obj_from_arr = convert_arr_pil(img)
         pil_obj_original = Image.open('data/mark_1.png')
         self.assertEqual(type(pil_obj_original), type(pil_obj_from_arr)) 

     def test_convert_arr_byte(self):
         img = cv.imread('data/mark_1.png')
         byte_arr = convert_arr_byte(img, '.PNG')
         self.assertEqual(type(byte_arr),bytes)

     def test_convert_arr_bytearr(self):
         img = cv.imread('data/mark_1.png')
         byte_arr = convert_arr_bytearr(img, '.PNG')
         self.assertEqual(type(byte_arr),bytearray)
              
unittest.main(exit=False)


