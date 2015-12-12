from .util import arity

from .symbol import Symbol
from .symbol import issymbol

from .environment import Environment

#import test

__all__ = [
	# classes:
	'Symbol',
	'Environment',
	# functions:
	'arity',
	'issymbol',
]


def load_tests(loader, tests, ignore):
	# TODO - When running 'python3 -m unittest util' only 4 tests are run,
	# as opposed to 'python3 -m unittest util.test' which runs 5 -- Why?.
	# Then it would also be nice to run tests from toplevel with
	# 'python3 -m unittest pyforth.util.test' -- How?

	# TODO - This package should be completely agnostic about tests!

	import util.test
	return test.load_tests(loader, tests, ignore)
