## Take the unit int he form of integer
# Apply all the conditions and calculate the total bill amount.
# Check another condition for applying discount

# unit=int(input())
# bill=0
# if unit>0 :
#      if unit<=100:
#        bill=(5*unit)
#      elif unit<=300 and unit>100:
#        bill=(7*unit)
#      elif unit>300:
#        bill=(10*unit)


# if(bill > 5000):
#      print(bill-bill*0.05)
# else:
#      print(bill)

     

units = int(input())
bill_amt = 0
if units > 0:
  if units <= 100:
    bill_amt = units*5
  elif 101 <= units <= 300: 
    bill_amt = units*7
  else:
    bill_amt = units*10
else:
  print("Enter valid units")

if bill_amt > 5000:
  bill_amt = bill_amt*0.95

#F string ---> String + expression
print(f"Bill amount after discount: {bill_amt}")