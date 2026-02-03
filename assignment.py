import random

password = ""
length = 8

for i in range(length):
    choice == random.randint(1,3)

    if choice == 1:

        password += chr(random.randint(97, 122))

    elif choice == 2:
         password += chr(random.randint(65,90))

    else:
         password += chr(random.randint(48, 57))

    elif choice == 2:
        
         passwoed += chr(random.randint(65, 90))
    
    else:

         password += chr(random.randint(48, 57))
    
password_list = list(password)
random.shuffle(password_list)

final_password = ""
for ch in password_list:
     final password += ch

print("generated password:", final_password)


        


  