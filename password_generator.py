import string
import secrets

# generate random 16 character password string
# includes mix of numbers, upper and lower case letters, and symbols

# some symbols can be removed if certain sites restricts it
symbols = ['!','@','#','%','$','&','~','+','-','/','*']

password = ""

for _ in range (4):
    password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(symbols)
    
print(password)
