#              CFS
''''
Used to control the execution flow of the program


SYNTAX:

if condition:
   block of code 1
elif condition2:
     block of code 2
else:
    block of code 3

On above it control which block should run with the
specified condition.

To create block of code indendation is must


To make conditions operators are used 

                             OPERATORS

1. Arthimetic - +. -, *, /, //, **, %(modulo)

EX:

a=10
b=3
print(a/b)  # gives floating point value
print(a//b) # gives rounded value without decimal
print(10**2) # squares the no
print(a%b) # returns the remainder


2. Comparision operator  - ==, >=, <=, >, <, !=
   It returns only boolean result

EX:
a=10
b=3
print(a==b)

3. Logical operator - and, or, not
                      and - used to check more than two conditions are gives true
                      or - used to check atleat one condition is returns true
                      not - converts false to true, true to false

                    

Ex1:

a=20
b=20

result = (a>=18) and (b>=18)
print(result)

OUTPUT:
True

--------------------------------------------

Ex2:
a=20
b=2

result = (a>=18) or (b>=18)
print(result)

------------------------------------

Ex3:
a=20
b=2

result = not((a>=18) or (b>=18))
print(result)

OUTPUT:
False

----------------------------------


Ex4:
a=20
result = not(a>=18)
print(result)

OUTPUT:False



4. Membership operator -  in, not in

EX:
salary=[123,2,45,34,5]
member_of_list = int('5') in salary
print(member_of_list)


5. Identity operator - is, is not
   
   It checks two object are equal or not with the value

   EX:

#Object check

a=int("123")
b=int("123")

print(a is b)

# Data type check


a="123"
b="123"

print(a is b)


                           EXAMPLE FOR IF

a = 15

if a> 15:
    print('Yes a is 15')
elif a <=15:
    print('Yes lt eq 15')


Ex2:

a = 26


a = 26

if (a>15) and (a<20):
    print('15-20')
elif (a>20) and (a<25):
    print('20-25')
elif (a>25) and (a<30):
    print('25-30')
else:
    print('Other range')



Ex3:


a = 26

if (a>15) or (a<20):
    print('15-20')
elif (a>20) and (a<25):
    print('20-25')
elif (a>25) and (a<30):
    print('25-30')
else:
    print('Other range')


Ex4:

a=12
b=13

if a>10:
    print('A is gt 10')

    if b==10:
        print('B is 10')
    elif b==11:
        print('B is 11')
    elif b== 12 or b==13:
        print('B has value in 12-13')
    else:
        print('B has other value')

else:
    print('A has other value')
'''

a=12
b=13

if a%2 == 0:
    print('Even')

# 1
# user value
# digit print it is a digit -> convert those digit into int and float -> add converted int value + float value
# not a digit -> if check user value is alpha -> print('it is alphabet value') -> isalphnum -> 


# check if use enters digit value if he enters digit value check whethere it is negative or not negative value

# 
#-----------------------------------------------------------
# task1
a = input("Enter a value: ")

if a.isdigit():
    print("It is a digit")
    if a.startswith("-") and a[1:].isdigit():
        print("It is not a negative value")


    int_value = int(a)
    float_value = float(a)

    print("Integer value:", int_value)
    print("Float value:", float_value)
    print("Addition:", int_value + float_value)
else:

    if a.isalpha():
            print("It is an alphabet")

    elif a.isalnum():
            print("It is an alphanumeric value")

    else:
            print("User enter negative value")

#Task2

a=int(input("Enter a number to check ODD/Even:"))
if a%2 == 0:
      print(a,"-Its Even")
else:
      print(a,"- Its odd")