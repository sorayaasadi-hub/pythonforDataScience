
prices = {
    "rice": 75,
    "oil": 185,
    "sugar": 120,
    "milk": 95,
    "egg": 12,
    "flour": 65,
    "salt": 40,
    "lentil": 130,
    "potato": 45,
    "onion": 80,
    "tea": 250,
    "coffee": 450,
    "biscuit": 50,
    "soap": 70,
    "shampoo": 180
}

print("AVAILABLE PRODUCTS")

for item, price in prices.items():
    print(item, ":", price, "Tk")


order = {}


n = int(input("\nHow many order entries? "))

for i in range(n):

    item = input("Enter product: ").lower()
    quantity = int(input("Enter quantity: "))

    if item not in prices:
        print(item, "is not available.")

    elif quantity <= 0:
        print("Quantity must be positive.")

    else:
        order[item] = order.get(item, 0) + quantity


print("\nFINAL ORDER")
print(order)

bill = {}
subtotal = 0

for item, quantity in order.items():

    unit_price = prices[item]
    total = quantity * unit_price

    bill[item] = {
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    }

    subtotal = subtotal + total

if subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0


vat = (subtotal - discount) * 0.02

final_amount = subtotal - discount + vat

print("\n================ GROCERY SHOP BILL ================")

print(f"{'Item':<15}{'Quantity':>10}{'Unit Price':>15}{'Total':>12}")

print("-" * 52)

for item, details in bill.items():

    print(f"{item:<15}{details['quantity']:>10}"
          f"{details['unit_price']:>15.2f}"
          f"{details['total']:>12.2f}")

print("-" * 52)

print(f"{'Subtotal:':<35}Tk {subtotal:.2f}")
print(f"{'Discount (5%):':<35}Tk {discount:.2f}")
print(f"{'VAT (2%):':<35}Tk {vat:.2f}")

print("-" * 52)

print(f"{'Final amount:':<35}Tk {final_amount:.2f}")

print("=" * 52)
