# Student details program
# Student Information
student_name = input("enter your name:")
age =int(input("enter the your age")) 
grade = input("enter the grade")
marks_math = int(input("enter the your maths marks")) 
marks_science = int(input("enter the your science marks")) 
marks_english =int(input("enter the your english marks")) 
total_marks = marks_math + marks_science + marks_english
average_marks = total_marks / 3
attendance = int(input("enter the your attendence percentage")) 
discipline_score = int(input("enter the your displine score of student ")) 

# Display student details
print(f"Student Name: \"{student_name}\"")
print(f"Age: \"{age}\" years old")
print(f"Grade: \"{grade}\"")
print(f"Math Marks: \"{marks_math}\"")
print(f"Science Marks: \"{marks_science}\"")
print(f"English Marks: \"{marks_english}\"")
print(f"Total Marks: \"{total_marks}\"")
print(f"Average Marks: \"{average_marks:.2f}\"")

# Check if student passed
if average_marks >= 50:
    print(f"\"{student_name}\" has passed.")
else:
    print(f"\"{student_name}\" has failed.")
# Check if student is eligible for scholarship
if average_marks > 80 and attendance > 75:
    print(f"\"{student_name}\" is eligible for a scholarship.")
else:
    print(f"\"{student_name}\" is not eligible for a scholarship.")
# Check discipline status
if discipline_score >= 8:
    print(f"\"{student_name}\" has excellent discipline.")
elif 5 <= discipline_score < 8:
    print(f"\"{student_name}\" has good discipline.")
else:
    print(f"\"{student_name}\" needs improvement in discipline.")
# Grade categorization
if average_marks >= 90:
    print(f"\"{student_name}\" has an \"A+\" grade.")
elif 80 <= average_marks < 90:
    print(f"\"{student_name}\" has an \"A\" grade.")
elif 70 <= average_marks < 80:
    print(f"\"{student_name}\" has a \"B\" grade.")
elif 60 <= average_marks < 70:
    print(f"\"{student_name}\" has a \"C\" grade.")
else:
    print(f"\"{student_name}\" has a \"D\" grade.")
# Bonus marks for discipline
if discipline_score == 10:
    total_marks += 5
    print(f"\"{student_name}\" received 5 bonus marks for excellent discipline.")
elif discipline_score >= 8:
    total_marks += 3
    print(f"\"{student_name}\" received 3 bonus marks for good discipline.")
# Final marks after bonus
average_marks = total_marks / 3
print(f"Final Total Marks after bonus: \"{total_marks}\"")
print(f"Final Average Marks after bonus: \"{average_marks:.2f}\"")
# Attendance warnings
if attendance < 75:
    print(f"Warning: \"{student_name}\" has low attendance.")
# Result Summary
if average_marks >= 50 and discipline_score >= 5 and attendance >= 75:
    print(f"\"{student_name}\" has successfully completed the academic year.")
else:
    print(f"\"{student_name}\" needs improvement to pass the academic year.")
