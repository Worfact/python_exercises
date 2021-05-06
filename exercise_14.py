sentence = input("Quelle est la phrase ? ")
lower_case = upper_case = 0
for i in sentence:
    if i.islower():
        lower_case += 1
    elif i.isupper():
        upper_case += 1

print("Lower case = ", lower_case, "\nUpper case = ", upper_case)