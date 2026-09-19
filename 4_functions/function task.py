# 1.
"""
def p(name):
    return f"Welcome {name}! Have a great day at work."

name = input("Name: ")
print(p(name))


# 2. 

def student(name, age, course):
    return f"Name: {name}\nAge: {age}\nCourse: {course}"

name = input("Name: ")
age = input("Age: ")
course = input("Course: ")

print(student(name, age, course))


# 3. 

def product(name, price):
    return f"Product: {name}\nPrice: {price}"

name = input("Product: ")
price = input("Price: ")

print(product(name, price))


# 4. 

def employee(name, salary):
    return f"Employee: {name}\nSalary: {salary}"

name = input("Name: ")
salary = input("Salary: ")

print(employee(name, salary))


# 5. 

def square(num):
    return num * num

num = int(input("Number: "))
print("Square:", square(num))


# 6. 

def total_price(price, quantity):
    return price * quantity

price = int(input("Price: "))
quantity = int(input("Quantity: "))

print("Total:", total_price(price, quantity))


# 7.

def temperature(c):
    return (c * 9/5) + 32

c = float(input("Celsius: "))

print("Fahrenheit:", temperature(c))



#8.

def student_mark(mark):
    return f"PASS" if mark >=40 else "FAIL"
mark=int(input("MARK:"))
print(student_mark(mark))



#9.

def voting(age):
    return f"you can vote" if age >=18 else"cannot vote"
age=int(input("Age:"))
print(voting(age))

#10.

def account(login):
    return f"Account active" if login<=3 else"Account locked"
login=int(input("Attempts:"))
print(account(login))

#11.
def amount(order):
    return f"Free delivery" if order>=500 else"Delivery chareg applicable"
order = int(input("Order amount:"))
print(amount(order))

#12.

def salary(bonus):
    return f"Bonus eligible" if bonus>=50000 else"Not eligible"
bonus=int(input("Salary:"))
print(salary(bonus))

#13.

def age(a):
    return f"Adult" if a>=18 else"Minor"
a=int(input("Age:"))
print(age(a))



#14.

def amount(amt):
    return f"Discount available"if amt>=1000 else"no discount"
amt=int(input("Purchase:"))
print(amount(amt))


#15.

def password(len):
    return f"vaild password length" if len>=8 else"invaild length"
len=int(input("Length:"))
print(password(len))



#16,17,18

sales = [1200, 850, 2300, 1750, 900]
total=sum(sales)
min=min(sales)
max=max(sales)
print("Total:",total)
print("Minimun:",min)
print("Maximum:",max)



#19,20

salaries = [45000, 32000, 75000, 28000, 60000]
asc=sorted(salaries)
des=sorted(salaries,reverse=True)
print(asc ,des)


#21,22

marks = [78, 92, 65, 88, 74]
m=sum(marks)
a=max(marks)
print("Highest mark:",a)
print("Total marks:",m)


#26,27
code=int(input("Code:"))
char=(input("Character:"))
print("Charcter:",chr(code))
print("Code:",ord(char))


#28

emp=int(input("Emp ID:"))
print("Memory ID:",id(emp))


#31

def total_order(*price):
    return sum(price)
print("Total order:",total_order(100, 250, 500, 150))



#32

def emp(*salaries):
    return max(salaries)
print("Highest salary:",emp(25000, 45000, 32000, 75000, 50000))

"""

#33
def sales(*values):
    return f"""
     Total sales={sum (values)} 
     Lowest sales={min(values)}
     Highest sales={max(values)}

     """
print (sales(1200, 3500, 2200, 4800, 1500))

#37

def details(*details):
    print("Name:", details[0])
    print("Age:", details[1])
    print("Department:", details[2])

details("Arun", 25, "IT")


#38
def cus(*value):
    print("Name:",value[0])
    print("Age:", value[1])
    print("city:",value[2])

cus("hema",28,"Gobi")


#40 

def num(*add):
    return f"""
    Total={sum(add)}
    """
print(num(10,20,30,40,50))

#43

age=lambda x:"Eligible" if x>=18 else "not eligible"
r=age(25)
print(r)

#44

mark=lambda x:"Pass" if x>=40 else"Fail"
m=mark(35)
print(m)

#45
amt=lambda x:"Discount" if x>=1000 else"no discount"
a=amt(1200)
print(a)


#46

sq=lambda x:x*x
q=sq(8)
print(q)


# 47
salary = lambda s1, s2: max(s1, s2)
print("Higher Salary:", salary(45000, 52000))


# 48
smaller_price = lambda p1, p2: min(p1, p2)
print("Lower Price:", smaller_price(1500, 1200))


# 49
even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print(even_odd(105))


# 50
age_category = lambda age: "Adult" if age >= 18 else "Minor"
print(age_category(16))


# 51
salary_category = lambda salary: "High Salary" if salary >= 50000 else "Normal Salary"
print(salary_category(65000))


# 52
number_status = lambda n: "Positive" if n > 0 else "Not Positive"
print(number_status(-10))


# 53
def employee_count(n):
    if n == 0:
        return
    print(n)
    employee_count(n - 1)

employee_count(5)


# 54
def registration_counter(n, current=1):
    if current > n:
        return
    print(current)
    registration_counter(n, current + 1)

registration_counter(5)


# 55
def fact(n):
    if n <= 1:
        return 1
    else:
       return n * fact(n - 1)
print("Factorial:", fact(5))


# 56
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

print("Total:", total(5))


# 57
def product(n):
    if n <= 1:
        return 1
    return n * product(n - 1)

print("Product:", product(5))


# 58
def countdown(n):
    if n == 0:
        print("Start!")
        return
    print(n)
    countdown(n - 1)

countdown(3)


# 59
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

print("Result:", power(2, 4))


# 60
def employee_factorial(n):
    if n <= 1:
        return 1
    return n * employee_factorial(n - 1)

print("Factorial:", employee_factorial(6))


























































