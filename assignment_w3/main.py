print("\n=== Pet Grooming Service Calculator ===")
print("Enter service package: bath, trim, or full")
print("Type 'done' when finished selecting services\n")
s = 0.0
while True:
    a = input("Enter service package: ")
    if a == "done": break
    elif a == "bath":
        s += 15
        print(f"Price: $15.00\nCurrent total: ${s:.2f}")
    elif a == "trim":
        s += 25
        print(f"Price: $25.00\nCurrent total: ${s:.2f}")
    elif a == "full":
        s += 40
        print(f"Price: $40.00\nCurrent total: ${s:.2f}")
    else: print("Invalid service package. Please try again.\n")
print("\n=== Service Summary ===")
if s > 74:
    print(f"Subtotal: ${s:.2f}")
    print("Multi-Pet Discount: -$12.00")
    s -= 12
print(f"Final Total: ${s:.2f}")
print("Thank you for choosing our salon!")