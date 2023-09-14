# is these pure function? 

def multiplyj_by2(li):
    new_list= []
    for item in li:
        new_list.append(item*2)
    return(new_list)
print(multiplyj_by2([1,2,3])) 



# 1.is this going to give you the same output, no matter how many time you run the code? yes
# 2.is it going to produce a side affect? no





def multiplyj_by2(li):
    new_list= []
    for item in li:
        new_list.append(item*2)
    return print(new_list)
(multiplyj_by2([1,2,3])) 


# 1.is this going to give you the same output, no matter how many time you run the code? yes
# 2.is it going to produce a side affect? yes, bcz print is inside 





new_list= [] 
def multiplyj_by2(li):
   for item in li:
        new_list.append(item*2)
        return(new_list)
    
print(multiplyj_by2([1,2,3])) 


#2.is it going to produce a side affect? yes, bcz it interact outside the scope