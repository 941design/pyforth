#!/usr/bin/env python3


import doctest


class Symbol(object):
	"""Unique symbolic values, which may be given an optional name.

	>>> Symbol('A')
	<A>
	>>> Symbol('A') == Symbol('A')
	True
	>>> Symbol('A') is Symbol('A') # TODO - should be singleton!
	False
	"""


	def __init__(self, name='??'):
		self.name = name


	def __eq__(self, other):
		return isinstance(other, Symbol) \
			and self.name == other.name


	def __hash__(self):
		return hash(self.name)


	def __repr__(self):
		return '<' + str(self.name) + '>'

	
	def __str__(self):
		return repr(self)



def symbol(obj):
	"""True if parameter is of type Symbol.
	
	"""
	return isinstance(obj, Symbol)


if __name__ == """__main__""":

	doctest.testmod()
