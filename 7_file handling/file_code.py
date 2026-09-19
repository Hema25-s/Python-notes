#                   FILE HANDLING
'''
used to open close read write update delete files on a os

SYNTAX:

var_name = open('file_name','file_mode')
var_name.close()


FILE MODE:
1. r   = gives error if we try to read a non exisiting file
2. w   = when we open a file with write it creates the file if it is not exist, if exist it replace
3. r+  = read, write
4. w+ = write, read
5. a  = appends new content to the existing content
6. a+ = appends, read 


EX:
file = open('file.txt','w')
file.write('Sample content')
print('File created....')


EX 1:
file = open('file.txt','r')
content = file.read()
print(content)
file.close()


                           CONTEXT MANAGER

used to automatically closes the opend file
it uses with keyword

SYNTAX:

with open(file_name, file_mode) as variable_name:
     block of code

When the code execution comes to out of the block the file automatically closed.

EX:
with open('file.txt','w+') as file:
    file.writelines(['hi','hello','\n','how are you'])
    print('File created....')

    file.seek(0) # it moves the cursor to the needed file, where we want read

    #file_content = file.readlines() # returns like list of value
    file_content = file.read() # returns text value
    print('File content is, ')
    print(file_content)

EX:

with open('file.txt','w') as file:
    file.writelines(['sample text'])
    print('File created....')


EX:


with open('file.txt','a+') as file:
    file.writelines(['\n','New content'])
    print('File created....')

    file.seek(0)
    
    file_content = file.readlines()
    print(file_content)
'''


#       JSON FILE HANDLING
'''
Json - unstructured data that stores data like dictionary
It has .json extension.
json is the module used to read, write on json files.

                  WHAT IS MODULE

It is a python file or folder, some of the moduels will already installed
with python. One of the module is json

That needs to be imported by using import keyword.

All the modules can be imported only using import keyword

           JSON MODULE FUNCTIONS

1. dump() - used to write json data on json file
2. load() - used to read json data


EX FOR WRITE:

import json

data = {
    "name":'A',
    'age':23
}

with open('data.json','w') as file:
    json.dump(data, file, indent=4)
    print('File created...')



EX for READ:

import json

data = {
    "name":'A',
    'age':23
}

with open('data.json','r') as file:
    file_content = json.load(file)
    print(file_content)
'''

#                     TASK
'''
1. Ask user to enter a file name
2. Open the file and read the content
3. Paste the readed to on another file. 

'''
'''
with open('student.txt','w') as file:
     file.writelines(['Afsfwe','\n','Badws','\n','Cwfer','\n','Dwdfgd','\n','Ergftr'])
     print('File created..')
     print('*'*100)

with open('student.txt','r') as file:
    content = file.readlines()

    print('Each student as list')
    print(content)
    for name in content:
        print(name)

    print('Total no of student', len(content))

    print('Student name with five char')

    for name in content:
            if len(name)-1 == 5:
                 print(name)


    
with open('file1.txt','w') as f:
    f.writelines(['hi','\n','hello'])
print("Created successfully!!!!!!!!!!!!!") 
file1=input("Enter the file name:")
file2=input("Enter the next file name:")

with open(file1,'r') as f:
    content=f.read()
with open(,'w')as f:
    f.write(content) 
    print("content copied successfully")    
  
    
'''


#             CSV FILE READ AND WRITE
'''
                   WHAT IS CSV 

Comma seperated values, it is considered as excel file.
it has .csv as it's extension

                CSV MODULE

csv is the module used to read write on csv files.
it also needs to be imported before using it.
this module already installed with python

pip install csv  - run this command on ternimal

           WHAT IS PIP

Python module install manager, pip is a python file
used to install other python files from online


       WRITING CSV FILE

it takes data as list of dictionary for writing contents
inside the file.

EX:

[
{'key':'value'},
{'key':'value'},

]

key = column
value = row


EX:

import csv

data = [
    {'name':'A','age':234},
    {'name':'B','age':23}
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name','age']) # filednames = column name
    writer.writeheader() # writes the column which is specified on fieldnames

    writer.writerows(data)
    print('Created.....')



        READING EXAMPLES

import csv
with open('data.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'])
        print(row)
'''




