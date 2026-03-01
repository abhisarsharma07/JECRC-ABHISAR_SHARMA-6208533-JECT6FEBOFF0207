# t1 = ('Hello', 'Hi', 20, 30, 40.2, 9,6j, [1,2], 'Python', 'Jecrc', (1,2,3))
# new_coll1={}

# for i in t1:
#   if type(i) in [str, tuple]:
#     if len(i)%2==0:
#       new_coll1[i] = i[0] + i[-1]
#     else:
#       new_coll1[i] = i[len(i)//2]
# print(new_coll1)



#siR


coll = eval(input('Enter a collection'))
new_coll = {}
for i in coll:
     if type(i) in [str, tuple]:
        if len(i) % 2==0 :
          new_coll[i] = i[0] + i[-1]
        else:
          new_coll[i] = i[len(i)//2]
print(new_coll)