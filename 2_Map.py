#map, filter, zip, reduce



#map


'''def multiplyj_by2(li):
    new_list= []
    for item in li:
        new_list.append(item*2)
    return(new_list)

print(map(multiplyj_by2, [1,2,3]))


#output: <map object at 0x00000271EF236B60> it gives the object that map has created in this location. so, to view it we have to turn it into a list.

print(list(map(multiplyj_by2, [1,2,3])))'''

#output: error, bcz with map we dont need new_list and append with map is that you give some data, and data act upon 'multiplyj_by2' (action), so you only need a ffunction that return this '(item*2)' so we only need to do


def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, [1,2,3])))



#**********************#
my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))
print(my_list) #output:[1, 2, 3] it doesn't changed




