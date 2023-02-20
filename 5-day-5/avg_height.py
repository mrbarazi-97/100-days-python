students_heights = input(
    'Please enter a list of height with space : \n').split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

# you can use sum() function instead , But we practice "for" loop
student_height_num = 0
for height in students_heights:
    student_height_num += 1


student_height_sum = 0
for height_sum in students_heights:
    student_height_sum += height_sum

height_avg = round(student_height_sum / student_height_num, 2)

print(f'you enter {student_height_num} student height')
print(f'Total height is {student_height_sum}')
print(f'The average of heights is {height_avg}')
