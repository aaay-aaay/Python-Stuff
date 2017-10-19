#(lambda n : [c for c in ().__class__.__bases__[0].__subclasses__() if c.__name__ == n][0])('Sized').__len__.__globals__['__builtins__'] # builtins

eval('''(lambda n : [c for c in ().__class__.__bases__[0].__subclasses__() if c.__name__ == n][0])('Sized').__len__.__globals__['__builtins__']['exec'](\'\'\'import sys
sys.exit()\'\'\', {'__builtins__' : ((lambda n : [c for c in ().__class__.__bases__[0].__subclasses__() if c.__name__ == n][0])('Sized').__len__.__globals__['__builtins__'])})''')