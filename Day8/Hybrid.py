'''
It is mixture of more than one type of inheritence
'''
## Hybrid
class A:
  a = 'a'

class B(A):
  pass
class C(A):
  pass
class D(A):
  pass

class E(B,C,D):
  pass

obj = E()
print(obj.a)