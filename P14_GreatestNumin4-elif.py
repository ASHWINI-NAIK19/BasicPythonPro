# WAP to find the greatest among four numbers

def greatestNum():
   a=int(input("Enter the number:"))
   b=int(input("Enter the number:"))
   c=int(input("Enter the number:"))
   d=int(input("Enter the number:"))
   if a>b and a>c and a>d:
       print("a is greatest")
   elif b>a and b>c and b>d:
       print("b is greatest")
   elif c>a and c>b and c>d:
       print("c is greatest")
   else:
       print("d is greatest")
greatestNum()
