import sys

def body(innit_space, innit_leaf, high):
    space = innit_space
    leaf = innit_leaf
    for i in range(1,high,1):
        print(space * ' ', '\33[32m' + leaf * '*')
        space = space - 1
        leaf = leaf + 2

def trunk(size, trunk_space):
    width = size
    if (size % 2) != 0:
        size = size - 1
    trunk_space = int(trunk_space - (size / 2))
    for i in range(0, width, 1):
        print(trunk_space * ' ', '\33[33m' + (size + 1) * '|')
     
def tree():
    size = int(sys.argv[1])
    innit_space = 3 * size
    innit_leaf = 1
    high = 5
    trunk_space = innit_space
    for i in range(1, size + 1, 1):
        body(innit_space, innit_leaf, high)
        innit_space = innit_space - 2
        innit_leaf = innit_leaf + 4
        high = high + 1
    trunk(size, trunk_space)

tree()