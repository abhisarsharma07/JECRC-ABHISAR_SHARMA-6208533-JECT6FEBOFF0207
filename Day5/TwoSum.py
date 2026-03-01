def twoNun(coll,target):
     for i in range(len(coll)-1):
          for j in range(i+1,coll):
               if coll[i]+ coll[j]==target:
                    return [i,j]
     return -1