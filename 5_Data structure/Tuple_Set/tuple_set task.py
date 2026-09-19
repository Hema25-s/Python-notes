
# def check_value(a):
#      if type(a)==list:
#          result=list(a)
#      elif type(a)==set:
#        result=set(a)
#      else:
#          print("invaild")

#          return result

# a=[12,33,45,47,22,225]
# print(check_value(a))



# a=[234,234,234,456,67,567,76]

# def num(*a):
#     return f
#     Total= {a.count(a)}
    
# print(num(a))


# #task1
# a=(10, 20, 30, 40, 50)
# print(a[-1])


# #task2

# a=(10, 20, 10, 30, 10, 40, 20)
# res=a.count(10)
# print(res)


# #task3

# a=('A', 'B', 'C', 'D', 'E')
# res=a.index('D')
# print(res)

# #task4
# a=(12, 5, 23, 8, 40, 17, 3)
# for i in a:
#     if i>15:
#         print(i)

# #task5

# numbers=(1,2,3,4,5,6,7,8,9)
# for i in numbers:
#     if i%2==0:
#         print(i)


# #task6
# numbers = (-10, 20, -5, 30, -2, 40)

# def check(numbers):
#     print("Positive numbers:")
#     for num in numbers:
#         if num > 0:
#             print(num)

#     print("Negative numbers:")
#     for num in numbers:
#         if num < 0:
#             print(num)

# check(numbers)

# #task7 
   
# a= {i for i in range(1,11)}
# print(a) 
# print("numbers greater than 5:")
# for i in a:
#     if i>5:
#         print(i)
        


# #task8


# a = [234, 234, 234, 456, 67, 567, 76]

# def remove(a):
#     return set(a)

# print(remove(a))


# #task9

# a = {10, 20, 3, 45, 6, 80, 11}

# def greater(a):
#     for num in a:
#         if num > 20:
#             print(num)

# greater(a)



# #task10

# a = {1, 2, 3, 4, 5}

# def num(a):
#     a.add(100)
#     a.add(200)
#     return a

# print(num(a))



# #task11



# a = {1, 2, 3}
# b = {4, 5, 6}

# def update_set(a, b):
#     a.update(b)
#     return a
# print(update_set(a, b))


# #task12

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c=a.union(b)
# print(c)


# #task13

# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 6, 7}
# c= a.intersection(b)
# print(c)



# task14
# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 6, 7}
# c=b.difference(a)
# print(c)


# #task15
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c=a.symmetric_difference(b)

# print(c)

# #task16

# a = {10, 20, 30, 40, 50}

# def remove_values(a):
#     a.remove(30)
#     a.discard(100)
#     return a

# print(remove_values(a))


# #task17

# a = {1, 2, 3, 4, 5, 6}
# b = {1, 2, 3}

# def check_sets(a, b):
#     print("Is b subset of a?")
#     print(b.issubset(a))

#     print("Is a superset of b?")
#     print(a.issuperset(b))

# check_sets(a, b)


