class Car:
     wheelers= 4
     engine = 'Petrol'
     base_speed= '40kmph'
     max_speed='120kmph'
     gears=4


mahindra =Car()
suzuki= Car()
toyota= Car()

# TATA, mahindra, suzuki, toyota are objects
## For accessing the properties , we will have to follow the below syntax😊:
# print(TATA) # return Hexadecimal address

TATA = Car()
## By following the below approach , we can also add some new properties inside an object:
TATA.air_bags= True
TATA.security = 'Level 5'
print("Tata Properties")
print(f'No of Wheelers: {TATA.wheelers}')
print(f'Engine Type: {TATA.engine}')
print(f'Base Speed: {TATA.base_speed}')
print(f'Max Speed: {TATA.max_speed}')
print(f'Manual: {TATA.wheelers}')
print(f'Air Bags: {TATA.air_bags}')
print(f'Security: {TATA.security}')

print()
print("mahindra Properties")
print(f'No of Wheelers: {mahindra.wheelers}')
print(f'Engine Type: {mahindra.engine}')
print(f'Base Speed: {mahindra.base_speed}')
print(f'Max Speed: {mahindra.max_speed}')
print(f'Manual: {mahindra.wheelers}')

print()

print("suzuki Properties")
print(f'No of Wheelers: {suzuki.wheelers}')
print(f'Engine Type: {suzuki.engine}')
print(f'Base Speed: {suzuki.base_speed}')
print(f'Max Speed: {suzuki.max_speed}')
print(f'Manual: {suzuki.wheelers}')

print()
print("toyota Properties")
print(f'No of Wheelers: {toyota.wheelers}')
print(f'Engine Type: {toyota.engine}')
print(f'Base Speed: {toyota.base_speed}')
print(f'Max Speed: {toyota.max_speed}')
print(f'Manual: {toyota.wheelers}')


