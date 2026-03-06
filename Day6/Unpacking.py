def add_no(*args):
    print(args,type(args))
    sum=0
    for i in args:
     if type(i) in [float, int] :
      sum+=i
    print(f'Addition : {sum}')
    return sum

add_no(*eval(input('Enter a list of values')))
## add_no(*[1,2,3,4,5])
## Thats why unpacking is used...


