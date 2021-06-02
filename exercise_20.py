import sys

def number_generator():
    for i in range(int(sys.argv[1])):
        if (i % 7) == 0:
            yield i

for i in number_generator():
    print(i)