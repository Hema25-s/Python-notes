# part1
#1
name="Hema"
print(type(name))
age=21
print(type(age))
salary=25000.50
print(type(salary))
is_student=True
print(type(is_student))


#3
com=(type(33.3j))
print("33.3j=",com)


#5

a="100"
converted_a=int(a)
print(type(a),a)
print(type(converted_a),converted_a)




#part2

b="25"
converted_b=int(b)
print(type(b),b)
print(type(converted_b),converted_b)

c="45.67"
converted_c=float(c)
print(type(c),c)
print(type(converted_c),converted_c)

e=100
converted_e=float(e)
print(type(e),e)
print(type(converted_e),converted_e)

#13
f=True
converted_f=int(f)
print(type(f),f)
print(type(converted_f),converted_f)


f=False
converted_f=int(f)
print(type(f),f)
print(type(converted_f),converted_f)

#14


f=0
f2=1
converted_f=bool(f)
converted_f2=bool(f2)
print(type(f),f)
print(type(f2),f2)
print(type(converted_f),converted_f)
print(type(converted_f2),converted_f2)

#15


f="hello"
f2=""
converted_f=bool(f)
converted_f2=bool(f2)
print(type(f),f)
print(type(f2),f2)
print(type(converted_f),converted_f)
print(type(converted_f2),converted_f2)



#part3

#age=input("enter your age:")
converted_age=int(age)
print(type(age))
print(type(converted_age))

#salary=input("enter your salary:")
converted_salary=float(salary)
print(type(salary))
print(type(converted_salary))



#part4
k="python programming"
print(k.upper())
print(k.capitalize())
print(k.title())
print(k.count('i'))
print(k.strip())
print(k.startswith('p'))
print(k.endswith('i'))
print(k.__contains__('th'))
print(k.split(" "))

h="hello 123"
print(h.isalnum())
h="hello123"
print(h.isalnum())


h="12345"
h2="123.45"
h3="hello"
print(h.isdigit(),h)
print(h2.isdigit(),h2)
print(h3.isdigit(),h3)
print(h.isdecimal(),h)
print(h2.isdecimal(),h2)
print(h3.isdecimal(),h3)


#part5


name="hemasomu"
print(name[0])
print(name[-1])
print(name[5])


#part6

k="hemasomu"
print(k[0:4],k)
print(k[2:6])
print(k[4:8])

name = "hemasomukumar"
print(name[:6])
print(name[-1:])
print(name[-1:-10:-2])
print(name[::-1])
print(name[0:8:2])
print(name[::3])


#take the following information from the user
#firstname,lastname,add,gmail,phoneno,skills,expere,certificate,proffesionalsummary

# the check the following constrain
# digit, alpha, ends with .com, @ contains, +91 contains

#  AI/ML developer job
# count how may words are in your resume
# count data analysis, data cleaning , summary, visual, ml algorithm
# dl algorthim, model train


# --------------------------------------------------
#                     JOHN DOE
#        Erode, Tamil Nadu, India
#        john.doe@gmail.com | +91 98765 43210
# --------------------------------------------------

# PROFESSIONAL SUMMARY
# Motivated and detail-oriented professional with
# experience in Python, web development and database
# technologies...

# SKILLS
# • Python
# • HTML & CSS
# • SQL
# • JavaScript

# PROFESSIONAL EXPERIENCE

# Python Developer
# ABC Technologies
# 2024 - Present

# Developed Python applications and maintained
# database-driven web systems.

# Junior Developer
# XYZ Solutions
# 2022 - 2024

# Worked on web applications, debugging, testing
# and API integration.

# CERTIFICATIONS
# • Python Programming Certificate
# • Web Development Certificate
# • SQL Certification
