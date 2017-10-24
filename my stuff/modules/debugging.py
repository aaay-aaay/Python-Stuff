def debug(func):
	def new_func(*args, **kwargs):
		print('Arguments: %s' % args)
		print('Keyword arguments: %s' % kwargs)
		returned = func(*args, **kwargs)
		print('Returned: %s' % returned)
		return returned
	return new_func

class observer():
	def __init__(self, *args, **kwargs):
		self.log = ['Initialised with args', args, 'and kwargs', kwargs]
	def __repr__(self):
		self.log += ['Repr()-ed']
		return self
	def __str__(self):
		self.log += ['Str()-ed']
		return self
	def __bytes__(self):
		self.log += ['Bytes()-ed']
		return self
	def __format__(self, *args):
		self.log += ['Format()-ed with args', args]
		return self
	def __iter__(self):
		self.log += ['Iter()-ed']
		return self
	def __next__(self):
		self.log += ['next()-ed']
		return self
	def __reversed__(self):
		self.log += ['reversed()-ed']
		return self
	def __getattribute__(self, *args):
		self.log += ['getattribute()-ed with args', args]
		if args[0] == 'log':
			return self.log
		return self
	def __getattr__(self, *args):
		self.log += ['getattr()-ed with args', args]
		return self
	def __setattr__(self, *args):
		self.log += ['setattr()-ed with args', args]
		return self
	def __delattr__(self, *args):
		self.log += ['delattr()-ed with args', args]
	def __dir__(self):
		self.log += ['dir()-ed']
	def __call__(self):
		self.log += ['called... what?']
		return self
	def __len__(self):
		self.log += ['len()-ed']
		return self
	def __contains__(self, *args):
		self.log += ['Somebody checked if', args, 'are in this object!']
		return self
	def __getitem__(self, *args):
		self.log += ['Somebody getitem()-ed with', args]
		return self
	def __setitem__(self, *args):
		self.log += ['Somebody setitem()-ed with', args]
		return self
	def __delitem__(self, *args):
		self.log += ['Somebody tried to delete', args]
		return self
	def __missing__(self, *args):
		self.log += ['Somebody tried to get', args, 'but it was missing!']
		return self
	def __add__(self, *args):
		self.log += [args, '+me']
		return self
	def __sub__(self, *args):
		self.log += [args, '-me']
		return self
	def __mul__(self, *args):
		self.log += [args, '*me']
		return self
	def __truediv__(self, *args):
		self.log += [args, '/me']
		return self
	def __floordiv__(self, *args):
		self.log += [args, '//me']
		return self
	def __mod__(self, *args):
		self.log += [args, '% me']
		return self
	def __divmod__(self, *args):
		self.log += ['I was divmod()-ed by', args]
		return self
	def __pow__(self, *args):
		self.log += [args, '**me']
		return self
	def __lshift__(self, *args):
		self.log += [args, '<<me']
		return self
	def __rshift__(self, *args):
		self.log += [args, '>>me']
		return self
	def __and__(self, *args):
		self.log += [args '&me']
		return self
	def __xor__(self, *args):
		self.log += [args, '^me']
		return self
	def __or__(self, *args):
		self.log += [args, '|me']
		return self
	def __radd__(self, *args):
		self.log += ['me+', args]
		return self
	def __rsub__(self, *args):
		self.log += ['me-', args]
		return self
	def __rmul__(self, *args):
		self.log += ['me*', args]
		return self
	def __rtruediv__(self, *args):
		self.log += ['me/', args]
		return self
	def __rfloordiv__(self, *args):
		self.log += ['me//', args]
		return self
	def __rmod__(self, *args):
		self.log += ['me %', args]
		return self
	def __rdivmod__(self, *args):
		self.log += [args, 'was divmod()-ed by me!']
		return self
	def __rpow__(self, *args):
		self.log += ['me**', args]
		return self
	def __rlshift__(self, *args):
		self.log += ['me<<', args]
		return self
	def __rrshift__(self, *args):
		self.log += ['me>>', args]
		return self
	def __rand__(self, *args):
		self.log += ['me&', args]
		return self
	def __rxor__(self, *args):
		self.log += ['me^', args]
		return self
	def __ror__(self, *args):
		self.log += ['me|', args]
		return self
	def __iadd__(self, *args):
		self.log += ['me+=', args]
	def __isub__(self, *args):
		self.log += ['me-=', args]
	def __imul__(self, *args):
		self.log += ['me*=', args]
	def __itruediv__(self, *args):
		self.log += ['me/=', args]
	def __ifloordiv__(self, *args):
		self.log += ['me//=', args]
	def __imod__(self, *args):
		self.log += ['me %=', args]
	def __ipow__(self, *args):
		self.log += ['me**=', args]
	def __ilshift__(self, *args):
		self.log += ['me<<=', args]
	def __irshift__(self, *args):
		self.log += ['me>>=', args]
	def __iand__(self, *args):
		self.log += ['me&=', args]
	def __ixor__(self, *args):
		self.log += ['me^=', args]
	def __ior__(self, *args):
		self.log += ['me|=', args]
	def __neg__(self):
		self.log += ['-me']
		return self
	def __pos__(self):
		self.log += ['+me']
		return self
	def __abs__(self):
		self.log += ['abs(me)']
		return self
	def __invert__(self):
		self.log += ['~me']
		return self
	def __complex__(self):
		self.log += ['complex(me)']
		return self
	def __int__(self):
		self.log += ['int(me)']
		return self
	def __float__(self):
		self.log += ['float(me)']
		return self
	def __round__(self, *args):
		self.log += ['Rounded with', args]
	def __ceil__(self):
		self.log += ['math.ceil(me)']
		return self
	def __floor__(self):
		self.log += ['math.floor(me)']
		return self
	def __trunc__(self):
		self.log += ['math.trunc(me)']
		return self
	def __index__(self):
		self.log += ['some_list[me]']
		return self
	def __eq__(self, *args):
		self.log += ['me == ', args]
		return self
	def __ne__(self, *args):
		self.log += ['me != ', args]
		return self
	def __lt__(self, *args):
		self.log += ['me < ', args]
		return self
	def __le__(self, *args):
		self.log += ['me <= ', args]
		return self
	def __gt__(self, *args):
		self.log += ['me > ', args]
		return self
	def __ge__(self, *args):
		self.log += ['me >= ', args]
		return self
	def __bool__(self, *args):
		self.log += ['if me:']
		return self