# WAP to check whether the given data is SVDT or not

def SVDTChk():
   data=eval(input("Enter the data:"))
   if type(data) in [int,float,complex,bool]:
       print("data is SVDT")
   else:
       print("data is not SVDT")
SVDTChk()
