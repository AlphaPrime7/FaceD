from __future__ import absolute_import
import unittest

from utils.make_init import *

class TestMakeInit(unittest.TestCase):

	def test_make_init_type(self):
		self.assertRaises(TypeError, make_init , int(1))

	def test_make_init(self):
		self.assertEqual(make_init('bs'),make_init('mf')) #No DIRS!!
	
	def test_make_init(self):
		self.assertEqual(type(make_init('bs')),type(make_init('mf'))) #DIRS

	@unittest.skip('Exceptions specially handled')
	def test(self):
		with self.assertRaises(Exception) as context: #self.assertRaises(RuntimeError, afunction, arg1, arg2)
			make_init('ureshit')
		self.assertTrue('TEST GHOST FOLDERS' in context.exception)

unittest.main(exit=False)