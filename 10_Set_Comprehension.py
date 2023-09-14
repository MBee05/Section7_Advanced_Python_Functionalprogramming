#set comprehension- set only allow numbers that not duplicated

my_list = []

for char in 'hello':
    my_list.append(char)
print(my_list)



my_list1 = {char1 for char1 in 'morning'}
print(my_list1)



my_list2 ={num for num in range(0, 100)}
print(my_list2)


my_list3 ={num*2 for num in range(0, 100)}
print(my_list3)



my_list4 ={num**2 for num in range(0, 100) if num % 2 ==0}
print(my_list4)