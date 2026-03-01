# Types of Operators

# Arthemetic operators
# a. addition (+)
# b. Subtraction (-)              
# c. Multiplication (*)
# d. Division,
#      1.True Division(/), Floating Point Number
#      2.Floor Division (//), Int Number
#      3.Modulus(%),
# e. Exponential/ Power Operator 

# 10 + 20, 10 and 20 are operands

# 2. Relational Operator
#    1. Equal to (==),
#    2. Not Equal to (!=),
#    3. Less than (<),
#    4. Greater than (>),
#    5. Less than or equal to (<=),
#    6. Greater than or equal to (>=),

# It will return Bool Value( Final Result)

# 3.Logical Operator :
#  1. Logical and (and),
#  2. Logical or (or),
#  3. Logical not (not),

# ** If all the conditions are True,then only "and" will return output as true.
# Otherwise False

# **If any of the conditions is True, then "or will" return output
# as True . If both the conditions are False , final output will be False.

# 4. Assignment Operator:
#    1.Assignment (=)
#    2. Argumented Assignment Operator:
#    3. += , -= ,*= , /= ,//= , %=, etc.


# 5. Bitwise Operator:
#   1. Bitwise AND (&),
#   2. Bitwise OR (|),
#   3. Bitwise NOT (~),
#   4. Bitwise XOR (^),
#   5. Bitwise Right Shift (>>),
#   6. Bitwise Left Shift (<<),



# 6. Membership Operator: using it we can check that whether a value is present in the collection or not
# a. in
# b. not in
# >>> s= 'hello'
# >>> 'h' in s
# True
# >>> 'H' in s
# False
# >>> 'H' not in s
# True
# >>> 'h' not in s
# False
# ** in operator will give output as True if the value belong to a collection, otherwise false
# ** not in operator will give output as True if the value is not there inside a collection, otherwise False

# 7. Identity Operator:
# a. is
# b. is not
# >>> a = 10
# >>> b = a
# >>> a
# 10
# >>> b
# 10
# >>> a is b
# True
# >>> c = 20
# >>> a is 20
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# >>> a is c
# False
# >>> a is not c
# True
# >>> a is not b
# False
# >>> 20 is 20
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# True
# >>> 20 is 30
# <stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
# False
# >>> 20 is not 30
# <stdin>:1: SyntaxWarning: "is not" with 'int' literal. Did you mean "!="?
# True
# >>> 20 is not 20
# <stdin>:1: SyntaxWarning: "is not" with 'int' literal. Did you mean "!="?
# False

# ** Is operator will give output as True if both the values are belongs to the same memory location. Otherwise, False.
# ** Is not operator will give output as True if the values are not pointig towards the same memory location. Otherwise False.

