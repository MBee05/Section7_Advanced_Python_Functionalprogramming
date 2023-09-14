#Filter we can receive less than we gave it
#with map we always have the same result, we gave 3 items, it gives back 3 items.


'''def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))'''


my_list = [1,2,3]
def only_odd(item):
    return item % 2 != 0  #if it equal 0 then its even otherwise odd

print(list(filter(only_odd, my_list)))
print(my_list)
