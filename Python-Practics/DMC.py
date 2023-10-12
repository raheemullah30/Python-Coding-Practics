# Input marks for English, Urdu, and Maths subjects
Student_Name = str(input("First enter your Name: "))

english = int(input("Enter your English subject marks here: "))
urdu = int(input("Enter your Urdu subject marks here: "))
maths = int(input("Enter your Maths subject marks here: "))

# Calculate the total marks and percentage
total_marks = 300
obtained_marks = english + urdu + maths
percentage = (obtained_marks / total_marks) * 100

# Display the percentage
print("Percentage:", percentage)
