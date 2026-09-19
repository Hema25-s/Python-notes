'''
#task1
import numpy as np
num= np.array([10,20,30,40,50])
print(num)


#task2
import numpy as np
n=np.array([[1,2,3],
           [4,5,6]])
print(n)



#task3
import numpy as np
a=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)



#task4

import numpy as np
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(a.shape)




# task5
import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Rows:", a.shape[0])
print("Columns:", a.shape[1])


# task6
import numpy as np
a = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(a.shape)


# task7
import numpy as np
a = np.array([5, 10, 15, 20])
print(a + 5)


# task8
import numpy as np
a = np.array([2, 4, 6, 8])
print(a * 3)


# task9
import numpy as np
a = np.array([
    [1, 2],
    [3, 4]
])

print(a * 10)


# task10
import numpy as np
a = np.array([10, 20, 30])
print((a + 5) * 2)


# task11
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a + 10)


# task12
import numpy as np
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(a - 5)


# task13
import numpy as np
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)


# task14
import numpy as np
a = np.array([2, 3, 4])
b = np.array([10, 20, 30])

print(a * b)


# task15
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20, 30])

print(a + b)


# task16
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([2, 3, 4])

print(a * b)


# task17
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [10],
    [20]
])

print(a + b)


# task18
import numpy as np
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([10, 20])

try:
    print(a + b)
except ValueError:
    print("ValueError")


# task19
import numpy as np
a = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

b = np.array([100, 200, 300])

print(a + b)


# task20
import numpy as np
a = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

b = np.array([10, 20, 30])

print(a - b)



#task21&22
import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a[2])
print(a[-1])


#task23&24&25
import numpy as np
a = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(a[1][1])
print(a[0][0:])
print(a[1][0:])



#task26
import numpy as np
a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

t=[int(a[i][-1]) for i in range(len(a))]
print(t)



# task27
import numpy as np

a = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(a[1, 0, 1])


# task28
import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(a[:, 0])


# task29
import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(a[:, -1])


# task30
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

a[1, 1] = 50
print(a)


# task31
import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])

print(a[1:4])


# task32
import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])

print(a[-3:])


# task33
import numpy as np

a = np.array([10, 20, 30, 40, 50, 60])

print(a[::2])


# task34
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a[:2, 1:])


# task35
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a[:2])


# task36
import numpy as np

a = np.array([1, 2, 3, 4, 5])

a[2] = 100
print(a)


# task37
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

a[1:4] = 10
print(a)


# task38
import numpy as np

a = np.array([1, 2, 3, 4, 5])

a[1:4] = [20, 30, 40]
print(a)


# task39
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

a[2, :2] = [100, 200]
print(a)


# task40
import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a[::-1])


# task41
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.sum())


# task42
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.sum(axis=0))


# task43
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.sum(axis=1))


# task44
import numpy as np

a = np.array([10, 20, 5, 40, 15])

print("Mean:", a.mean())
print("Min:", a.min())
print("Max:", a.max())


# task45
import numpy as np

a = np.array([1, 2, 3, 4])

print(np.cumsum(a))


# task46
import numpy as np

a = np.array([1, 2, 3, 4])

print(np.cumprod(a))


# task47
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])

print(a.reshape(2, 3))


# task48
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.reshape(1, -1))


# task49
import numpy as np

zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
random_array = np.random.randint(10, 20, size=(3, 3))

print("Zeros:")
print(zeros)

print("Ones:")
print(ones)

print("Random array:")
print(random_array)


# task50
import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

result = np.where(a > 4, a, 0)

print(result)


# task51
import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Shape:", a.shape)
print("First row:", a[0])
print("Last column:", a[:, -1])

a = a + 5

print("After adding 5:")
print(a)

print("Total sum:", a.sum())
print("Column-wise sums:", a.sum(axis=0))
print("Row-wise sums:", a.sum(axis=1))
print("Mean:", a.mean())
print("Maximum:", a.max())

a[a > 50] = 100

print("After replacing values greater than 50:")
print(a)

print("Reshaped:")
print(a.reshape(1, 9))

print("Cumulative sum:")
print(np.cumsum(a))

print("Cumulative product:")
print(np.cumprod(a))

print("Zeros like:")
print(np.zeros_like(a))

print("Random array:")
print(np.random.randint(1, 10, size=(3, 3)))


# task52
import numpy as np

marks = []

for i in range(5):
    while True:
        try:
            mark = float(input(f"Enter mark {i + 1}: "))
            marks.append(mark)
            break
        except ValueError:
            print("Invalid input. Enter a number.")

marks = np.array(marks)

print("Marks:", marks)

for i in range(5):
    if marks[i] >= 50:
        print(f"Student {i + 1}: Pass")
    else:
        print(f"Student {i + 1}: Fail")

total = marks.sum()
average = marks.mean()
highest = marks.max()
lowest = marks.min()

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

with open("marks.txt", "w") as file:
    file.write(f"Marks: {marks}\n")
    file.write(f"Total: {total}\n")
    file.write(f"Average: {average}\n")
    file.write(f"Highest: {highest}\n")
    file.write(f"Lowest: {lowest}\n")

    for i in range(5):
        if marks[i] >= 50:
            file.write(f"Student {i + 1}: Pass\n")
        else:
            file.write(f"Student {i + 1}: Fail\n")

print("Results saved to marks.txt")


# task53
import numpy as np

a_values = []
b_values = []

for i in range(5):
    while True:
        try:
            value = float(input(f"Enter A value {i + 1}: "))
            a_values.append(value)
            break
        except ValueError:
            print("Invalid input. Enter a number.")

for i in range(5):
    while True:
        try:
            value = float(input(f"Enter B value {i + 1}: "))
            b_values.append(value)
            break
        except ValueError:
            print("Invalid input. Enter a number.")

A = np.array(a_values)
B = np.array(b_values)

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice: ")

try:
    if choice == "1":
        result = A + B
        operation = "Addition"

    elif choice == "2":
        result = A - B
        operation = "Subtraction"

    elif choice == "3":
        result = A * B
        operation = "Multiplication"

    elif choice == "4":
        if np.any(B == 0):
            raise ZeroDivisionError
        result = A / B
        operation = "Division"

    else:
        print("Invalid choice")
        result = None

    if result is not None:
        print("A:", A)
        print("B:", B)
        print("Result:")
        print(result)

        with open("calculator.txt", "w") as file:
            file.write(f"Array A: {A}\n")
            file.write(f"Array B: {B}\n")
            file.write(f"Operation: {operation}\n")
            file.write(f"Result: {result}\n")

        print("Result saved to calculator.txt")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# task54
import numpy as np

salaries = []

for i in range(5):
    while True:
        try:
            salary = float(input(f"Enter salary of employee {i + 1}: "))
            salaries.append(salary)
            break
        except ValueError:
            print("Invalid input. Enter a valid number.")

salaries = np.array(salaries)

print("Salaries:")
print(salaries)

for i in range(5):
    if salaries[i] >= 50000:
        category = "High Salary"
    elif salaries[i] >= 30000:
        category = "Medium Salary"
    else:
        category = "Low Salary"

    print(f"Employee {i + 1}: {category}")

total = salaries.sum()
average = salaries.mean()
maximum = salaries.max()
minimum = salaries.min()

print("Total Salary:", total)
print("Average Salary:", average)
print("Maximum Salary:", maximum)
print("Minimum Salary:", minimum)

with open("salary_report.txt", "w") as file:
    file.write("Employee Salary Report\n")
    file.write(f"Salaries: {salaries}\n")

    for i in range(5):
        if salaries[i] >= 50000:
            category = "High Salary"
        elif salaries[i] >= 30000:
            category = "Medium Salary"
        else:
            category = "Low Salary"

        file.write(f"Employee {i + 1}: {category}\n")

    file.write(f"Total: {total}\n")
    file.write(f"Average: {average}\n")
    file.write(f"Maximum: {maximum}\n")
    file.write(f"Minimum: {minimum}\n")

print("Report saved to salary_report.txt")


# task55
import numpy as np

temperatures = []

for i in range(7):
    while True:
        try:
            temp = float(input(f"Enter temperature for Day {i + 1}: "))
            temperatures.append(temp)
            break
        except ValueError:
            print("Invalid input. Enter a valid temperature.")

temperatures = np.array(temperatures)

print("Temperatures:")
print(temperatures)

for i in range(7):
    if temperatures[i] >= 35:
        category = "Very Hot"
    elif temperatures[i] >= 25:
        category = "Normal"
    else:
        category = "Cold"

    print(f"Day {i + 1}: {category}")

average = temperatures.mean()
highest = temperatures.max()
lowest = temperatures.min()
total = temperatures.sum()

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Total:", total)

with open("temperature.txt", "w") as file:
    file.write("Temperature Report\n")
    file.write(f"Temperatures: {temperatures}\n")

    for i in range(7):
        if temperatures[i] >= 35:
            category = "Very Hot"
        elif temperatures[i] >= 25:
            category = "Normal"
        else:
            category = "Cold"

        file.write(f"Day {i + 1}: {category}\n")

    file.write(f"Average: {average}\n")
    file.write(f"Highest: {highest}\n")
    file.write(f"Lowest: {lowest}\n")
    file.write(f"Total: {total}\n")

print("Report saved successfully.")



'''
