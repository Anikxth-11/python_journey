print('WELCOME TO PyPASSWORD GENERATOR!!')
p_letters=int(input('how many letters would you like to have in your password?\n'))     
p_symbols=int(input('how many symbols would you like to have in your password?\n'))
p_numbers=int(input('how many numbers would you like to have in your password?\n'))
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []
for char in range(1,p_letters+1):
    random_char= random.choice(letters)
    password+=random_char
for char in range(1,p_numbers+1):
    random_num=random.choice(numbers)
    password+=random_num
for char in range(1,p_symbols+1):
    password+=random.choice(symbols)
random.shuffle(password)
delimiter=''
passcode=delimiter.join(password)





print(f'your password is: {passcode}')
