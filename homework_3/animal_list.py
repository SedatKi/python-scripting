print()

animal_list = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'hippopotamus', 'monkey',\
'crocodile', 'bear', 'panda', 'penguin', 'kangaroo', 'lion', 'gazelle', 'parrot', 'toucan',\
'giraffe', 'elephant', 'kangaroo', 'monkey']
print('animal list: ', animal_list)

print()

output_dict = {}
for i in animal_list:
    if i in output_dict:
        output_dict[i] += 1
    else:
        output_dict[i] = 1
print('output_dict', output_dict)

print()
# lion = len([i for i in animal_list if i == 'lion'])
# tiger = len([i for i in animal_list if i == 'tiger'])