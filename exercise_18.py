import sys

password_list = input().split(',')

def test_launcher(x):
    test_list = (length_test, uppercase_test, lowercase_test, number_test, special_test)
    for test in test_list:
            if test(x) != True:
                return(False)

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
    result_list = []
    for x in password_list:
        if test_launcher(x) != False:
            result_list.append(x)
    print(', '.join(result_list))


password_test(password_list)