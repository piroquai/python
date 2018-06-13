random_list = [5, 0, 10, 6, 1, 0, 3, -7, 4, 2]
print(random_list)


def func1(list):
    for x in range(len(random_list)):
        if random_list[x] == 0:
            last_zero_pos = x
    num = 0
    summa = 0
    for x in range(last_zero_pos, len(random_list)):
        if random_list[x] > 0:
            summa += random_list[x]
            num += 1
    mean = summa / num
    return mean


print(func1(random_list))
