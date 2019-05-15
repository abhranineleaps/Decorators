# Decorators
________________

1. Decorators are callable that process other callables. They come in two flaovours, function decorators and class decorators.

Function Decorators:
runs one function through another function at end of a def statement and rebinds original function name to result.

`decorator first example`

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

Takeaway:

so this decorator returns afunc intact, and whatever is returned is bound to name of original function.
No __name__ info gets lost, no docstrings lost.

