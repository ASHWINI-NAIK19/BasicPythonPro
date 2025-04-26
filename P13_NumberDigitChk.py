# WAP to check whether the number is single digit or  two digit
#or three digit or more than 3 digit

def digitChk():
   d=int(input("Enter the number:"))
   if 1<=d<=9:
       print("single digit number")
   elif 10<=d<=99:
       print("two digit number")
   elif 100<=d<=999:
       print("three digit number")
   else:
       print("More than three digit number")
digitChk()
