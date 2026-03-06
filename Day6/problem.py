## Create a function which will return a list if prime numbers Please make sure that user can pass b of inputs. For checking whether a number is prime of not, you can create one function

def isPrime(num):
     if num<2:
          return False
     for i in range (2,num-1):  
        if num%i==0:
          return False
     return True
     


def find_prime_nums(*args):
     prime=[]
     for i in args:
          if type(i) is int:
               if isPrime(i) == True:
                    prime.append(i)
     return prime

     

print(find_prime_nums(*eval(input())))



































#  if (n < 2) return 0;
#     for (int i = 2; i <= sqrt(n); i++) {
#         if (n % i == 0) return 0;
#     }
#     return 1;
