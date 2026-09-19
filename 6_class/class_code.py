#                    CLASS
'''

It is collection of function that allows to use current python file function on
another python file. 

And that allows to reuse n no of functions on another python file.

It is mainly used for collabration and reuse purpose.

used to secure the code from the attackers.


               WHAT IS CONSTRUCTOR

Used to give values to the instance of the class
it can be created by __init__ function

It take value when the object is created.


         WHAT IS SELF

Keywors to access variables of a class inside the function.



SYNTAX:

class ClassName:
       instance_1=0
       instance_2=0  # variable

      def __init__(self): # self is used to access the variable(outside the function) inside the function
          self.instance = value   # used to initilaize values to the instance of the class
                                # instead of self we can use any letter or word

      def functions(parameter1):
          block of code

          
SYNTAX FOR USING CLASS:

variable_name = Classname()

EXAMPLE FOR NORMAL CLASS:

EX:

class Student:
    name = ''
    age = 0

    def __init__(self):
        self.name='hema'
        self.age = 12424535


SYNTAX_2 with constructor parameter:

class ClassName:
       instance_1=0
       instance_2=0  # variable

      def __init__(self, parameter1, parameter2):
          self.instance_1 = parameter1
          self.instance_2= parameter2

          
SYNTAX FOR USING CLASS:

variable_name = Classname(arugment_1,argument_2)

EXAMPLE FOR CONSTRUCTOR CLASS:

class Student:
    name = ''
    age = 0

    def __init__(self, a,b):
        self.name = a
        self.age = b 

        return a,b

Student1 = Student(1,2)


                          OBJECT


class Student:
    name = ''
    age = 0

    def __init__(self, a,b):
        self.name = a
        self.age = b 
        return a,b

#  OBJECT
Student1 = Student(1,2)



Ex3:

class Student:
    name = ''
    age = 0

    def __init__(self, a,b):
        self.name = a
        self.age = b 

    def display(self):
        print(self.name, self.age)

#  OBJECT
Student1 = Student(1,2)
Student1.display()

Student2 = Student(3,5)
Student2.display()



EX 3


class Student:
    name = ''
    age = 0

    def __init__(self, a,b):
        self.name = a
        self.age = b 

    def display(self, extra_details="234"):
        print(self.name, self.age, extra_details)

#  OBJECT
Student1 = Student(1,2)
Student1.display("25345345")

Student2 = Student(3,5)
Student2.display()

'''


# 1. Create a class name calculator that should has two instance a and b
# 2. Assign values for a and b with constructor
# 3. Create 4 function with name add, sub, mul, div all the functions should do its operations with a and b
# 4. Create One object by passing 3,4 as value, find add, sub, mul, div for this value
# 5. Create four type of object with different values, call add, sub, mul, div for all four 
# objects 
'''
class Calculator:
    a = 0
    b = 0

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def add(self):
        print("Add =", self.a + self.b)

    def sub(self):
        print("Sub =", self.a - self.b)

    def mul(self):
        print("Mul =", self.a * self.b)

    def div(self):
        print("Div =", self.a / self.b)


Calculator1 = Calculator(3, 4)
Calculator1.add()
Calculator1.sub()
Calculator1.mul()
Calculator1.div()

print()

Calculator2 = Calculator(10, 5)
Calculator2.add()
Calculator2.sub()
Calculator2.mul()
Calculator2.div()

print()

Calculator3 = Calculator(20, 4)
Calculator3.add()
Calculator3.sub()
Calculator3.mul()
Calculator3.div()

print()



Calculator4 = Calculator(15, 3)
Calculator4.add()
Calculator4.sub()
Calculator4.mul()
Calculator4.div()


EX2:

class Calculator:
     a=0
     b=0
     def __init__(self,x,y):
          self.a=x
          self.b=y
     def add(self):
        print("ADDITION:",self.a+self.b)
     def sub(self):
            print("SUBRACTION:",self.a-self.b)
     def mul(self):
            print("MULTIPLICATION:",self.a*self.b)
     def div(self):
       print("DIVISION:",self.a/self.b)

a=int(input("Enter a 1stnumber to calculate:"))

b=int(input("Enter a 2nd number to calculate:"))

Calculator1 = Calculator(a,b)
Calculator1.add()
Calculator1.sub()
Calculator1.div()
Calculator1.mul()


'''

