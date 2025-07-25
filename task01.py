def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Xatolik: 0 ga bo‘lish mumkin emas"

result = multiply(8, 5)
print("Natija:", result)