a=10
type(a)

a=input()
b=input()
c=a+b
print(c)
type(c)

a=20
id(a)

class Temp:
  pass

obj=Temp()
obj

a=30
b=a
a=a+b
print(a,b)
print(id(a))
print(id(b))
print(id(30))

print(id(60))

n1=int(input())
n2=int(input())
class Add:
  @staticmethod
  def result(n1,n2):
    return (n1+n2)

print(Add.result(n1,n2))


a,b,c=10,20,30
print(a,b,c)
result=a,b,c
type(result)



dir(int)


help('keywords')

import keyword
keyword.kwlist

len(keyword.kwlist)

type(None)

a=None

a=6.7
b=23+67676j
print(a+b)

print(id(True))
print(id(False))


print(True+True+False)
print(20*False)
print(20*True)
print(20*1)
print(20*0)

print('HELLO')
print("HELLO")
print('''HELLO''')

name="Abhisar"
print(id(name))
print(id(name[0:1]))
print(id(name[1:2]))

paragraph="""
Hello Abhisar Sharma This Side
Khamma Ghani

"""

print(paragraph)

name="Python"
print(name[-6]+name[-4]+name[-1])
print(name[-len(name)+1])

print(int())
print(float())
print(bool())
print(str())
print(complex())
print(list())
print(tuple())
print(set())
print(dict())

bool('')