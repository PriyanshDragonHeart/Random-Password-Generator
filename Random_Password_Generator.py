#code by Priyansh (DragonHeart)
#import random module
import random
#initialize a list
option=[]
#declare char
upper='A'
lower='a'
#using brute force to enter char into list
for i in range (0,26):
    option.append(upper)
    upper=chr(ord(upper)+1)
for j in range(0,26):
    option.append(lower)
    lower=chr(ord(lower)+1)
#enter int into list
num=['0','1','2','3','4','5','6','7','8','9']
option+=num
#enter special characters to list
special_char=['!','@','#','$','%','&']
option+=special_char
#ask for length of password
print("Password Length:")
password_length=int(input())
#select random characters and join them
random_char=[random.choice(option) for i in range(password_length)]
random_password="".join(random_char)
#print password
print (random_password)