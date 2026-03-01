#WAP to check whether a year is leap year or not

year= int(input())

if year%400==0 or (year%4==0 and year%100!=0) :
     print("Yes it is a leap year")
else:
     print("Not a leap Year")