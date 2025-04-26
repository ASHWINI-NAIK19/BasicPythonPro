# WAP to check whether the string is palindrome or not using slicing

def palinChk():
   s=input("Enter the string:")
   if s==s[::-1]:
       print("String is Palindrome")
   else:
       print("String is not Palindrome")
palinChk()
