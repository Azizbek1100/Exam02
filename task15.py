def highest_grade_student(input_path, output_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()[1:]

    students = []
    for line in lines:
        name, grade = line.strip().split(',')
        try:
            students.append((name, int(grade)))
        except ValueError:
            continue

    if students:
        top_student = max(students, key=lambda x: x[1])
        result = f"Bahosi eng yuqori o‘quvchi: {top_student[0]} - {top_student[1]}"
        with open(output_path, 'w') as f:
            f.write(result)
        print(result)

if __name__ == '__main__':
    highest_grade_student('Input/grades.csv', 'Output/output15.txt')