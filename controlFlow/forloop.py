# Prompt the user to enter their marks
marks = int(input("Enter your marks: "))

# Define the grade ranges and corresponding grades
grade_ranges = [(90, 100, "A+"), (80, 90, "A"), (70, 80, "B"), (60, 70, "C"), (50, 60, "D"), (40, 50, "E")]

# Iterate through the grade ranges and find the corresponding grade
grade = "F"  # Default grade if not found in any range
for lower, upper, letter_grade in grade_ranges:
    if marks >= lower and marks < upper:
        grade = letter_grade
        break  # Exit the loop once the grade is found

# Print the grade
print("Your grade is:", grade)
