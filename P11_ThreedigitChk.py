 # WAP to check whether the given integer is 3 digit number or not

def threedigitChk():
   n=int(input("Enter the number:"))
   if 100<=n<=999:
       print("number is 3 digit number")
   else:
       print("number is not 3 digit number")
threedigitChk()
