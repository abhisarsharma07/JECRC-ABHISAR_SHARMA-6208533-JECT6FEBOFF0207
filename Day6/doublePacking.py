# def func_name(**kwargs):
     # Statement
     # Block

# func_name(k1=v1, k2=v2, ...., kn=vn)
# All the key names should a string but you cant use quotes

def print_details(**kwargs):
     print(kwargs)

print_details(username='user123', password='****', logged_in_devices=['Android', 'Windows', 'Linux'])

