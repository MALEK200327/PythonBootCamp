# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

total=0
numberOfS=0
for n in student_heights:
  total+=n
  numberOfS+=1

average = round(total/numberOfS)
print(f"total height = {total}")
print(f"number of students = {numberOfS}")
print(f"average height = {average}")