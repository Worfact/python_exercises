import sys

result_list = []

for i in sys.argv[1].split(','): 
    if (int(i ,2) % 5 == 0 ): 
       result_list.append(i)

print(', '.join(result_list))