#                    INHERITANCE
'''
Process of combining two or more class to reuse one class functions and instances on another class.


SYNTAX:

class class_name1:
      constructor

      functions


class class_name2(class_name1):
      constructor -> child class
      call parent class constructor

      functions 


TYPES OF INHERITANCE

1. Single        - a class connect with only one class
2. Multiple     - a class connect with more than one class

EX:

class parent1: 
      pass
      
class child1:
      pass
      
class child2(child,parent1):
      pass



2. Multi level - 

EX:
class parent1: 
      pass
      
class child(parent1):
      pass
      
class child2(child):
      pass
      


EX CODE:

class Train:
    from_location = ''
    to_location = ''
    arrival_time = ''

    def __init__(self, a,b,c):
        self.from_location = a
        self.to_location = b
        self.arrival_time = c  

    def display_train_details(self, train_no):


        details = f"""
        Train name: XYZ Express
        From location: {self.from_location}
        To location: {self.to_location}
        """

        if train_no == 101:
            details = f"""
Train name: ABC Express
From location: {self.from_location}
To location: {self.to_location}
"""
            return details
        
        else:
            return details



class Passanger(Train):
    pas_name = ''
    age= 0

    def __init__(self, a, b, c, pass_name, age):
        super().__init__(a, b, c)   #  parent class constructor, super is the keyword used to call parent class constructor witha argument
        self.pas_name = pass_name
        self.age = age

    def display_all_details(self, train_no):
        self.display_train_details(train_no) # by using self keyword we can access parent class functions and instance

        passanger_details = f"""
Passanger name: {self.pas_name}
Age:            {self.age}
Arrival time: {self.arrival_time}
"""

        return passanger_details


train1 = Train('A','B','23:00')

print(train1.display_train_details(101))


pass1 = Passanger('A','B','24:00','Hema',23434)
print(pass1.display_all_details(102))

'''


#             METHOD OVERRIDING  & OVERLOADING
'''
METHOD OVERRIDING  - same name with different functionality


EX:
class Library:
    lib_name= "ABC"
    lib_location = "XYZ"

    def display(self):
        print(f"""

        Library details:

        Library name: {self.lib_name}
        Located at: {self.lib_location}
        """)




class Book(Library):
    book_name= "A"
    book_location = "X"

    def display(self):
        print(f"""

        Book details:

        Book name: {self.lib_name}
        Located at: {self.lib_location}
        """)


Book1 = Book()
Book1.display()



METHOD OVERLOADING - same function with different parameter


EX:


class Library:
    lib_name= "ABC"
    lib_location = "XYZ"

    def display(self):
        print(f"""

        Library details:

        Library name: {self.lib_name}
        Located at: {self.lib_location}
        """)




class Book(Library):
    book_name= "A"
    book_location = "X"

    def display(self,a,b):
        print(f"""

        Book details:

        Book name: {self.lib_name}
        Located at: {self.lib_location}
        """)


Book1 = Book()
Book1.display(1,2)
Book1.display(2,3)


'''


#                         ENCAPSULATION
'''
A class is considered as encapsulation that used to store
collection mini functions and instance like mini medicine inside
a plastic capsule.



class Library:
    lib_name= "ABC"   # global scope
    _lib_location = "XYZ" # protect scope
    __lib_size = 234434 # private



    def __display_lib_details(self):   #   private
        print("Lib details")


class Book(Library):
    book_name= "A"
    book_location = "X"

    def display(self):
        print('Public lib values:')
        self.lib_name="CAB"
        print(self.lib_name)

        self._lib_location = 'ZYX'
        print(self._lib_location)

        #print(self.__lib_size) # gives error

        #self.__display_lib_details()# gives error

Book1 = Book()
Book1.display()


'''

