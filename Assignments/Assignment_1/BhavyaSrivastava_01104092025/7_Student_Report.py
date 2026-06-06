# Student Report Program
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

english = float(input("Enter English Marks: "))
maths = float(input("Enter Maths Marks: "))
science = float(input("Enter Science Marks: "))
computer = float(input("Enter Computer Marks: "))
hindi = float(input("Enter Hindi Marks: "))

total = english + maths + science + computer + hindi

percentage = (total / 500) * 100

print("\n STUDENT REPORT-")
print("Name       :", name)
print("Roll No    :", roll_no)
print("English    :", english)
print("Maths      :", maths)
print("Science    :", science)
print("Computer   :", computer)
print("Hindi      :", hindi)
print("Total Marks:", total)
print("Percentage :", percentage, "%")