#Lambda Expressions are really useful when using them for function that a. you only use once, b. and it is anonymous function, just used it once and done with it, throw it away

from functools import reduce

#lambda param: action(param)

my_list = [1,2,3]

#def multiply_by2(item):
    #return item*2-----> we can delete this function and just using lambda by print out as below
print(list(map(lambda item: item*2, my_list)))


#output:[2, 4, 6]
#Lambda Expressions are one time anonymous function, no name attached with, you dont need to run more than once.Once the interpreter runs that code then it forgets about it.





#def only_odd(item): 
    #return item % 2 != 0 -----> we can delete this function and just using lambda by print out as below

print(list(filter(lambda item: item % 2 != 0, my_list)))






#def accumulator(acc, item):
    #print(acc, item)
    #return acc + item -----> we can delete this function and just using lambda by print out as below


print(reduce(lambda acc, item: acc + item, my_list))

