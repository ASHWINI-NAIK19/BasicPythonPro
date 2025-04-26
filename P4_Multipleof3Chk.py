# WAP to print the square of the number only if it is multiple of 3

def multipleChk():
   n=int(input("Enter the number:"))
   if n%3==0:
       print("square of the number:",n**2)
   else:
       print("number is not multiple of 3")
multipleChk()
