# Decorators

Decorators are callable that process other callables. They come in two flaovours, function decorators and class decorators.

Function Decorators:

Runs one function through another function at end of a def statement and rebinds original function name to result.

`decorator first example`

```
def dec(afunc):
	return afunc

@dec
def pname():
	print 'vijay'

>>> pname()
'vijay'
>>> pname
<function pname at 0x1038c95f0>

>>> pname.__name__
'pname'
```
Takeaway:

1. so this decorator returns afunc intact, and whatever is returned is bound to name of original function.
2. No `__name__` info gets lost, no docstrings lost.

`decorator second example`

```
>>> def dec(afunc):
		print 'vijay'
		return afunc

>>> @dec
	def afunc():
		print 'shanker'
'vijay'

>>> afunc()
'shanker'

>>> afunc()
'shanker'

>>> pname.__name__
'pname'
```

Takeaway:
1. binding happens one time, i.e at end of def statement, so 'vijay' gets printed the moment def statement ends, 
and any further call to function afunc() only prints 'shanker'

2. Once the decoration or binding happens, calling the original function will call whatever is the output of decoration.
```
@decorator
def myfunc(1,2):
	print 'in func'

# the above and decorator(myfunc)(1,2) are essentially same.	
```

3. `__name__` info still remains intact and if provided will be preserved.

`decorators returning wrappers`

```
def decorator(afunc):
	def wrapper(*args):
		afunc(*args)
	return wrapper

@decorator
def pname(name):
	print name

>>> pname.__name__
'wrapper'

>>> pname
<function wrapper at 0x10ffd3410>
```

Takeaway:
1. decorators when coded this way return a wrapper function, which retains the original function passed to it in scope.
2. next time the decorated function gets called, the wrapper function gets called, along with params if any.
the wrapper function which have the original function in scope can use it along with the params passed to it.
3. after decoration or name binding, the original function is assigned whatever decorator choose to return, which
in this case is wrapper function, leading to loss of correct __name__ attribute and docstring.
4. we can preserve __name__ and docstring by making changes in our decorator definition, below is an example:

```
def decorator(afunc):
	def wrapper(*args):
		afunc(*args)
	wrapper.__name__ = afunc.__name__
	wrapper.__doc__ = afunc.__doc__	
	return wrapper
```

third example can be coded as a class decorator, like below, explanation to follow:

```
class decorator:
	def __init__(self, afunc):
		self.afunc = afunc

	def __call__(self, *args):
		self.func(*args)

```












