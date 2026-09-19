'''
#task1

class vehicle():
    def start(self):
        print("car is going to start")

class Car(vehicle):
    def start(self):
        print("car engine is starting")

car1=Car()
car1.start()            

#task2

class Animal():
    def sound(self):
        print("Dog says:shhhhh")
class Dog() :
    def sound(self):
        print("Dog says:Bark")
dog1=Dog()
dog1.sound()  

#task3

class Employee():
    def work(self):
        print("developer is reading the code")           

class Developer(Employee):
    def work(self):
        print("Developer is writing code" )

dev=Developer()
dev.work()        


#task4

class School():
    School_name = "ABC School"
    School_location = "Chennai"


    def display(self):
        print(f"""
        Student details:
        School name = {self.School_name}
        School location = {self.School_location}

        """)
class Student(School):
-    Student_name="Hema"
    Student_class="10th"
    def display(self):
        print(f"""
Student details:

Student name: {self.Student_name}
Student class: {self.Student_class}
""")
stu=Stud*ent()
stu.display()            


#task5


class Calculator():
 
   def add(self,a,b,c=0,d=0):
        return a + b + c + d
cal=Calculator()
print(cal.add(10,20))
print(cal.add(10,20,30))
print(cal.add(10,20,30,40))






#task7
class BankAccount:
    account_name = "Arun"
    _balance = 50000
    __account_pin = 1234

    def display(self):
        print("Account name:", self.account_name)
        print("Balance:", self._balance)


b = BankAccount()
b.display()

print(b.__account_pin)    



#task8
class Hospital():
    hospital_name = "City Hospital"
    _hospital_location = "Chennai"
    __hospital_code = 9876
    def display(self):
        print("Hospital name:",self.hospital_name)
        print("Hospital Location:",self._hospital_location)
class Doctor (Hospital):
        def display(self):
               print("Hospital name:",self.hospital_name)
               print("Hospital Location:",self._hospital_location) 

doc=Doctor()
doc.display()



#task9
class Company():
    company_name = "TechWorld"
    _company_location = "Bangalore"
    __company_salary = 50000
    def call(self):
        print("Company name:",self.company_name)
        print("Company location:",self._company_location)
class Employee(Company):
    def call(self):
         print("Company name:",self.company_name)
         print("Company location:",self._company_location) 

emp=Employee()
emp.call()                


#task10
class Restaurant():
    restaurant_name = "Food Corner"
    _restaurant_location = "Chennai"
    __restaurant_code = 4567
    def display(self):
        print("Restaurant name:",self.restaurant_name)
        print("Restaurant location:",self._restaurant_location)
class Menu(Restaurant):
        
         def display(self):
                 print("Restaurant name:",self.restaurant_name)
                 print("Restaurant location:",self._restaurant_location)
         
         def  price(self,a,b=0,c=0):
               return    a + b + c        
menu1=Menu()
menu1.display()
print(menu1.price(100))
print(menu1.price(100, 50))
print(menu1.price(100, 50, 25))
'''



#task6
""" 

class Message():
     
     def send(self,message,to,location):
          if message.strip()!='':
               print("Message:",message)

mes=Message()
mes.send("Hello")
mes.send("Hello", "Rahul")
mes.send("Hello", "Rahul", "Chennai")

    """

n=int(input())
t=tuple(input().split(' '))
print(hash(t))      
          