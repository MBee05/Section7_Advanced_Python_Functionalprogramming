#Zip iterate over each data and zip them together without any modification intead create a new whole

my_list = [1,2,3]
your_list=[ 10,20,30]
their_list=[ 12,23,38]
print(list(zip(my_list, your_list)))

print(list(zip(my_list, your_list, their_list)))