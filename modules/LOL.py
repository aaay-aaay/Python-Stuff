order_list = (lambda list_to_order : (lambda func, arg, arg2 : func(func, arg, arg2))(lambda me, arg, arg2 : arg if (len(arg2) == 0) else me(me, (lambda func, theArg, theArg2 : func(func, theArg, theArg2))(lambda me, arg, arg2 : arg if (len(arg2) == 0) else me(me, (arg[:(arg2[0])] + [arg[arg2[0]+1]]+ [arg[arg2[0]]]+ arg[(arg2[0]+2):] if arg[arg2[0]] > arg[arg2[0]+1] else arg), arg2[1:]), arg, range(0, len(arg)-1)), arg2[1:]), list_to_order, range(0, len(list_to_order))))([5, 8, 1, 6, 8, 34, 5])