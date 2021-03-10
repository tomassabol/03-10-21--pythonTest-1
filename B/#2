first_l = []
second_l = []
count = 1
count2 = 1
count_l = 0
with open('cisla.txt', 'r') as path_file:
    with open('riesenie.txt', 'w') as dest_file:
        for line in path_file:
            if count_l == 0:
                for num in line:
                    if count <= 20:
                        first_l.append(num)
                        count += 1
                count_l += 1
            if count_l == 1:
                for num2 in line:
                    if count2 <= 20:
                        second_l.append(num2)
                        count2 += 1
        first_l.reverse(), second_l.sort()
        for k in first_l:
            dest_file.write(k)
        dest_file.write("\n")
        for j in second_l:
            dest_file.write(j)
