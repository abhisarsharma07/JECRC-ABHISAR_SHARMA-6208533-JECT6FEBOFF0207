## INHERITENCE

'''
1. Single
2. Multi-level
3. Multiple
4. Hieherichal
5. Hybrid
'''

# Single level
## We will have a single parent & child class. Also the properties will be derived only one time


## Parent Class or, Super Class
## The class from which we are going to deriver the properties, is known as Parent Class

class Parent:
     bank_balance='54L'
     def __init__(self, *members):
          self.members = members

     def desc(self):
          print('I am the parent class')

## Child Class or , Sub Class
## The class in which we are going to deriving the properties, is known as child class

class Child(Parent):
     def __init__(self,child_name,*args):
          self.child_name =child_name
          super().__init__(args)
          
     def display(self):
          super().desc()
     
obj= Child('Rakesh','Mom', 'Dad')
# obj= Child()
print(obj.bank_balance)
# obj.desc()
print(obj.members)
print(obj.child_name)
obj= Child('Mom', 'Dad')
obj.display()



## Constructor Chaining : Calling Parent class's Constructor from inside child class's constructor is called as constructer chaining
