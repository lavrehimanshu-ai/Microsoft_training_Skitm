# Marksheet Program
name = input("Enter student name: ")
subjects = ["English", "Maths", "Science", "Computer", "Hindi"]
total = 0
for subject in subjects:
    marks = float(input("Enter marks in " + subject + ": "))
    total += marks

percentage = total / len(subjects)
print("\n----- MARKSHEET -----")
print("Name:", name)
print("Total Marks:", total, "out of", len(subjects) * 100)
print("Percentage:", percentage, "%")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
