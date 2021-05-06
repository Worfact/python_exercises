sentence = input("Quelle est la phrase ? ")
number = letter = 0
for i in sentence:
    if i.isalpha():
        letter += 1
    elif i.isnumeric():
        number += 1

print("letter = ", letter, "\nnumber = ", number)