# TODO - How do we run this from a parent package?

from doctest import DocTestSuite
# Importing modules for doctesting
import util.util as util_module
import util.environment as environment_module
import util.symbol as symbol_module


# TODO - How can we teak unittest to detect all classes in this package?
from util.test.ArityTest import ArityTest



def load_tests(loader, tests, ignore):

	# TODO - uncomment once top level package gets doctests!
	#tests.addTests(doctest.DocTestSuite(util)) 
	
	for module in [ util_module
		      , symbol_module
		      , environment_module ]:

		# TODO - Is it possible to add classes instead of modules for doctesting?
		tests.addTests(DocTestSuite(module))


	return tests
