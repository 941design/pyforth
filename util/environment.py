class Environment(object):
	"""Associative tree like structure.
	
	Bindings are shadowed not overwritten if reassigned.  When unbinding/deleting 
	a shadowing binding, the shadowed binding becomes visible again.
	An environment may be initialized with an optonal dict of bindings and an optional
	parent environment.  If a key is not found in the current environment search traverses
	upward.

	>>> env = Environment()
	>>> env[0] = 'x'
	>>> env[0]
	'x'
	>>> env[0] = 'y'
	>>> env[0]
	'y'
	>>> del(env[0])
	>>> env[0]
	'x'
	>>> other = Environment(bindings={1: 'z'}, parent=env)
	>>> other[0]
	'x'
	>>> other[1]
	'z'
	
	#>>> env[1]
	#Error # TODO - read doctest doc how to express this
	"""


	def __init__(self, bindings={}, parent={}):
		self.parent = parent
		self.bindings = bindings


	def __getitem__(self, key):
		if key in self.bindings:
			return self.bindings[key]
		else:
			return self.parent[key]


	def __setitem__(self, key, value):
		# TODO - only create new instance if key already exists in self!
		# RECONSIDER - then we would no longer have closures, because we may
		# manipulate a referenced environment
		self.parent = Environment(self.bindings, self.parent)
		self.bindings = { key: value }


	def __delitem__(self, key):
		# TODO - if this was the last binding, unlink parent
		if key in self.bindings:
			del(self.bindings[key])
		else:
			del(self.parent[key])
