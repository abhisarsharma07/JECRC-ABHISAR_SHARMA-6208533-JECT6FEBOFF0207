## Using the same method name or operator to perform two or more different operation

class Temp:
     def sum(self, a, b):
          print(a+b)

     add_two_sum=sum # monkey Patching -> we can solve the problemmm ## i can access the method area again.

     def sum(self,a,b,c):
          print(a+b+c)

obj = Temp()
# obj.sum(10,20)
obj.add_two_sum(10,20)
obj.sum(10,20,30)
# obj.sum(10,20)
# TypeError: Temp.sum() missing 1 required positional argument: 'c'
## It will not happend


#  In python, if we wnat to perform method overloading then it will act as method overloading
# In other programming language, based upon no of arguments, the respective method block will get executed. But in python , it will never happeenn

# Method Overriding is a phenomenon the prev method's address with the latest one..

# Monkey Patching ->It is a process of storing the prev method's address inside a variable before overriding the method area's adddress. Using that var, we can access the prev method's method area.