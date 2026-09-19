#         VARIABLES AND DATA TYPES
'''
Variable is a container that are used to store different type of values.


RULES FOR VARIABLE NAME:

Name shouldn't starts with no, special character
It shouldn't contain any space.

Data types:
1. numeric - int, float, complex
2. text or string - '', " ", """ """(used for store paragraph like text on variable)
3. boolean - True, False


EX:

first_name = 'hema'
bio = """
      sample text 1
      sample tex 2
"""
age=12324
salary = 23454.344
temp = 235.34j # complex  235 - real part, 34j-imaginary part
is_student = True


EX2:
first_name, age, salary = 'hema',124234,234235.234
'''

#                INPUT AND OUTPUT
'''
input() - it is a function used to take input values from user
print() - used to produce and see the output

SYNATX:

variable_name = input('msg')
print(variable_name)

EX:

name = input('Enter a name: ')
print('You entered value',name)


EX2:

first_name = 'hema'
bio = """
sample text 1
sample tex 2
"""
age=12324
salary = 23454.344
temp = 235.34j # complex  235 - real part, 34j-imaginary part
is_student = True

print('first name is',first_name)
print('bio ', bio)
'''


#                 FUNCTIONS
'''

It is method that are developed by python developer

'''

#                TYPE CASTING
'''
used to see the data type of a variable's value and used to
convert one data type to another data type.

EX:
int -> str
bool -> int

For check the data type of variable we need to use type() functions

SYNTAX(grammer) FOR TYPE:

variable_name = type(give the variable name you want to check data type)


EX:
first_name = 'hema'
bio = """
sample text 1
sample tex 2
"""
age=12324
salary = 23454.344
temp = 235.34j # complex  235 - real part, 34j-imaginary part
is_student = True


data_of_bio = type(temp)
print('Data type of variable bio is',data_of_bio)



                     TYPE CASTING FUNCTIONS

1. int()
2. float()
3. complex()
4. str()
5. bool()

SYNTAX:

variable_name = type_casting_function(variable_name)

EX:
b="10"
converted_b = int(b)
print('Data type of b =', type(b), b)
print('Data type of converted_b =', type(converted_b), converted_b)

Ex2:

b=float("10")
print('Data type of b =', type(b), b)

Ex3:

b=int("10.345")
print('Data type of b =', type(b), b)

OUTPUT:
ValueError

Ex4:

b=complex("10")
print('Data type of b =', type(b), b)

OUTPUT:
Data type of b = <class 'complex'> (10+0j)

Ex5:

a=bool(" ")
print('Data type of a =', type(a), a)

OUTPUT:
Data type of a = <class 'bool'> True

a=bool("")
print('Data type of a =', type(a), a)

OUTPUT:
Data type of a = <class 'bool'> False


Ex6:

a=input('Enter a: ')
converted_a = int(a)
print('Data type of a is ', type(a))
print('Data type of a is ', type(converted_a))

a=int(input('Enter a: '))
print('Data type of a is ', type(a), a)

OUTPUT:
Enter a: wfr
ValueError: invalid literal for int() with base 10: 'wfr'


EX7:

a=bool(input('Enter a: '))
print('Data type of a is ', type(a), a)

OUTPUT:
Enter a: gredre
Data type of a is  <class 'bool'> True
'''


#                  STRING FUNCTIONS
'''
Collection of elements or letter or sequence
In python it is immutable(can't be changed)


name="345jin"

# UPPER
# name = name.upper()
# print(name)

# name = name.lower()

# print(name.capitalize())
# print(name.title())
# print(name.count('a'))
# print(name.strip())
# print(name.startswith('h')) # returns true or false value
# print(name.endswith('o'))
# print(name.__contains__('a'))

# #print(name.split(' '))

# first_name, last_name = name.split('22')
# print(first_name)

print(name.isalnum())
print(name.isdigit())
print(name.isdecimal())


                       INDEX

Address of each elememt in the string

name = 'hema'
 left-> 0123
       -4 -3 -2 -1 right   

Used to access particular letter or specific no of letter in a
string

SYNTAX TO WORK WITH INDEX:
variable_name[index]

EX:
name = 'hema somu'
print(name[0])
print(name[-1])


SYNATX TO WORK WITH SLICING:
variable_name[start_index:end_index-1]


Ex2:
name = 'hemasomu'
print(name[2:6])

OUTPUT:
maso


SYNATX 2:
variable_name[:end_index-1]
variable_name[start_index:]

EX:

name = 'hemasomu'
print(name[1:])
print(name[:5])

OUTPUT:
emasomu
hemas


SYNTAX 3:
variable_name[start_index:end_index-1:step_value]

EX:
name = 'hemasomukumar'
print(name[1:12:3])


SYNTAX 4:
variable_name[::step_value]

EX:
name = 'hemasomukumar'
print(name[::3])

Ex2:
name = 'hemasomukumar'
print(name[-1:-10:-2])

OUTPUT:
rmkms

EX3:
name = 'hemasomukumar'
print(name[::-1])

OUTPUT:
ramukumosameh


                       STRING TEMPLATING or FORMATTED STRING

"
Dear sir/mam {name}
       Sample content
"

To print the result in above formated string value, use can use f string

EX:

name = "hema"
result = f"Dear sir/mam {name}\n Sample content"
print(result)


                 CONCATNATION

Process of combining more than one string 

EX:
name = 'hema'
msg = 'welcome'
print(name+msg)


EX2:
name = 'hema'
rep_name = name * 10
print(rep_name, end=' ')
print(rep_name)

'''

name = 'hema'
rep_name = name * 10
print(rep_name, end=' ')
print(rep_name)


