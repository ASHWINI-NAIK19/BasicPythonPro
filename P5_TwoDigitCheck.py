# WAP to check whether the number is 2 digit number

def twodigitChk():
   n=int(input("Enter the number:"))
   if n>=10 and n<=99:
       print("number is 2 digit number")
   else:
       print("number is not 2 digit number")
twodigitChk()
