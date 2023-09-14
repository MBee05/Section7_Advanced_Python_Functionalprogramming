my_list = []

simple_dict = {
    'a': 1,
    'b': 2
}
#my_dict = {key:value**2 for key, value in simple_dict.items() }
my_dict = {k:v**2 for k, v in simple_dict.items() if v % 2 == 0}

print(my_dict)


my_dict1 = {num:num * 2 for num in [1,2,3]}

print(my_dict1)