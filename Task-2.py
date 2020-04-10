import random
import string

first_name = input("Enter first name ")
last_name = input("Enter last name ")
email = input("Enter email ")

letters = string.ascii_lowercase
password = first_name[:2] + last_name[-2:] + ''.join(random.choice(letters) for i in range(5))

response = input(f'Here is your password: "{password}" are you okay with it? Yes or No: ').lower()

userdatails = []

if response == "no":
    new_password = input("please enter your prefered password: " )
    while len(new_password) <= 7: 
        new_password = input("input a new password equal to or greater than 7 in length: ")
  

    newuserdetails = {"first_name": first_name, "last_name": last_name, "email": email}
    userdatails.append(newuserdetails)
    print(userdatails)
elif response == "yes":
   
    newuserdetails = {"first_name": first_name, "last_name": last_name, "email": email}
    userdatails.append(newuserdetails)
    print(userdatails)

else:
    print("You inputed a wrong option")