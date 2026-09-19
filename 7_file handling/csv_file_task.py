'''
#task1


import csv
data = [
    {'name': 'Arun', 'age': 20, 'marks': 85},
    {'name': 'Priya', 'age': 21, 'marks': 92},
    {'name': 'Rahul', 'age': 19, 'marks': 78},
    {'name': 'Divya', 'age': 20, 'marks': 88}
]
with open ('data.csv','w',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=['name','age','marks'])
    writer.writeheader()
    writer.writerows(data)
    print("Created####")

with open('data.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row['name'],row['age'],row['marks'])    


'''

#task2

import csv
things=[
    {'product': 'Laptop', 'price': 55000, 'quantity': 5},
    {'product': 'Mouse', 'price': 800, 'quantity': 20},
    {'product': 'Keyboard', 'price': 1500, 'quantity': 10},
    {'product': 'Monitor', 'price': 12000, 'quantity': 7}
]
with open('things.csv','w',newline='')as file:
    writer=csv.DictWriter(file,fieldnames=['product','price','quantity'])
    writer.writeheader()
    writer.writerows(things)
    print("File created!!!!!!!!!!!!")
with open('things.csv','r')as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row['product'],row['price'],row['quantity'],int(row['price'])*int(row['quantity']))   