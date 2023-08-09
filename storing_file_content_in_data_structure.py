# A program that store file content in data structure
from random import choice


def petname():
    with open('file1.txt', 'r') as file:
        f_content = file.read()
        f_content_list = f_content.split('\n')
        print(choice(f_content_list))
petname()   

#   Alternative way of opening and reading file
'''
file = open('file1.txt', 'r')
f_content = file.read()
print(f_content)
'''

