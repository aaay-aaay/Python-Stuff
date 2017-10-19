def debug(func):
	def new_func(*args, **kwargs):
		print('Arguments: %s' % args)
		print('Keyword arguments: %s' % kwargs)
		returned = func(*args, **kwargs)
		print('Returned: %s' % returned)
		return returned
	return new_func