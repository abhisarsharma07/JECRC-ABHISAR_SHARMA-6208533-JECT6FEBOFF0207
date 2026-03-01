# Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> list1=[1,2,3,4,5]
# >>> list1
# [1, 2, 3, 4, 5]
# >>> list2=[1,1.2,3.4+90.2j, True, 'hello']
# >>> list2
# [1, 1.2, (3.4+90.2j), True, 'hello']
# >>> ##list1 is a homogenous list collection
# >>> ##list 2 is a heterogenous list collection
# >>> ##List is atype of collection
# >>> ##in which we can store both homogenous or heterogenous data items(values)
# >>> ##All the values will be enclosed with in square brackets
# >>> ##values will be seperated by comma
# >>> type(list1)
# <class 'list'>
# >>> list1
# [1, 2, 3, 4, 5]
# >>> ##append()--> It is  used to add a new value at the very end of an existing collection
# >>> ##append()--> It is  used to add a new value at the very end of an existing list collection
# >>> dir(list)
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# >>> dir(list.append)
# ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__objclass__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
# >>> help(list.append)
# Help on method_descriptor:

# append(self, object, /)
#     Append object to the end of the list.

# >>> list1.append(6)
# >>> list1
# [1, 2, 3, 4, 5, 6]
# >>> list1.append(7)
# >>> print(list1.append(7))
# None
# >>> #insert()
# >>> help(list.insert)
# Help on method_descriptor:

# insert(self, index, object, /)
#     Insert object before index.

# list1.insert(2,100)
# list1
# [1, 2, 100, 3, 4, 5, 6, 7, 7]
# list1 = [1,2,3]
# list1
# [1, 2, 3]
# ## 0 1 2
# ## index =4, add3; >len(list_coll)
# list1.insert(4,3)
# list1
# [1, 2, 3, 3]
# ##it will insert if it exceed the length if list then it will insert at veryb end of list
# list1.insert(10,4)
# list1
# [1, 2, 3, 3, 4]
# list1.insert(100,5)
# '
# list1
# [1, 2, 3, 3, 4, 5]
# list1
# [1, 2, 3, 3, 4, 5]
# list1.insert(-1,-1)
# list1
# [1, 2, 3, 3, 4, -1, 5]
# list1.insert(-9,-1)
# list1
# [-1, 1, 2, 3, 3, 4, -1, 5]
# len(list1)
# 8
# ## if the index size is less then length of list then it will add the value at very beginning
# list1.insert(1,2,3)
# Traceback (most recent call last):
#   File "<pyshell#43>", line 1, in <module>
#     list1.insert(1,2,3)
# TypeError: insert expected 2 arguments, got 3
# ## it will add only one value at a time
# help(list.extend)
# Help on method_descriptor:

# extend(self, iterable, /)
#     Extend list by appending elements from the iterable.

# list1.extend([100,200,300])
# list1
# [-1, 1, 2, 3, 3, 4, -1, 5, 100, 200, 300]
# ## it will append many values at the end
# list1.extend([i for i in range(100,201)])
# list1
# [-1, 1, 2, 3, 3, 4, -1, 5, 100, 200, 300, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]
# ##with the help of this looping statement we can add
# list2 =[1,2,3]
# list2
# [1, 2, 3]
# list2.extend([(1,2,3)])
# list2
# [1, 2, 3, (1, 2, 3)]
# list2.extend(20,30,40)
# Traceback (most recent call last):
#   File "<pyshell#56>", line 1, in <module>
#     list2.extend(20,30,40)
# TypeError: list.extend() takes exactly one argument (3 given)
# list2.extend((1,2,3))
# list2
# [1, 2, 3, (1, 2, 3), 1, 2, 3]
# ## ek ek karke append





