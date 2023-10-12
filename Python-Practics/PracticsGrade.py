Student_Name = str(input("First enter your Name: "))
Student_Semester = int(input("Enter your Semester in integer(mean in number): "))
oops = int(input("Enter your oops subject marks here: >=100: "))
DLD = int(input("Enter your DLD subject marks here:>=100: "))
management_Science = int(input("Enter your management_Science subject marks here: >=100: "))

# Calculate the total marks and percentage
total_marks = 100*3
obtained_marks = oops + DLD+ management_Science
percentage = (obtained_marks / total_marks) * 100
print("total Marks: ", total_marks)
# Display the percentage
print("Percentage:", percentage)
obtained_marks = float(input("Enter your Percentage: "))

if obtained_marks >= 90:
    grade = "A+"
elif obtained_marks >= 80:
    grade = "A"
elif obtained_marks >= 70:
    grade = "B+"
elif obtained_marks >= 60:
    grade = "B"
elif obtained_marks >=55:
    grade = "C+"
elif obtained_marks >= 51:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)
