import random
import string

userdatails = {}

first_name = input("Enter first name ")
last_name = input("Enter last name ")
email = input("Enter email ")

letters = string.ascii_lowercase
password = first_name[:2] + last_name[-2:] + ''.join(random.choice(letters) for i in range(5))

response = input(f'Here is your password: "{password}" are you okay with it? Yes or No: ')

if response == "no":
    new_password = input("please enter your prefered password: " )
    while len(new_password) <= 7: 
        new_password = input("input a new password equal to or greater than 7 in length: ")
    
    userdatails["first_name"] = first_name
    userdatails["last_name"] = last_name
    userdatails["email"] = email

    print(userdatails)
else:
    userdatails["first_name"] = first_name
    userdatails["last_name"] = last_name
    userdatails["email"] = email

    print(userdatails)
