'''Important you are not allowed to use the max or min functions. Use for loop'''
# Input a list of student scores
# student_scores = input().split()
student_scores = [75, 87, 78, 76, 66, 91, 84, 92]
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = int()
for i in student_scores:
    if highest_score < i:
        highest_score = i

print(f"The highest score in the class is: {highest_score}")
