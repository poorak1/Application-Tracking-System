import re
import docx2txt
import pdfplumber
from tabulate import tabulate
def name_check(resume):  # Function to check the Person's name in resume
    if(re.search(r'\b[A-Za-z0-9._]+@[A-Za-z0-9.]+\.[A-Za-z]{2,}\b', resume)):
        return("Yes")
    else:
        return("No")
    
def mail_check(resume):  # Function to check whether the email entered is in the correct format
    if(re.search(r'\b[A-Z]+[a-z]+\s{1}+[A-Z]+[a-z]+', resume)):
        return("Yes")
    else:
        return("No")

def phone_check(resume): # Function to check whether phone number has the country code and 10 digits. 
    if(re.search(r'\+\d{2,3}+\s*\d{10}', resume)):
        return("Yes")
    else:
        return("No")

def education_check(resume): # Function to check the educational details are entered correctly or not. 
    edu = (re.search(r'\b\d{4}+\s+', resume)) and (re.search(r'institute|Institute|University|university', resume)) and (re.search(r'\b\d{2}\.+.+%+', resume))
    if(edu):
        return("Yes")
    else:
        return("No")

def experience_check(resume): # Function to check the desired work experience
    if((re.search(r'Experience|experience.*(A-Z)(a-z)+', resume)) and (re.search(r'\b\d{2}+', resume))):
        return("Yes")
    else:
        return("No")

def project_check(resume): # Function to check the project details
    if((re.search(r'\b[A-Z][a-z].*', resume)) and (re.search(r'\bProject|project.*', resume))):
        return("Yes")
    else:
        return("No")

def skill_check(resume):  # Function to check if skill section is mentioned or not
    if(re.search(r'\bskill|Skill.*', resume)):
        return("Yes")
    else:
        return("No")

file_location = input("Please enter the location/Path of the file: ")

if (re.search(r'.pdf', file_location)): # Condition to check whether the resume is in docx format or pdf
        with pdfplumber.open(file_location) as pdf:
            resume = ""
            for page in pdf.pages:
                resume += page.extract_text()
elif (re.search(r'.docx', file_location)):
        resume = docx2txt.process(file_location)
else:
        print("Unsupported file format. Only PDF and DOCX are supported.")

mydata = [          # Assigning data in table
	["1", "Name", name_check(resume)],
	["2", "E-mail", mail_check(resume)],
	["3", "Phone Number", phone_check(resume)],
	["4", "Educational Check", education_check(resume)],
    ["5", "Project Details", project_check(resume)],
    ["6", "Work Experience", experience_check(resume)],
    ["7", "Skills", skill_check(resume)]
]

head = ["S.No", "Resume Details", "Yes/No"]  # Creating header for the table

print(tabulate(mydata, headers=head, tablefmt="grid")) # displaying the results in table