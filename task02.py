def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        return "Xatolik: yetarli mablag‘ yo‘q"

def check_balance(balance):
    return balance

balance = 100000
balance = deposit(balance, 50000)
print("Yangi balans:", balance)