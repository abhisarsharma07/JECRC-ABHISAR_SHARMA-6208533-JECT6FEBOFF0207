## Achieve the desired output for the below given input:
## Input :RAhul@123Gh
## OUTPUT: raHUL@123gH

##You cant use any inbuilt function

char =input()
result = ''

for i in char:
     if 'A' <= i <= 'Z':
       result += chr(ord(i) + 32)
     elif 'a' <= i <= 'z':
        result += chr(ord(i) - 32)
     else:
        result += i


print(result)