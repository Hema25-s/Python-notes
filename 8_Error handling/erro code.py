#                    ERROR HANDLING
'''
Are used to run the application when it has many type of error.

It has four block to handle error.


try:
  block of code
  # code for trying something like opening a file
except:
   block of code
   # this block of code runs when try had a error
else:
    block of code
    # it runs try doesn't have any error
fianlly:
     block of code
     (option)
     helps to denotes the code execution are in
     the last line.

EX:

try:
    file_name = input('Enter a file name to read: ').strip()
    with open(file_name,'r') as file:
        content = file.read()
except:
    print('Enter a valid file name')
else:
    print('File content:', content)
finally:
    print('program finished')


        SUMMARY ERROR MSG EXAMPLE

try:
    file_name = input('Enter a file name to read: ').strip()
    with open(file_name,'r') as file:
        content = file.read()
except Exception as e: # e has summary error msg
    print(e)
else:
    print('File c ontent:', content)
finally:
    print('program finished')


OUTPUT:
Enter a file name to read: data2.csv
[Errno 2] No such file or directory: 'data2.csv'
program finished

   
             HANDLING SPECIFC ERROR

try:
    file_name = input('Enter a file name to read: ').strip()
    with open(file_name,'r') as file:
        content = file.read()
except FileNotFoundError as e: # e has summary error msg
    print(e)
else:
    print('File content:', content)
finally:
    print('program finished')


            HANDLING MULTIPLE ERROR WITH SPECIFIC ERROR BLOCK

try:
    a=int(input('Enter a value: '))
    b=int(input('Enter b value: '))
    result = a/b
except TypeError as e:
    print('Type error value',e)
except ValueError as e:
    print('Value error value',e)
except ZeroDivisionError as e:
    print('Zero errro value',e)
else:
    print('Result:', result)
finally:
    print('program finished')


                      RAISE

used to throw the erro without doing any operations


EX:

try:
   raise TypeError('Sample error')
except TypeError as e:
    print('Type error value',e)
except ValueError as e:
    print('Value error value',e)
except ZeroDivisionError as e:
    print('Zero errro value',e)
else:
    print('Result:', result)
finally:
    print('program finished')
'''

#          DEBUGGING
'''

It is a process found the reason for the error.
It can be done by stopping the program execution
on the line which makes error.

For this pdb module are used and breakpoint() built in function are
also used.

pdb - python debugger module stops the program execution and
     opens the debugger terminal, where we can run set of following commands.

     p varibale_name - print
     c - continous execution


Pdb are already installed with python that can be imported at
at time on any file

EX:


import pdb

a=10
b=27
#pdb.set_trace()  # stops the program execution
result = a/b 
print(result)


                        EX FOR BREAKPOINT:

a=10
b=27
breakpoint()  # stops the program execution
result = a/b 
print(result)
'''



a=10
b=27
#breakpoint()  # stops the program execution
result = a/b 
print(result)
