def highest_grade_student(input_path, output_path):
    with open(input_path) as f:
        lines = f.readlines()
    students = [line.strip().split(',') for line in lines]
    students = [(name, int(grade)) for name, grade in students]
    top_student = max(students, key=lambda x: x[1])
    
    result = f"Bahosi eng yuqori o‘quvchi: {top_student[0]} - {top_student[1]}"
    with open(output_path, 'w') as f:
        f.write(result)
    print(result)
