#        FUNCTION
'''
Reusable block of code

Types of functions

1. Built in function       - it is developed by python developer
                             EX: print(), input(), int()


EX:

a=[1,23,425,34,534,2]

total = sum(a) # min, max
b = sorted(a)

c=sorted(a, reverse=True)

memory_location_of_c, char_of_digit, digit_of_char = id(c), chr(70), ord('A')

#   id -> gives hardware location of the variable
# chr -> returns character at givem index
# ord -> gives index at the specified character
print(char_of_digit, digit_of_char)



2. User defined function   - developed by python programmers

SYNTAX:

def function_name():
    block of code

    
SYNTAX 2:

def function_name(parameter1, parameter2, parametern): # parameter -> input value for function
    block of code


SYNTAX 3:

def function_name(parameter1, parameter2, parametern): # parameter -> input value for function
    block of code
    return some_value


SYNTAX 4 FOR MULTI ARGUMENT FUNCTION:

def function_name(*parameter): # *parameter -> takes n no of input value
    block of code
    return some_value

    
EX1:

def print_name():
    print('Hema')

print_name()


EX2:

def print_name_with_given_details(age, address):

    result = f"""
    Name: Hema
    Age: {age}
    Address: {address}
    """

    print(result)

print_name_with_given_details(123,253463463)


Ex3:


def print_name_with_given_details(*details):

    result = f"""
    Name: Hema
    Age: {details[0]}
    Address: {details[1]}
    """

    return result

personal_info = print_name_with_given_details(1223,234235)

print(personal_info)



                   LAMBDA FUNCTION

It is called anonymous functions, it doesn't have any name

SYNTAX:

variable_name  = lambda parameter1,parameter2: block of code

SYNTAX FOR ONE LINE IF CONDITION:

variable_name = true_value if condition else false_value


EX:
voter = lambda x: "you can vote" if x>=18 else "can't vote"

result = voter(22)
print(result)


Ex2:

square = lambda x:x**2

print(square(2))


EX3:

courses = ['A','B','C']

is_student = lambda age,course: True if age<=18 and course in course else False

stu_age = 16
stu_course = 'C'

if(is_student(stu_age,stu_course)):
    print('He or she is a student')

    

                  RECURSIVE FUNCTION (important interview question)


A function calls it's are called recursive function

EX:

def fact(a):
    if a==0:
        return 1
    else:
        return a * fact(a-1)
    """
    a=5 

    5 * fact(5-1) => 
               fact(4) =>
                       4 * fact(3) =>
                            3 * fact(2) =>
                                2 * fact(1) =>
                                    1 * fact(0) => 1
    """

result = fact(5)
print(result)

# 5! = 5*4*3*2*1 

'''

#           LOCAL GLOBAL SCOPE
'''

a='hello' # global scope

def msg():
    global a  # updates the a value when it called.
    a='how are you?'   # local scope
    print('Function calling time a value is ',a)

print('Before calling function a value is ',a)
msg()
print('After calling function a value is ',a)



EX2:

def msg_1():
    a='hello'

    def msg_2():
        nonlocal a  # it updates the upper function local value
        a="How are you"
        print('Message 2 a value is ', a)

    msg_2()
    print('Message 1 a value is ', a)

msg_1()

'''

def msg_1():
    a='hello'

    def msg_2():
        nonlocal a  # it updates the upper function local value
        a="How are you"
        print('Message 2 a value is ', a)

    msg_2()
    print('Message 1 a value is ', a)

msg_1()

    


