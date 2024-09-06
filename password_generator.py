import string
import secrets

# 16 characters 
# numbers, upper case and lower case letters, and symbols.


symbols = ['!','@','#','%','$','&','~','+','-','/','*']
#other_symbols = ['`','^','(',')','{','}','<','>','|',':',';','[',']']

password = ""

for _ in range (4):
    password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(symbols)
    
print(password)
