# list, set, dictionary comprehension 
#comprehensions are quick way to create list, set and dico instead of looping...this a short way of doing it


#Example

my_list = []

for char in 'hello':
    my_list.append(char)
print(my_list)



#how to do it by using list comprehension

#my_list1 = [param for param in iterable]


my_list1 = [char1 for char1 in 'morning']
print(my_list1)



my_list2 =[num for num in range(0, 100)]
print(my_list2)


my_list3 =[num*2 for num in range(0, 100)]
print(my_list3)



my_list4 =[num**2 for num in range(0, 100) if num % 2 ==0]
print(my_list4)