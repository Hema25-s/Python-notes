#           FOR LOOP
'''
Used to do particular task in repeatative manner and for sequence(collection of elements) iteration(one by one accessing operation)


SYNTAX FOR SEQUENCE ITERATION:

for variable_name in sequence_variable_name:
    block of code


EX:

a= 'hema'
for char in a:
    print(char)


SYNTAX FOR LOOPING OPERATION:

for vairable_name in range(start_value (optional), end_value-1, step_value (optional)):
    block of code

EX:
a= 'hema'
for time in range(1,50):
    print(time,'hi')

Ex2:

a= 'hema'
for time in range(50):  # lopp starts from 0
    print(time,'hi')


Ex3:

a= 'hema'
for time in range(0,50,5):
    print(time,'hi')



SEQUENCE ITERATION 2:

a= 'hema'

for i in range(len(a)):
    print(a[i])


"""

#          WHILE LOOP

It is also a loop that helps to do looping task that doesn't knows it's range

It runs the loop until the conditions gets false

If the condition is not given properly it will convert as a infinite loop,
becuase condition is helps to stop the loop, the condition make the process
gets false

EX:
Application running functionality

SYNTAX:

start_value

while end_value_with_condition:
      step_value

      
EX:
a=0
while a<=10:
    print(a)
    a+=1  


Ex_2:
a=0
while a<=10:
    print(a)
    a+=2

Ex3:
a=0
while a<=10:
    print(a)
    a+=2


Ex4: FOR INFINITE LOOP

while True:
    print('hi')







#     ASSIGNMENT OPERATOR

+=, -=, *=, /=, //=, %=

EX:
a=10
b=2
a %= b #  a = a % b
print(a)
'''


#         LOOPING CONTROL STATEMENTS
'''
1. break - used to stop loop with specific condition
2. continue - used to skip the particular loop
3. pass - used to create empty block


EX:

while True:
    user_input= input('Enter c to continue or q to quit the loop: ')
    if user_input.strip() == 'c':
        print('Looping continuing.......')
    elif user_input.strip() == 'q':
        print('Loop stopped')
        break
        

EX FOR CONTINUE:

for i in range(1,10):
    if i==6: continue
    print(i)

OUTPUT:
1
2
3
4
5
7
8
9


Ex FOR PASS:

for i in range(1,10):
    if i==6: pass
    print(i)
'''

"""
for i in range(1,10):
    if i==6: pass
    print(i)
    """