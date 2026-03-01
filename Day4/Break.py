##Whenever python interpreter will encounter "break" keyword it will simply stop its execution on  this partucular line and make the interpreter to go outside of the loop. In future , control will never go inside the same loop

coll= [1,1.2,3,4,5, 'HI']

i,flag = coll[0],True


# for j in coll:
#      if type(i) == type(j):
#           flag=True
#      else:
#           flag=False
# # if flag==True:  it is also correct
# if flag:
#      print('Homogenous Collection')
# else:
#      print('Hetero Collection')

for j in coll:
     if type(i) == type(j):
          flag = False
          break
# if flag==True:  it is also correct
if flag:
     print('Homogenous Collection')
else:
     print('Hetero Collection')

