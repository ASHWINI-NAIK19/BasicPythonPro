 # WAP to check the given data is float or not

def floatChk():
   data=eval(input("Enter the number:"))
   if type(data)==float:
       print("number is float number")
   else:
       print("number is not float number")
floatChk()
