class Car:
     ## Below variables are known as "Properties/ States/ Members"
     wheelers=4
     engine='Petrol'
     base_speed='40kmph'
     max_speed='120km'
     gears=4

     def __init__(self,air_bags, security, base_budget, varient, total_sale):
          self.air_bags=air_bags
          self.security=security
          self.base_budget=base_budget
          self.varient=varient
          self.total_sale=total_sale

     def display_properties(self):
          print({
               'wheelers' : self.wheelers,
               'engine' :self.engine,
               'base_speed' :self.base_speed,
               'max_speed' :self.max_speed,
               'gears' :self.gears,
               'security':self.security,
               'base_budget':self.base_budget,
               'varient':self.varient,
               'air_bags':self.air_bags,
               'total_sale':self.total_sale,        
          })
     def update_base_speed(self,new_speed):
          self.base_speed = new_speed
          print(f'New base Speed :{self.base_speed}')  

     def update_max_speed(self,new_speed):
          self.max_speed = new_speed
          print(f'New Max Speed : {self.max_speed}')
     
     @classmethod
     def update_gears(cls,new_gears):
          cls.gears = new_gears
          print(f'No of gears :{cls.gears}')




TATA=Car(True,'Level 5', '2L', 12, 100000)
TATA.display_properties()
TATA.update_base_speed('700kmph')
TATA.update_max_speed(60)
TATA.update_gears(10)
mahindra=Car(True,'Level 4', '3L', 20, 100000)

# TATA= Car()
# TATA.engine = ['Petrol', 'Diesel', 'EV']
# TATA.air_bags= True
# TATA.no_of_air_bags=4
# TATA.base_budget='2L'
# TATA.no_of_varient= 12

# ## constructer (__init__)
# def __init__(self,air_bags):
#      self.air_bags = air_bags


# def __init__(rahul,air_bags):
#      rahul.air_bags = air_bags  // it is also correct

'''
class ClassName:
     properties

     
     def __init__(self, arg1, arg2, arg3, ...., argn):
     self.arg1=arg1
     self.arg2=arg2
     self.arg3=arg3
     self.arg4=arg4
     ...
     self.argn=argn
     //self object ke upar point karta hai. self addrees hold karega object ka



'''

