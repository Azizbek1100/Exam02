import json

with open('Input/students.json', 'r') as file:
    data = json.load(file)

names = sorted(student['name'] for student in data)
output = {'sorted_names': names}

with open('Output/output12.json', 'w') as file:
    json.dump(output, file, indent=2)

print(json.dumps(output, indent=2))
