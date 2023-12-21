'''Important You should not use the sum() or len() functions in your answer.
You should try to replicate their functionality using what you have learnt about for loops.'''

# Input a Python list of student heights

# student_heights = input().split()

student_heights = "192 150 160 200"
student_heights = student_heights.split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_height = int()
students = int()
average_height = int()

for i in student_heights:
    total_height += i
    students += 1

average_height = total_height / students
print(f"total height = {total_height}")
print(f"number of students = {students}")
print(f"average height = {average_height:.0f}")
