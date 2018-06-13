random_list = [5, 1.3, 10, 6, 1.1, 2.3, 3.5, 7, 4, 0.2]
print(random_list)
max_pos = random_list.index(max(random_list))
min_pos = random_list.index(min(random_list))
start_pos = min(min_pos, max_pos)
end_pos = max(min_pos, max_pos)
summa = 0
for x in range(start_pos + 1, end_pos):
    if random_list[x] % 1 == 0:
        summa += random_list[x]
print(summa)
