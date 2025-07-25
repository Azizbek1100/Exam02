import json

def count_students(input_path, output_path):
    with open(input_path) as f:
        students = json.load(f)
    count = len(students)
    with open(output_path, 'w') as f:
        json.dump({"count": count}, f, indent=2)
    print(f"O‘quvchilar soni: {count}")

count_students('Input/students.json', 'Output/output11.json')