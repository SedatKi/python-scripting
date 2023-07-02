# string1 = 'Hello World'

# multiline_string = '''this
# is
# a
# multiline
# string'''

# print(multiline_string)

# ---------------------------------

# input() is similar to read -s in bash
    # input function will always output string

# inp = input('Please provide your name: ')
# print('Hello', inp)

# num1 = int(input('Please provide your first number: '))
# num2 = int(input('Please provide your second number: '))

# ans = (num1 + num2)
# print(ans)
#------------------------------------------------
# String Slicing

# str1 = 'Hello world, some random thing'

# print(str1[:11])

def reverse_slicing(s):
     return s[::-1]

str1 = 'Hello world, some random thing'

print(reverse_slicing(str1))

reverse_hello_only = input(reverse_slicing(str1[:5])) 

print(reverse_hello_only[::-1])

#----------------------------------

# name = input('Please provide your name: ')
# age = input('Please provide your age')
# print('My name is', name, 'My age is', age, sep='||', end='. Welcome!')
# print(' lastname')

# My name is||name||My age is||age. Welcome! lastname
