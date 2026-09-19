#               LIST
'''
It is a collection and similar and unsimilar data types

Can be created using [] delimiter

Or it can be created using list() built in function, and also this
function converts any data structure into list.

Order of the values doesn't change

It have index that helps to access particular or set of elements

Mutable(changable) data type, elements inside this data structure can
be changed any time.

EX:

names = ['A','B','C']
age= list((1,2,3,4))

result = names+age 

print(names, age, result)


                 MULTIPLY OPERATION

names = ['A','B','C']

result = names*2

print(result)



EX2:

names = ['A','B','C']
age= list((1,2,3,4,5,6,6,7,7,75,4,3,4,3,2,2))

print(names[1])
print(age[-2])
print(age[1:])
print(age[:8])
print(age[::2])
print(age[-1:-4:-1])
print(age[::-1])
'''


#     LIST METHODS OR BUILT IN FUNCTION
'''

All the list built in function on the list can be accessed by dot

list_vairable_name.list_built_in_function()


a=[24,45,3,45,5,6,456,456,'A','B']

#a.append('hi') # adds this item on last of the list, modifies the original list
#a.append([234,235,34,5])
#a.extend([234,45,34,5]) # adds multiple elements

#deleted_item = a.pop() # deletes the last item in the list, and it returns the deleted item
#print(a, deleted_item)

# a.pop(2)
# print(a)

#a.remove(456)  # it deletes the specified values, and it delets the first occurence, returns delete element 

# index_of_456 = a.index(456)  # returns the specified element's index

# print(index_of_456)

# count_of_value = a.count(456)
# print(count_of_value)

# a.insert(2,'hello')
# print(a)


#a.sort()
#a.sort(reverse=True)
#a.reverse()

# b=a.copy()
# a.clear()

# print(a)
'''

#     LIST COMPHREHENSION
'''

SYNTAX:

var = [variable_name for variable_name in range()]


EX:
a=[i for i in range(0,10,2)]
print(a)

SYNATX 2:
var = [var for var in range() if condition_var]

EX:
a=[i for i in range(100) if i%2==0]

print(a)


Ex3:

b=12

a= True if b>10 else False

print(a)
'''


def day_name(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

print(day_name(3))



b=12

a= True if b>10 else False

print(a)