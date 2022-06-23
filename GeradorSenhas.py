import random

# Receives the characters
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '@#!$&*/\?.'

# Concatenates the characters
concat = lower_case + upper_case + number + symbols
length_pass = int(input('What is the desired password length: '))

# By randomly concatenated characters and the password length, the password is generated
password = "".join(random.sample(concat, length_pass))

# Password presentation
print(f'Your Passsword is: {password}')

# By GustavoWustemberg