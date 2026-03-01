# Loan Approval System

'''
Problem :
Loan approavl if:
Salary>25000
CIBIL score >700
if salary >50000 & CIBIL > 750 -> Instant approval

Otherwise -> Rejected
'''

sal=int(input())
cs=int(input())

if sal>25000 and cs>700 :
     print("Loan Approve")
     if sal>50000 and cs>750:
          print("Instant Approval")
     else:
          print("Loan will be approved after background verification")
else:
     print("NOt Eligible")