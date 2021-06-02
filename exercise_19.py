import sys
import re

info_list = sys.stdin.readlines()

def tuple_creator(info_list):
    x = 0
    for hooman in info_list:
        info_list[x] = hooman.replace('\n', '')
        x += 1
    info_tuple = [tuple(hooman.split(',')) for hooman in info_list]
    info_tuple.sort()
    print(info_tuple)

tuple_creator(info_list)