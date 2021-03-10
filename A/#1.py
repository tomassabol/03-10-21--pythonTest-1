import random

list_a = ['A', 'E', 'I', 'O', 'U']
list_b = ['B', 'M', 'P', 'R', 'S', 'V', 'Z']

with open('password.txt', 'w') as dest_file:
    for k in range(5):
        password = []
        for i in range(6):
            password.append(random.choice(list_b))
            password.append(random.choice(list_a))
        
        dest_file.write(str("".join(password)))
        dest_file.write("\n")
