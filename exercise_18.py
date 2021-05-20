import sys

password_list = input().split(',')

def length_test(x):
    if len(x) > 5 and len(x) < 13:
        return(True)
    else:
        return(False)

def uppercase_test(x):
    for l in x:
        if l.isupper():
            return(True)
            break

def lowercase_test(x):
    for l in x:
        if l.islower():
            return(True)
            break

def number_test(x):
    for i in x:
        if i.isnumeric():
            return(True)
            break

def special_test(x):
    for f in x:
        if x == '$' or '#'or '@':
            return(True)
            break

def password_test(password_list):
    for x in password_list:
        if length_test(x) != True:
            continue
        if uppercase_test(x) != True:
            continue
        if lowercase_test(x) != True:
            continue
        if number_test(x) != True:
            continue
        if special_test(x) != True:
            continue
        print(x)


password_test(password_list)