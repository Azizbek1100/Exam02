def max_number(input_path, output_path):
    with open(input_path) as f:
        numbers = list(map(int, f.readlines()))
    maximum = max(numbers)
    with open(output_path, 'w') as f:
        f.write(f"Eng katta son: {maximum}")
    print(f"Eng katta son: {maximum}")

max_number('Input/numbers.txt', 'Output/output09.txt')