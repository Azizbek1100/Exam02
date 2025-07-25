import csv

count = 0
with open('Input/grades.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if len(row) >= 2 and row[1].isdigit() and int(row[1]) == 5:
            count += 1

with open('Output/output16.txt', mode='w', encoding='utf-8') as output_file:
    output_file.write(f"5 baho olganlar soni: {count}")
