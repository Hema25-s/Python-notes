def make_resume():

    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    address = input("Enter Address: ")
    gmail = input("Enter Gmail: ")
    phone_no = input("Enter Phone Number: ")
    skills = input("Enter Skills: ")
    experience = input("Enter Experience: ")
    certificate = input("Enter Certificate: ")
    professional_summary = input("Enter Professional Summary: ")


    if first_name.isalpha():
           print("Name is in correct format")
    else:
        print("Invalid")

    if last_name.isalpha():
           print("Name is in correct format")
    else:
          print("Invalid")


    if "@" in gmail and gmail.endswith(".com"):
        print("user use @,.com")
    else:
        print("user not use @,.com")

    if "+91" in phone_no:
        print("user use +91")
    else:
        print("user not use +91")

     

    resume_text = (professional_summary.lower() +  skills.lower()  + experience.lower()+ certificate.lower())

    data_analysis = resume_text.count("data analysis")
    data_cleaning = resume_text.count("data cleaning")
    summary = resume_text.count("summary")
    visual = resume_text.count("visual")
    ml_algorithm = resume_text.count("ml algorithm")
    dl_algorithm = resume_text.count("dl algorithm")

    total_keywords = (data_analysis + data_cleaning+ summary+ visual + ml_algorithm + dl_algorithm )

    ats_score = total_keywords * 10

    if ats_score > 100:
        ats_score = 100

    
    resume = f"""
========================================================
                       RESUME
========================================================

                    {first_name.capitalize()} {last_name.capitalize()}
         {address}||{gmail}|| {phone_no}

--------------------------------------------------------
PROFESSIONAL SUMMARY
--------------------------------------------------------

{professional_summary}

--------------------------------------------------------
SKILLS
--------------------------------------------------------

{skills}

--------------------------------------------------------
EXPERIENCE
--------------------------------------------------------

{experience}

--------------------------------------------------------
CERTIFICATIONS
--------------------------------------------------------

{certificate}

--------------------------------------------------------
ATS KEYWORD CHECK
--------------------------------------------------------

Data Analysis : {data_analysis}
Data Cleaning : {data_cleaning}
Summary       : {summary}
Visual        : {visual}
ML Algorithm  : {ml_algorithm}
DL Algorithm  : {dl_algorithm}

--------------------------------------------------------
ATS SCORE : {ats_score}/100
--------------------------------------------------------

"""

    return resume



print(make_resume())

print("========== RESUME 1 ==========")
print(make_resume())

print("========== RESUME 2 ==========")
print(make_resume())

print("========== RESUME 3 ==========")
print(make_resume())

print("========== RESUME 4 ==========")
print(make_resume())

print("========== RESUME 5 ==========")
print(make_resume())

print("========== RESUME 6 ==========")
print(make_resume())

print("========== RESUME 7 ==========")
print(make_resume())

print("========== RESUME 8 ==========")
print(make_resume())

print("========== RESUME 9 ==========")
print(make_resume())

print("========== RESUME 10 ==========")
print(make_resume())