some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

duplicates =[]
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)            
print(duplicates)


duplicates1=[]
duplicates1 =[value for value in some_list if some_list.count(value) > 1]

#my_list4 =[num**2 for num in range(0, 100) if num % 2 ==0]
print(duplicates1)



duplicates2 =set ([value for value in some_list if some_list.count(value) > 1])

print(duplicates2)


duplicates3 =list(set ([value for value in some_list if some_list.count(value) > 1]))

print(duplicates3)