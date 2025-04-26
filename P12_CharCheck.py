# WAP to check whether the character is uppercase or lowercase or digits or special character

def charChk():
   ch=input("Enter the character:")
   if 'A'<=ch<='Z':
       print("character is Uppercase")
   elif 'a'<=ch<='z':
       print("character is lowercase")
   elif '0'<=ch<='9':
       print("character is digits")
   else:
       print("character is special character")
charChk()
