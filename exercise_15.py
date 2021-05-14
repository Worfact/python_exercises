import sys

value = sys.argv[1]
result = 0

for i in range(1, 5):
    result += int(i * value)

print(result)