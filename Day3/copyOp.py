a=100
## Immutable Data Type
b=a
b=a=100
## b also store reference of 100
a ## 100
b ## 100
id(a)
id(b)

l1=[1,2,3,4,5]
l2=l1
## Dest var = Source Var
l1
l2
id(l1)
id(l2)
id(l1),id(l2)
l1
l1.append(5)
l1
l2
## Same changes are visible in another variable also in General copy
## In case of mutable collection if we want to perform copy operation either shallow or deep copy

##dest_var = source_var.copy() : Shallow Copy
list1=[1,2,3]
list2 = list1.copy()
list1,list2
id(list1)
id(list2)
list1.pop()
list2
list1

import copy
l1 =[1,2,[10,20]]
l2= copy.deepcopy(l1)

id(l1),id(l2) ## Adress of outer collection
id(l1[-1]), id(l2[-1])
l1[-1].append(30)
l1
l2
## Outer and inner different memory allocation is happening.
l2[-1].pop()
l1,l2