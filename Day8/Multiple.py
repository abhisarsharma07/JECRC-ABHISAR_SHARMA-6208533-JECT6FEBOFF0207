'''
It is a type of inherirtence in which the properties will be derived from multiple parent class to a single child .

'''

class Parent_1:
     a=10
class Parent_2:
     b=100
class Parent_3:
     c=1000
class Parent_4:
     d=10000000
class child(Parent_1,Parent_2,Parent_3,Parent_4):
     pass

print(child.a,child.b,child.c,child.d)
## hum properties ko access kar sakte hain bina object banaye but for that it is accessible


