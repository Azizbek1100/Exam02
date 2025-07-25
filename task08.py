def sum_numbers(input_path, output_path):
    with open(input_path) as f:
        numbers = list(map(int, f.readlines()))
    total = sum(numbers)
    with open(output_path, 'w') as f:
        f.write(f"Yig'indi: {total}")

    print("yig'indi")