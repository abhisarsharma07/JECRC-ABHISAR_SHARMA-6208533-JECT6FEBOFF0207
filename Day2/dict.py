# >>> ##{k1: v1 , k2:v2, ........., kn:vn}
# >>> ## It is a type of collection
# >>> ## In which we can store the data in the form of key- Value pairs
# >>> ## Which will be enclosed between braces
# >>> ## Where key - value pairs will be separated by comma & key, value will be separatesd by collon
# >>> user_info = {
# ... 'userid' : 876545687,
# ... 'password':'******',
# ... 'location
#   File "<stdin>", line 4
#     'location
#     ^
# SyntaxError: unterminated string literal (detected at line 4)
# >>> user_info = {
# ... 'userid' : 876545687,
# ... 'password':'******',
# ... 'location' :'IN'
# ... }
# >>> user_info
# {'userid': 876545687, 'password': '******', 'location': 'IN'}
# >>> type(user_info)
# <class 'dict'>
# >>> ## I want to access values for a particular key.
# >>> ## var_name/ value
# >>> user_info
# {'userid': 876545687, 'password': '******', 'location': 'IN'}
# >>> user_info['userid']
# 876545687
# >>> user_info.password
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'dict' object has no attribute 'password'
# >>> user_info.'password'
#   File "<stdin>", line 1
#     user_info.'password'
#               ^^^^^^^^^^
# SyntaxError: invalid syntax
# >>> user_info.['password']
#   File "<stdin>", line 1
#     user_info.['password']
#               ^
# SyntaxError: invalid syntax
# >>> user_info['password']
# '******'
# >>> user_info['location']
# 'IN'
# >>>
# >>> user_info[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 0
# >>> user_info
# {'userid': 876545687, 'password': '******', 'location': 'IN'}
# >>> ## new Key value pair
# >>> ##is_logged_in = True
# >>> ##user_info[key_name]
# >>> ##user_info[key_name] = value
# >>> user_info['is_logged-in']=True
# >>> user_info
# {'userid': 876545687, 'password': '******', 'location': 'IN', 'is_logged-in': True}
# >>> ## Logged Out
# >>> ## update the value
# >>> user_info['is_logged_in']= False
# >>> user_info
# {'userid': 876545687, 'password': '******', 'location': 'IN', 'is_logged-in': True, 'is_logged_in': False}
# >>> user_info['is_logged-in']= False
# >>> user_info
# {'userid': 876545687, 'password': '******', 'location': 'IN', 'is_logged-in': False, 'is_logged_in': False}
# >>> ## It is overriding the value
# >>> ## If key is not present it will simply add it
# >>> ## If key is present , it will override the prev value
# >>>