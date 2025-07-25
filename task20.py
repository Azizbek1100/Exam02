def shortest_named_student(students):
    return min(students, key=lambda s: len(s['name']))['name']

students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21},

]
print(shortest_named_student(students))