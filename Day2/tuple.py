# >>> tpl1=(1,2,3)
# >>> ## It is a Homogenous tuple collection
# >>> tpl2=(10,20,300,1.1) ##Heterogenous Tuple Collection
# >>> ## in which we can store both same or different data items
# >>> ##which will be enclosed between paranthesis
# >>> ## it is an immutable collection
# >>> tpl3 = 1, 1.1 ,1.9j, False,[1,2] , (3,4) , {10,20} , {1:1 ,2:2}
# >>> tpl3
# (1, 1.1, 1.9j, False, [1, 2], (3, 4), {10, 20}, {1: 1, 2: 2})
# >>> type(tpl3)
# <class 'tuple'>
# >>> ## data_type()
# >>> tuple()
# ()
# >>> bool()
# False
# >>> bool(tuple())
# False
# >>> tpl3
# (1, 1.1, 1.9j, False, [1, 2], (3, 4), {10, 20}, {1: 1, 2: 2})
# >>> tpl3[-1]
# {1: 1, 2: 2}
# >>> tpl[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'tpl' is not defined. Did you mean: 'tpl1'?
# >>> tpl3[3]
# False
# >>> ## Set is unordered
# >>> tpl3[-2][-1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object is not subscriptable
# >>> {1,2,3,False,'',9+9j}
# {False, 1, 2, 3, '', (9+9j)}
# >>> ## set is unorderd  so it will not be accessed
# >>>