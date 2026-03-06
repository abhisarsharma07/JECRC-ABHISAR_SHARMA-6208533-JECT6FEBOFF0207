## Function for String Data Type

'''
1. lower
2. upper
3. capitalize
4. title
5. strip
6. lstrip
7. rstrip
8. replace
9. index
10. split
11. join
12. startswith
13. endswith
14. isdigit
15. isalpha
16. islower
17. isupper
'''

s= 'ABHISAR'
print(s.lower())

p='Python123%^^&*'
print(p.lower())

help(str.capitalize)

print(s.strip())
help(str.title)
help(str.strip)
help(str.lstrip)
help(str.rstrip)



a = '   JECRC   ' #
b='JECRC'
print(a.strip()) 
print(b.strip('C'))

c='    JECRC'
d='JECRC'
print(c.lstrip())
print(d.lstrip('J'))
print('Python'.lstrip('n'))


t= 'JECRC'

print(t.replace('C','c'))
print(t.index('RC'))  ## It will return the substring's starting index
## if substring is not present- >In case of index() fntion it will return value error but in case of find function it will return -1

x = 'I Love listening Music'
print(x)
print(x.split())

x='I-Love-listening-Music'
print(x.split('Music'))
print(x.split('-'))

list_of_str= x.split('-')
print(list_of_str)

help(str.join)
print(' '.join(list_of_str))
print('@'.join(list_of_str))
print('-'.join(list_of_str))


y= "Python"
help(str.startswith)
print(y.startswith('P'))
print(y.startswith('Z'))
print(y.startswith('Py'))

print("Endswith")
print(y.endswith('n'))
print(y.endswith('P'))


w= '123'
print(w.isdigit())
print(y.isalpha())

u="IOOP"
l="ifheebfgkj"
print(l.islower())
print(u.isupper())

# "-------------------------------------------------------------------------------------------------------------------------------------"
print("---------------------------------------------")

## Functions for list data types
'''
1. append
2. insert
3. extend
4. pop
5. remove
6. clear
7. sort
8. reverse
9. index
10. count
'''
l1 = [4,3,6,1,2,8,8,5]
l1.append(0)
print(l1)
l1.insert(2,99) ## add value at index
print(l1)
l1.extend([22,11,333])
print(l1)
l1.pop()
print(l1)
l1.remove(8) ## Remove first occurence from the list
print(l1)
# l1.clear()
# print(l1)





## Sort and reverse
l =[2,7,1,91,22]
l.sort()
print(l) ## Reverse flag is False By-default -> Ascending Order

l.sort(reverse=True) ## if Reverse flag is True =>Descending Order
print(l)

l=[1,2,3,4,5]
l.reverse()
print(l)

l=[1,2,0.5,1]  ##[1,0.5,2,1]
l.reverse()
print(l)

l.clear()
print(l)

## Function for tuple Data Type

'''
1.index
2.count

'''
t1 = (1,2,3,4,5,6,6,1)
print(t1.index(2))
print(t1.count(1))




## Set Functions


'''
1. add()
2. remove()
3. discard()
4. pop()
5. clear()
6. union()
7. intersection()
8. difference()
'''

help(set.add)

## add(object)  s={1,2,3,3,1.5} ==== {1,2,3,1.5}

# var_name.add(object)
s={1,2,3,3,1.5}
s.add(50) #{1,2,3,3,1.5,50}

print(s)

# s= {1,2,3,(10,20),{1:1,2:2}}
print(s)

s.add(100)

print(s)

value=2
s.add(value) # ye add to karega but print karega sirf ek value

# s.add([1,2,3])
s.add((1,2,3))
print(s)


s.add(3+9j)
print(s)

# remove

s.remove(3+9j)
print(s)
# s.remove(10)



# Discard -> if object is not present isme error nahi aayega jabki remove mein aayega
s.discard(1)
print(s)

# pop() it will randomly pop the value


s.pop()
print(s)
s.pop()
print(s)

#claar

s.clear()
print(s)

s1={1,2,3}
s2={2,3,4}

# union
s1={1,2,3}
s2={2,3,4}


s3=s1.union(s2)## it is returning a new set so yeah it is returning 
print(s3)
s4=s1.union({3,4,5},{1,2,3},{8,9,7},{5,4,7}) ## Packing concept
print(s4)


# Intersection

s1={1,2,3}
s2={2,3,4}
s3= s1.intersection(s2)
print(s3)


# difference

s3=s1.difference(s2) # It will return  unique element of s1
print(s3)

# Symmetric Difference

s3=s1.symmetric_difference(s2)
print(s3) ## It will take unique element from both the set and create a new set with it and return



## Dictionary Function

'''
1. get()
2. pop()
3. popitem()
4. clear()
5. update()
6. keys()
7. values()
'''

d = {1:1,2:2,(1,2,3):(1,2,3)}  ## it did not throw any error
print(d)
# d.get('2') -> IT IS STRING BUT KEY IS IN FORM OF INT
print(d.get(2))

print(d.get((1,2,3)))
print(d[1,2,3])
print(d[1])


help(dict.pop)

user= {
     'username': 'user123',
     'password': '******',
     'location': 'IN'
}
print(user)

a=user.pop('location') # it is returning a value
print(user)
print(a) 

print(user.pop('username', 'password'))
print(user)

g= user.pop('password')
print(g)

print(user)




##popitem

help(dict.popitem)

user= {
     'username': 'user123',
     'password': '******',
     'location': 'IN'
}

print(user.popitem())
print(user)

user.popitem()
user.popitem() ## pop item in the form of LIFO order
# user.popitem()


# clear

user.clear()
print(user)



# update
user= {
     'username': 'user123',
     'password': '******',
     'location': 'IN'
}

user['password'] = '123'
print(user)

user.update({'password' : '123456'})
print(user)

## Inside a dictionary you should pass one dictionary

# user.update('password','123') throw error

user.update({'password':'******', 'is_logged_in':True})
print(user)


print(user.keys)
print(user.keys())
print(user.values())
print(user.items())








