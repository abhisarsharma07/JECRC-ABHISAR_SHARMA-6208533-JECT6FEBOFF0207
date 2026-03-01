''' 
It is a type pf statement which controls the execution of a program.
'''

## Conditional Statement : Based upon one condition , the flow of the execution of a program will be decided
'''
if statement
if else statement
elif statement 
nested if statement
'''

'''
in general we have 2 type of looping
1. entry --> for and while (python support only entry one)
2. exit --> do while
'''

# WAP to check whether the username & password is correct or not. If correct print login successfully completed -. if not , do nothing...

user = {
     'username' : 'user123',
     'password' : '****'
}
un = input("ENTER USERNAME:")
pwd = input("ENter Password:")
## IF the condition is true then only if block will get executed...
if un == user['username'] and pwd == user['password'] :
     print('Login Successfully Completed')
else:
     print(' incorrect username or password')
print('Program Get ended')



# if statement -:


