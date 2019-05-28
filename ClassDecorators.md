# Class Decorators

First introduced in python2.6, class decorators can be used as wrapper to instance creation call of a class, augmenting its behaviour.

```
@decorator
class Person(object):
	def __init__(self, name):
		self.name = name 

is same as => Person = decorator(Person)  
```
class gets passed to decorator and whatever decorator returns is assigned back to Person. Any call to create instance will be actually
a call to whatever is returned by decorator.
i.e `Person('vijay')` is actually `decorator(Person)('vijay')`

so a simplest example of a class decorator can be:
```
def decorator(cls):
	return cls
```  

we can use class decorators to intercept attribute fetches. Let's look at this example:
```
def decorator(cls):
	class wrapper:
		def __init__(self, *args, **kwargs):
			self.cls=cls(*args, **kwargs)

		def __getattr__(self, attr_name):
			print 'looking for {}'.format(attr_name)
			return getattr(self.cls, attr_name)
	return wrapper


# decorating a class Person

@decorator
class Person(object):
	def __init__(self, name):
		self.name = name

p = Person('vijay')
p.name # prints vijay
p.age 
looking for age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "class_decorators1.py", line 8, in __getattr__
    return getattr(self.cls, attr_name)
AttributeError: 'Person' object has no attribute 'age'
```

Like in examples where we were decorating classes, name rebinding happened here, therefore `Person.__name__` will give `wrapper`.
To preserve `__name__` attribute, we can set `wrapper.__name__` to `cls.__name__`

