import sys

number_list = sys.argv[1].split(',')
result_list = []

for x in number_list:
    if (int(x) % 2) != 0:
        result_list.append(x)

print(','.join(result_list))