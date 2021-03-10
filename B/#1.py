import random


def Heslo():
    list_a = ['2','4','6','8','0']
    list_b = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    list_c = ['1','3','5','7','9']
    with open('password.txt', 'w') as dest_file:
        for k in range(20):
            password = []
            for i in range(5):
                password.append(random.choice(list_a))
                password.append(random.choice(list_b))
                password.append(random.choice(list_c))
            dest_file.write(str(password))
            dest_file.write("\n")
