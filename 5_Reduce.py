#Reduce doeasn't come in the python built-function in order to use reduce we have to do 

from functools import reduce

my_list = [1,2,3]
def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 0))


#0 1 --> acc = 0 , item = 1
#return --> 0 + 1 = 1 so next will be 1 
#1 2 -->    1 + 2 = 3 so next will be 3
#3 3 -->    3 + 3 = 6
#6   -->    6


print(reduce(accumulator, my_list, 10))
'''output
10 1
11 2
13 3
16'''