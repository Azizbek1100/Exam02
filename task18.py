numbers = [
    {'value': 2}, 
    {'value': 3}, 
    {'value': 4}
]

squared_numbers = list(map(lambda x: {'value': x['value'] ** 2}, numbers))
print(squared_numbers)
