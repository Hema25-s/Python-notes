
f_name = input("Enter your name: ")
l_name = input("Enter your name: ")
address = input("Enter your address: ")
gmail = input("Enter your Gmail: ")
phone_no = input("Enter your phone number: ")
skills = input("Enter your skills: ")
experience = input("Enter your experience: ")
certificate = input("Enter your certificate: ")
professional_summary = input("Enter your professional summary: ")



if f_name.isalpha():
    print("Name is valid")
else:
    print("Name is invalid")

if l_name.isalpha():
    print("Name is valid")
else:
    print("Name is invalid")    


if gmail.endswith(".com"):
    print("Gmail ends with .com")
else:
    print("Gmail is invalid")

if "@" in gmail:
    print("Gmail contains @")
else:
    print("Gmail does not contain @")


if "+91" in phone_no:
    print("Phone number contains +91")
else:
    print("Phone number does not contain +91")



r = professional_summary.lower() + skills.lower() + certificate.lower() + experience.lower() 

data_analytics = r.count("data analytics")
data_cleaning = r.count("data cleaning")
summary = r.count("summary")
visual = r.count("visual")
ml_algorithm = r.count("ml algorithm")
dl_algorithm = r.count("dl algorithm")



def make_resume():

    resume = f"""
====================================================
                    RESUME
====================================================

                 {name.capitalize()}
            {address}{gmail}{phone_no}

----------------------------------------------------
PROFESSIONAL SUMMARY
----------------------------------------------------

{professional_summary}

----------------------------------------------------
SKILLS
----------------------------------------------------

{skills}

----------------------------------------------------
EXPERIENCE
----------------------------------------------------

{experience}

----------------------------------------------------
CERTIFICATIONS
----------------------------------------------------

{certificate}

----------------------------------------------------
AI / ML KEYWORDS
----------------------------------------------------

Data Analytics  : {data_analytics}
Data Cleaning   : {data_cleaning}
Summary         : {summary}
Visual          : {visual}
ML Algorithm    : {ml_algorithm}
DL Algorithm    : {dl_algorithm}

====================================================
"""

    return resume

for i in range(1, 11):

    print("RESUME", i)
    print(make_resume())



total = data_analytics + data_cleaning + summary + visual
total = total + ml_algorithm + dl_algorithm 

ats_score = (total / 7) * 100

print("ATS SCORE :", round(ats_score, 2), "%")