def average_grade(students):
    return sum(students.values()) / len(students)

def above_average_students(students):
    avg = average_grade(students)
    return [name for name, grade in students.items() if grade > avg]

students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}
avg = average_grade(students)
above = above_average_students(students)

print("O‘rtacha baho:", avg)
print("Yuqori baholilar:", ", ".join(above))