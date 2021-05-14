import sys
import re

transaction_list = sys.stdin.readlines()
account_level = 0

for x in transaction_list:
    transaction_level = ''.join(re.findall(r'\d+', x))
    if 'D' in x:
        account_level -= int(transaction_level)
    if 'W' in x:
        account_level += int(transaction_level)

print(account_level)
