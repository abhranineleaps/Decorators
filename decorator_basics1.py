class decorator(object):
	def __init__(self, fn):
		self.__name__ = fn.__name__
		self.__doc__ = fn.__doc__
		self.func = fn


	def __call__(self, *args):
		return self.func(*args)

@decorator
def pname(name):
	"""print name"""
	print name

class tryMe(object):
	def __init__(self, arg1, arg2):
		self.a = arg1
		self.b = arg2

	@decorator
	def pname(self, *args):
		'''
		>>> t = tryMe(1,2)
		>>> t.pname('vijay', 'shanker')
		('shanker',)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "decorator_basics1.py", line 9, in __call__
    return self.func(*args)
  File "decorator_basics1.py", line 23, in pname
    print self.a
AttributeError: 'str' object has no attribute 'a'

This happens because the decoration of method results in instance of decorator class. Calling that instance will 
invoke its __call__ method, and now t.pname('vijay', 'shanker') call will result in self getting 'vijay' assigned to it as value
and args will have the usual tuple. Thus, `self` being a string object now has no attribute 'a', the error. 
		'''
		print args
		print self.a
		print self.b