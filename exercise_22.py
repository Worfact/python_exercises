import sys
import os

def sentence_list():
    word_string = sys.stdin.readlines()
    word_list = word_string[0].split(' ')
    x = 0
    for word in word_list:
        word_list[x] = word.replace('\n', '')
        x += 1
    return(word_list)

def count_words():     
    phrase = sentence_list()
    words = sorted(list(dict.fromkeys(phrase)))
    for word in words:
        print(word, ':', phrase.count(word))

count_words()