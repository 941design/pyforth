from unittest import TestCase

from util import arity



class ArityTest(TestCase):

	def test_lambda(self):
		actual = arity(lambda x, y, z: 23)
		self.assertEqual(actual, 3)

