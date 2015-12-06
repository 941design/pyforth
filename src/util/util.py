#!/usr/bin/env python3


import doctest

from inspect import isclass
from inspect import ismethod
from inspect import isfunction
from inspect import isroutine
from inspect import isbuiltin
from inspect import getargspec



def arity(fn):
	"""Returns the arity of a callables without kwargs.

	>>> arity(lambda: 23)
	0
	>>> arity(lambda x: 23)
	1
	>>> def foo(x, y):
	...	pass
	>>> arity(foo)
	2

	#>>> arity(sum)
	#0 # TODO - unsupported callable
	>>> arity(int.__add__)
	2
	>>> class Foo(object):
	...     def __call__(self, x, y, z):
	...         pass
	>>> arity(Foo())
	3
	"""
	if isfunction(fn) \
	or ismethod(fn):
		return len(getargspec(fn).args)
	elif isroutine(fn):
		return len(getargspec(fn).args)
	elif isbuiltin(fn):
		1/0
	elif callable(fn):
		return len(getargspec(fn.__call__).args) - 1
	else:
		1/0



if __name__ == """__main__""":
	
	doctest.testmod()
