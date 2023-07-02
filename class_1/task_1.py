def reverse_slicing(s):
     return s[::-1]

str1 = 'Hello world, some random thing'

reversed_str1 = reverse_slicing(str1)

reverse_hello_only = reverse_slicing(str1[:5])