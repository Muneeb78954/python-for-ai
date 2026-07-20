def greeting():
    print("hello world")
    pass
greeting()

def check_wheather():
    temperature = 45
    if temperature > 40:
        print("Its a very hot day buddy.")
    elif temperature > 30:
        print("Its a hot day buddy.")
    else:
        print("Its a cold day buddy.")

check_wheather()

def Greet(name):
    print(f"Hello {name}, Nice to meet you {name}! \n I am Your AI assistant. How are you? ")

Greet(name="John")
Greet(name="Alice")

def calculate_total(price, tax_rate, discount):
    tax_amount = price * tax_rate
    total_price = price + tax_amount - discount
    print(f"Total Price: {total_price}")

calculate_total(price=100, tax_rate=0.1, discount=0)

# Returning values from functions
def calculate_total_price(price, tax_rate, discount):
    tax_amount = price * tax_rate
    total_price = price + tax_amount - discount
    return total_price

calculate_total_price(price=100, tax_rate=0.1, discount=0)


def area(length, width):
    area = length * width
    return area

result = area(length=10, width=5)
print(f"Area: {result}")