'''
#task1
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
                 

'''
#task2
with open('num.txt','r') as file:
