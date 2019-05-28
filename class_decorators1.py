def decorator(cls):
	class wrapper:
		def __init__(self, *args, **kwargs):
			self.cls=cls(*args, **kwargs)

		def __getattr__(self, attr_name):
			print 'looking for {}'.format(attr_name)
			return getattr(self.cls, attr_name)
	wrapper.__name__ = cls.__name__
	return wrapper
