import string
import secrets

# generate random character length password 
# includes upper and lower case letters, numbers, and symbols

# you can add or remove symbols in the list depending on the site account password creation requirements 
symbols = ['!','@','#','%','$','&','~','+','-','/','*']

password = ""

for _ in range (4): # default loop 4 for 16 character length, but you can modify it to increase or decrease password length 
    password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(symbols)
    
print("password:", password)

print("length:", len(password))
