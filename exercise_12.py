result_list = []

for i in range(999, 3001, 1):
    if ( i % 2 ) == 0:
        result_list.append(i)

print(', '.join(map(str, result_list)))