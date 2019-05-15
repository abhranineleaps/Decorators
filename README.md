# Decorators
________________

1. Decorators are callable that process other callables. They come in two flaovours, function decorators and class decorators.

Function Decorators:
runs one function through another function at end of a def statement and rebinds original function name to result.

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
...		print 'vijay'
...		return afunc

>>> @dec
...	def afunc():
...		print 'shanker'
...
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
...	print 'in func'

# above is essentially same as
>>> myfunc = decorator(myfunc)(1,2)	
```

3. `__name__` info still remains intact and if provided will be preserved.

`decorators as wrappers`
















