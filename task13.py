import json

with open('Input/students.json', 'r') as file:
    data = json.load(file)

long_names = [student['name'] for student in data if len(student['name']) > 5]
output = {'long_names': long_names}

with open('Output/output13.json', 'w') as file:
    json.dump(output, file, indent=2)
    
print(json.dumps(output, indent=2))
