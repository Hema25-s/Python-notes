#task 1
"""a=input("Enter withdrawal amount:")
if a.isdigit():
    a1=int(a)
    if a1%100==0:
        print("Valid withdrawal amount") 
    else:
        print("Amount must be in multiples of 100")
else:
    print("Invalid")
print("****************************************************")    


#task 2

mark=int(input("Enter your mark:"))
if mark>=40:
    print("PASS")
else:
    print("FAIL")
print("****************************************************")



#task3
age=int(input("Enter your age:"))
if age>=18:
    print("Eligible for driving license")
else:
    print("Not Eligible")
print("******************************************************")    




#task4


unit=int(input("Enter units:"))
if unit<100:
    print("Low consumption")
elif (unit>=100) and (unit<=200):
    print("Medium consumption")
elif(unit>=201) and(unit<=500):
    print("High consumption")
elif(unit>500):
    print("Very high consumption")
else:
    print("Invaild")
print("********************************************")    


#task5


amt=int(input("Enter shopping amount:"))
if amt>=5000:
    print("20% discount")
elif amt>=3000:
    print("10% discount")
elif amt>=1000:
    print("5% discount")
else:
    print("NO DISCOUNT")
print("************************************************")




    #task 6


pin=(input("Enter your pin:"))
if pin.isdigit():
    if pin=="1234":
        print("Access granted")
    else:
        print("Incorrect PIN")
else:
    print("PIN must contain digits only")
print("****************************************************")

#task7

emp=int(input("Enter employee ID:"))
if emp%2==0:
    print("Employee ID is EVEN")
else:
    print("Employee ID is ODD")
print("*****************************************************")    



#task8

num=int(input("Enter number:"))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
elif num==0:
    print("Zero")
else:
    ("Invaild")
print("***************************************************")    



#task9

mob=(input("Enter a mobile number:"))
if mob.isdigit():
    if mob.startswith(("9","8","7","6")):
        print("Vaild mobile number")
    else:
        print("Invaild mobile number")
else:
    print("invaild")    

#task10
user=input("Enter username:")
if user.isalpha():
    print("Username contains alphabets only")
elif user.isdigit():
    print( "Username contains digits only")
elif user.isalnum():
    print("Username is alphanumeric")
else:
    print("Username contains special characters")


#task11
bal=int(input("Enter balance:"))
if bal>=1000:
    print("Minimum balance maintained")
else:
    print("Minimum balance not maintained")




#task12

username=input("Username:")
password=input("Password:")
if (username=="admin") and (password=="1234"):
    print("Login successful")
else:
    print("not login")




#task13


age=int(input("Enter age:"))
mark=int(input("Enter mark:"))
if (age>=17) and (mark>=60):
    print("Eligible for admission")
else:
    print("Not Eligible for admission")


    

#task14

ser=input("Enter the emergency service: ")
if (ser=="ambulance"):
  print("Emergency service available")
elif (ser=="police"):
 print("Emergency service available")
else:
  print("Invalid emergency service")



#task15

day=input("Enter a day:")
if (day=="Saturday"):
   print("It is Weekend.")
elif(day=="Sunday"):
     print("It is weekend.")
else:
     print("It is a working day")
 
#task18


coupon=input("Enter a coupon:")
if 'SAVE10' in coupon:
    print("Valid coupon")
elif 'SAVE20' in coupon:
    print("Valid coupon")
elif 'WELCOME' in coupon:
    print("Valid coupon")
else:
    print("invalid coupon")


#TASK21

a = input("Enter a value: ")
if a.startswith("-") and a[1:].isdigit():
        print(" negative number")
else:
        print("Not a negative number")
--------------------------------------------------------------        
#task24
bill=input("Enter bill:")
pep=input("Enter people")
if bill.isdigit:
    print("Amount per person:",p)
    

#task25

price=int(input("Enter price:"))
quantity=int(input("Enter quantity:"))
total=price*quantity
print("Total=",total)
if total>=5000:
    print("Eligible for discount")
else:
    print("Not eligible")
    
#task26

bank1=int(input("Account 1 balance="))
bank2=int(input("Account 2 balance="))

if bank1>bank2:
    print("Account 1 has higher balance")
elif bank2>bank1:
        print("Account 2 has higher balance")

elif bank1==bank2:
      print("Both balances are equal")
else:
      print("Invaild")


#task28


age = int(input("Enter age: "))
department = input("Enter department: ")

if age >= 18 and (department == "IT" or department == "Security"):
    print("Eligible for night shift")
else:
    print("Not eligible for night shift")
    


#task29

balance = int(input("Enter balance: "))
withdrawal =int (input("Enter withdrawal amount: "))
if int(withdrawal):
    if withdrawal <= balance:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Invalid withdrawal amount")
"""

# task30

name = input("Enter name: ")
age = input("Enter age: ")
mobile = input("Enter mobile: ")
if name.isalpha():
    n1=True
    print("Valid name")
else:
    n1=False
    print("Invalid name")
if age.isdigit():
    age = int(age)
    if age >= 18:
        a1=True
        print("Eligible age")
    else:
        a1=False
        print("Not eligible")
else:
    print("Invalid age")
if mobile.isdigit() and mobile.startswith(("6", "7", "8", "9")):
     m1=True
     print("Valid mobile number")
else:
     m1=False
     print("Invalid mobile number")

if n1 and a1 and m1:
    print("Registration successful")
else:
    print("Registration failed")