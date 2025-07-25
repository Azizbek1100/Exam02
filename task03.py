def calculate_tax(salary):
    if salary > 5000000:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    return salary - tax

salary = 6000000
tax = calculate_tax(salary)
net = calculate_net_salary(salary)
print("Soliq:", int(tax))
print("Sof maosh:", int(net))