#                   TUPLE
'''
Used to store data that are unchangable(immutable)
Order data structure
it has index to make slice
It can be created from () delimiter or tuple() built in function


EX:
names = ('A','B','C','D')
print(names[-1])

names[-1]=0

EX2:

age = tuple([1,2,3,44,3])
print(age)

EX3:

a= tuple(i for i in range(1,10))
print(a)

METHODS:
1.count
2.index

'''





#          SET
'''
Unorder data structure, elements inside the set will be changed by time
Doesn't have index
Doesn't allows duplicate values
It can be created from {} demlitier and set() built in function

EX:
a = {'A','A','B',1,3245,34,5,234}
print(a)

OUTPUT:
{1, 34, 234, 5, 'B', 'A', 3245}


EX2:
a = {'A','A','B',1,3245,34,5,234}
print(a[0])

OUTPUT:
Error


EX3:
a= {i for i in range(1,10)}
print(a)

EX4:

def remove_duplicate(a):
    result = set(a)
    result = list(result)
    
    
    check type of a

    if type of a list: convert it as a list
    
    
    return result

a= [234,234,234,456,67,567,76]

print(remove_duplicate(a))


                    TASK 2

a= [234,234,234,456,67,567,76]

#  Count



                           SET OPERATIONS



a={12,23,4,4,5}
b={234,34,5,345,4}

print(a+b) Error



                           SET METHODS (BUILT-IN FUNCTIONS)


a={1,2,3,4,5,6}
b = {1,2,3}

#a.add(223)

#c= a.union(b)
#c= a.intersection(b)

#c= a.difference(b)

#c= a.symmetric_difference(b)  # gives both set remaining values

#a.intersection_update(b)

#a.difference_update(b)

#a.symmetric_difference_update(b)

#a.remove(20) # removes item from set if exists otherwise error

#a.discard(20) # removes if the specified element is exists, otherwise it doesn nothing

# a={1,2,3,4,5,6}
# b = {1,2,3}
# c = a.issuperset(b)

a={1,2,3,4,5,6,'hi'}
# b = {1,2,3}
# c = a.issubset(b)
# d = b.issubset(a)

#a.update({7,8})

# a.pop()  # deletes first value
# a.pop()

#print(a)


'''