# list1=[1]
# list2=[2]
# id(list1),id(list2)
# (1813633454976, 1813633357376)
# list3 = list1 + list2
# id(list3)
# 1813633135872
# id(list1)
# 1813633454976
# list.extend('GM')
# Traceback (most recent call last):
#   File "<pyshell#71>", line 1, in <module>
#     list.extend('GM')
# TypeError: descriptor 'extend' for 'list' objects doesn't apply to a 'str' object
# list1.extend('GM')
# list1
# [1, 'G', 'M']
# id(list1)
# 1813633454976
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ## pop()
# ##pop()
# ##pop(index=-1) -> by default -> always it will return it from negative indexing
# list1.pop()
# 10
# list1.pop()
# 9
# list1
# [1, 2, 3, 4, 5, 6, 7, 8]
# list1.pop()
# 8
# list1.pop(2)
# 3
# help(list.pop())
# Traceback (most recent call last):
#   File "<pyshell#85>", line 1, in <module>
#     help(list.pop())
# TypeError: unbound method list.pop() needs an argument
# help(list.pop)
# Help on method_descriptor:

# pop(self, index=-1, /)
#     Remove and return item at index (default last).
    
#     Raises IndexError if list is empty or index is out of range.

# list1
# [1, 2, 4, 5, 6, 7]
# list1.pop(10)
# Traceback (most recent call last):
#   File "<pyshell#88>", line 1, in <module>
#     list1.pop(10)
# IndexError: pop index out of range
# list1.pop(-10)
# Traceback (most recent call last):
#   File "<pyshell#89>", line 1, in <module>
#     list1.pop(-10)
# IndexError: pop index out of range
# ## I know what value i should remove
# ## remove()
# list1
# [1, 2, 4, 5, 6, 7]
# list1.remove()
# Traceback (most recent call last):
#   File "<pyshell#93>", line 1, in <module>
#     list1.remove()
# TypeError: list.remove() takes exactly one argument (0 given)
# list1.remove(7)
# list1
# [1, 2, 4, 5, 6]
# list2=[1,1,2,2,3,3,4,4,5,5]
# help(list.remove)
# Help on method_descriptor:

# remove(self, value, /)
#     Remove first occurrence of value.
    
#     Raises ValueError if the value is not present.

# list2.remove(2)
# list2
# [1, 1, 2, 3, 3, 4, 4, 5, 5]
# list2.remove(1)
# list2
# [1, 2, 3, 3, 4, 4, 5, 5]
# my_list = [100 , 200.02, 'HELLO' , [1,2,3] ]

# my_list
# [100, 200.02, 'HELLO', [1, 2, 3]]
# my_list[len(my_list)-1]
# [1, 2, 3]
# my_liat[len(my_list)-1] ##[1,2,3]
# Traceback (most recent call last):
#   File "<pyshell#105>", line 1, in <module>
#     my_liat[len(my_list)-1] ##[1,2,3]
# NameError: name 'my_liat' is not defined. Did you mean: 'my_list'?
# my_list[len(my_list)-1] ##[1,2,3]
# [1, 2, 3]
# len(my_list[len(my_list)]-1) ##[1,2,3]
# Traceback (most recent call last):
#   File "<pyshell#107>", line 1, in <module>
#     len(my_list[len(my_list)]-1) ##[1,2,3]
# IndexError: list index out of range
# len(my_list[len(my_list)-1]) ##[1,2,3]
# 3
# my_list[len(my-list)-1][len(my_list[len(my_list)-1])-1]
# Traceback (most recent call last):
#   File "<pyshell#109>", line 1, in <module>
#     my_list[len(my-list)-1][len(my_list[len(my_list)-1])-1]
# NameError: name 'my' is not defined
# my_list[len(my_list)-1][len(my_list[len(my_list)-1])-1]
# 3
# my_list[len(my_list)-2]
# 'HELLO'
# len(my_list[len(my_list)-2])
# 5
# my_list[-2][-2]
# 'L'
# ##1 use only negative indexing
# my_list[-1]
# [1, 2, 3]
# mylist[-1][-len(my_list[-1])]
# Traceback (most recent call last):
#   File "<pyshell#116>", line 1, in <module>
#     mylist[-1][-len(my_list[-1])]
# NameError: name 'mylist' is not defined. Did you mean: 'my_list'?
# my_list[-1][-len(my_list[-1])]
# 1
