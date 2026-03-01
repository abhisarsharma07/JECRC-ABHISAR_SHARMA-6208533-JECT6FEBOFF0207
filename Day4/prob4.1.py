## WAP to take a character from the user and convert it into lowercase
# if it is in uppercase or viceversa


char = input()

if 'A' <= char <= 'Z':
    print(chr(ord(char + 32)))
elif 'a' <= char <= 'z':
    print(chr(ord(char - 32)))
else:
    print(char)

# A-->a
# a-->A
# 1-->1
# *-->*

