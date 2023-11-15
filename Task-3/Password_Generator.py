import random
import string
s=int(input("Enter the size of password: "))
chrLst = ""
 
print("1. Alphabets\n2. Digits\n3. Special Characters\n4. Exit")
while(True):
    ch = int(input("Choose a option: "))
    if(ch == 1):
        chrLst += string.ascii_letters
    elif(ch == 2):
        chrLst += string.digits
    elif(ch == 3):
        chrLst += string.punctuation
    elif(ch == 4):
        break
    else:
        print("Please pick a valid option!")
 
pwd = []
for i in range(s):
    rndmchr = random.choice(chrLst)
    pwd.append(rndmchr)

print("The Random Password is " + "".join(pwd))
