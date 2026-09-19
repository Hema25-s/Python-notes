#              DICT
'''

Collections of keys and value pairs, used to control and store
data in unstructuced way.

It doesn't allows duplicate keys, Doesn't have index, key will act
as a index, through that we can access the value

Ordered Data structure

It is used to handel json based data.

SYNTAX:

{
"key":"value",
"key2:"value2,
}


EX:

user_details = {
    'name':'A',
    'age':123,
    'salary':23422,
    'name':'B'
}

print(user_details)

OUTPUT:
{'name': 'B', 'age': 123, 'salary': 23422}


                     DICT COMPHREHENSION

keys = [1,2,3,4,]
values=[324,345,546,56]

data = {i:j for i in keys for j in values}
print(data)

OUTPUT:
{1: 56, 2: 56, 3: 56, 4: 56}


                    DICT OPERATIONS



user_details = {
    'name':'A',
    'age':123,
    'salary':23422,
    'name':'B',
    'address':{
        'city':'A',
        'pincode':34234,
        'state':'ABC'
    },
    'skills': ['a','b']
}


# print(user_details['age'])
# skills = user_details['skills']


# skills[-1] = 90
# print(skills)


user_details['skills'][-1] = 90
user_details['salary'] = 5645

print(user_details)




             METHODS or BUILT IN FUNCTION
'''

# user_details = {
#     'name':'A',
#     'age':123,
#     'salary':23422,
#     'name':'B',
#     'address':{
#         'city':'A',
#         'pincode':34234,
#         'state':'ABC'
#     },
#     'skills': ['a','b']
# }


# user_details.pop('name')


# print(user_details.values())
# print(user_details.keys())
# print(user_details.items()) # returns key value as list of tuple to iterate each value

# for i,j in user_details.items():
#     print("ITEMS:",i,j)


# name = user_details.get('A',0)
# print(name)

# user_details.update({
#     'name':'c',
#     'salary':1324,
#     'phone_no':234345
# })

# print(user_details)

# empty_dict = user_details.fromkeys([1,2,3,4],'')
# print(empty_dict)

# user_details.setdefault('name1',0)

# print(user_details['name1'])


user_details = {
    'name':'A',
    'age':123,
    'salary':23422
}

print(user_details.pop())


