# input : [10,2.2,5, 'Hello', [100,200], 99.9]
# output: 99.9

# li =[10,2.2,5, 'Hello', [100,200], 99.9]
# maxi = 0
# for i in li:
#      if(type(i)==int or type(i)==float):
#           maxi = i
#           if(maxi>i+=1):
#                maxi = i+=1:




## Sir 

coll = [1, 'HELLO', 3.2, [1,2,3],99.9]
max= coll[0]

for i in coll:
     if type(i) in [int,float]:
          if i>max:
               max=i
print(max)