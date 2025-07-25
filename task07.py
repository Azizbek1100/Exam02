def calculate_total(cart):
    total = 0
    for item in cart.values():
        total += item['price'] * item['quantity']
    return total


cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
print("Umumiy summa:", calculate_total(cart))