'''
def func_name(*args):
  statement block

func_name(val1,val2,val3,...,valn)  
'''
## Create a function which can take n number of int or float numbers and return only their addition

# def add_nums(*args):
#   args = list(args)
#   print(args, type(args)) ## if without list then by default it is tuple
#   sum = 0
#   for i in args:
#     sum += i
#   print(f'Addition: {sum}')  
# #   return sum
# add_nums(1,2,3,10.3,5,7)
# # print(add_nums(1,2,3,10.3,5,7))



## Create a function which will take n no of inputs from ther user and return the sum of only int & floating numbers. Please make sure that, user is capable of passing all tyoes of values

def add_no(*args):
    print(args,type(args))
    sum=0
    for i in args:
     if type(i) in [float, int] :
      sum+=i
    print(f'Addition : {sum}')
    return sum

add_no(1,2,1.1,3+9j,'abr',False,'Hello',[1,2,3])

