import random

list_a = ['A', 'E', 'I', 'O', 'U']
list_b = ['B', 'M', 'P', 'R', 'S', 'V', 'Z']

with open('password.txt', 'w') as dest_file:
    password = []
    for i in range(6):
        password.append(random.choice(list_b))
        password.append(random.choice(list_a))


print("".join(password)) 


