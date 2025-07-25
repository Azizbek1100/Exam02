def sort_numbers(input_path, output_path):
    with open(input_path) as f:
        numbers = sorted(map(int, f.readlines()))
    with open(output_path, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")
    print("Saralangan sonlar:", numbers)
    
sort_numbers('Input/numbers.txt', 'Output/output10.txt')