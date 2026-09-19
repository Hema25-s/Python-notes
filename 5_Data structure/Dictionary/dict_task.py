# '''
# #task1


# details={ 
# 'name':'arun',
# 'age':21,
# 'course':'python',
# 'mark':85,

# }
# print(details)



#task2

# student = {
#     'name': 'Kumar',
#     'age': 22,
#     'course': 'Python',
#     'mark': 90
# }
# print(student['name'])
# print(student['age'])



# #task3

# student = {
#     'name': 'Kumar',
#     'age': 22,
#     'mark': 90
# }
# student['mark']=95
# print(student)



#task4

# student = {
#     'name': 'Kumar',
#     'age': 22,
#     'course': 'Python'
# }
# student.update({
#     'city':'erode'
# })
# print(student)



# #task5

# details={
#     'name':'A',
#     'age':20,
#     'name':'B',

# }

# print(details)



# #task6

# employee = {
#     'name': 'Ravi',
#     'age': 25,
#     'salary': 30000,
#     'department': 'IT'
# }
# c=employee.keys()
# print(c)



# #task7

# employee = {
#     'name': 'Ravi',
#     'age': 25,
#     'salary': 30000
# }
# c=employee.values()
# print(c)


# #task8

# employee = {
#     'name': 'Ravi',
#     'age': 25,
#     'salary': 30000
# }
# for i in employee:
#     employee.items()
#     print(i,employee[i])


# #task9

# user = {
#     'name': 'Arun',
#     'age': 23
# }
# c=user.get('phone','not available')
# print(c)


# #task10

# user = {
#     'name': 'Arun',
#     'age': 23,
#     'city': 'Erode'
# }
# c=user.pop('age')
# print(user)

# #task11

# user = {
#     'name': 'Arun',
#     'salary': 25000
# }
# user.update({
#     'salary':30000,
#     'phone':9360808933
# })
# print(user)


# #task12

# user = {
#     'name': 'Arun'
# }

# user.setdefault('email','not provided')
# print(user)


# #task13

# user = {
#     'name': 'Arun',
#     'address': {
#         'city': 'Erode',
#         'pincode': 638001,
#         'state': 'Tamil Nadu'
#     }
# } 
# p=user['address']['city']
# c=user['address']['pincode']
# print(p)
# print(c)



# #task14

# user = {
#     'name': 'Arun',
#     'skills': ['HTML', 'CSS', 'Java']
# }

# user['skills'][-1]='python'
# print(user)

# #task15

# keys=[1,2,3,4,5]
# data={i:i**2 for i in keys}
# print(data)

# k=[1,2,3,4,5]
# j={i:i+2 for i in k}
# print(j)


# #task16

# information={
#     101:
#     {
#       'name':'karthi',
#       'age':21,
#       'course':'IT',
#       'marks':85,
#       'skills':['python','java'],
#       'address':'gobi',
#     },
#     102:
#     {
#       'name':'hema',
#       'age':21,
#        'course':'AI',
#             'marks':95,
#             'skills':['java','html'],
#             'address':'erode',
#           }  
#     }
# print(information[101]['name'])
# print(information[102]['address'])
# information[101]['marks']=90
# print(information[101]['marks'])
# information[101]['skills'].append('git')
# print(information[101]['skills'])
# print(information.keys())
# print(information.items())



# #hard task 2

# cart={
#     101:{
#         'name':'mobile',
#         'price':50000,
#         'quantity':1,
#     },
#     102:{
#         'name':'laptop',
#         'price':20000,
#         'quantity':2,

#     }
# }
# print("mobile:",cart[101]['price'])
# print("laptop:",cart[102]['price'])
# s=cart[101]['price']
# u=cart[102]['price']
# def total(price1 ,price2):
#  return price1 + price2
# print("Total:",total(s,u))
# cart[102]['quanity']=3
# print("laptop quanity:",cart[102]['quanity'])
# cart.update({
#  'name':'mouse',
#  'price':3000,
#  'quantity':2,
#  }
# )
# print(cart)
# a=cart.pop(101)
# print(a)
# for i ,item in cart.items():
#  print(i)
# '''



#hard task 3


# employees = {
#      1001: {
#          'name': 'Arun',
#          'department': 'IT',
#         'salary': 40000,
#        'skills': ['Python', 'SQL']
#      },
#      1002: {
#         'name': 'Kumar',
#          'department': 'HR',
#          'salary': 35000,
#          'skills': ['Excel', 'Recruitment']
#    },
#      1003: {
#          'name': 'Ravi',
#         'department': 'IT',
#          'salary': 45000,
#          'skills': ['Python', 'Django']
#      }
#  }

# print("Employees:")
# print(employees[1001]['name'])
# print(employees[1002]['name'])
# print(employees[1003]['name'])

# print("Highest salary:")
# employees[1001]['salary']=45000     
# print("Ravi:",employees[1001]['salary'])
# print("Add skills:")     
# employees[1001]['skills'].append('git')
# print(employees[1001]['skills'])
# print("Add phone number:")
# employees[1001].setdefault('phone',9360808933)
# employees[1002].setdefault('phone',9876543210)
# employees[1003].setdefault('phone',9360808933)
# print(employees)
# a = employees[1001]['salary']
# b = employees[1002]['salary']
# c = employees[1003]['salary']

# d = [a, b, c]

# high_sal = d[0]

# for i in range(1, len(d)):
#     if d[i] > high_sal:
#         high_sal= d[i]

# print("HIGH SALARY=",high_sal)

# a = employees[1001]['salary']
# b = employees[1002]['salary']
# c = employees[1003]['salary']

# d = [a, b, c]
# average=sum(d)/len(d)
        

# print("AVERAGE SALARY=",int(average))

# print("IT Employees:")
# for i ,employees in employees.items():

#      if employees['department']=='IT':
#       print(employees['name'])
      

# #maxmimum value finding

# # numbers = [10, 25, 7, 45, 18, 32]

# # max_value = numbers[0]

# # for i in range(1, len(numbers)):
# #     if numbers[i] > max_value:
# #         max_value = numbers[i]

# # print(max_value)

# #hard task 4
# """
# inventory = {
#     1: {
#         'name': 'Laptop',
#         'category': 'Electronics',
#         'price': 50000,
#         'stock': 5
#     },
#     2: {
#         'name': 'Phone',
#         'category': 'Electronics',
#         'price': 25000,
#         'stock': 10
#     },
#     3: {
#         'name': 'Chair',
#         'category': 'Furniture',
#         'price': 3000,
#         'stock': 2
#     }
# }

# print(inventory)

# print("Increase Laptop stock by 3")
# inventory[1]['stock']=5+2
# print(inventory[1]['stock'])

# print("Reduce Phone stock by 2")
# inventory[2]['stock']=10-2
# print(inventory[2]['stock'])


# inven= ['price']*['stock']
# print(inven)

# print("Low stock products")

# for i,inventory in inventory.items():
#     if inventory['stock']<=5:
#         print(inventory['name'])

# """


            