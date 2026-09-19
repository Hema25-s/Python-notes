'''
#task1
try:
    a=int(input("enter a num1:"))
    b=int(input("enter a num2:"))
    result=a/b
except ZeroDivisionError as e:
    print("divided by zero",e) 
else:
    print("RESULT",result) 
finally:
    print("Finish")          

#task2
try:
    a=int(input("Enter a number:"))
except ValueError as e:
    print("You enter a text!")
else:
    print("You enter a number=",a)
finally:
    print("Program finish!!!!!!")   

    

#task3
     

try:
    a=input("Enter a file name to open:")
    with open("student.txt",'r')as file:
        file_content = file.read() 

except FileExistsError as e:
    print("File doesn't exist",e) 
else:
    print('File content is,',file_content)
    
finally:
        print("Program over")                         


#task4
try:
    print("Program finished")
except TypeError as  e:
    print(e)
else:
    print("program finished")
finally:
    print("Program finished")


#task5


def raise_value_error(age):
    if age < 0:
       raise ValueError('Sample msg')

try :
    age=int(input("Enter a age:"))
    raise_value_error(age)
except ValueError as e:
    print("ValueError",e)
finally:
   print("Program finished!!!!!!!!!!!")  

   

#task6
try:
    a=input("enter hi to open:")
except ValueError:
    print("Invalid")
else:
    print("No error occurred")


#task7
try:
   name=input("Enter a name:")
   if name=='':
      raise ValueError("sample msg")
except ValueError as e:
   print("you entered empty name")
else:
   print("Your name=",name)



#task8
a=["10","20"]
try:
   num=[int(x) for x in a]
   print(num)
except ValueError :
   print("Invalid")
    



#task9
try:
    a="a"
    b=4
    result=a+b
except TypeError:
    print('addition operation between int and string.')
else:
    print(result)

'''

#task10

try:
    num=int(input("Enter a number="))
    print("you entered=",num)
except :
    print("Invalid")
finally:
    print("Done")




