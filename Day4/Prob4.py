# coll = {'a' : 1 ,'b': 2}
# for i in coll:
#      print(i)

coll = {'a' : 1 ,'b': 2}
new_coll={}
for i in coll:
     new_coll[coll[i]] = i
print(new_coll)