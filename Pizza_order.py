# ============================================
# PIZZA ORDER SYSTEM
# CS 1300 — Lecture 6 Lab
# ============================================
#Loop Lecture 5v2.md 2026-03-26
#2 / 9
# ----- Menu Data (do not modify) -----
sizes = ["Personal (8\")", "Medium (12\")", "Large (16\")", "Party (20\")"]
size_prices = [6.99, 9.99, 12.99, 16.99]
topping_names = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions",
"Sausage", "Bacon", "Extra Cheese", "Pineapple", "Beef"]
topping_price = 1.50 # each topping, any size
# ----- Order Storage -----
order_descriptions = [] # e.g., "Large Pepperoni, Mushrooms"
order_prices = [] # e.g., 15.99
# Your code goes below this line.
print("Welcome to the Pizza Shop!")

while True:

#Sizes
    print("===========================================")
    print("Pizza Sizes")
    print("===========================================")
    for i in range(len(sizes)):
        print(f"{i + 1}. {sizes[i]} - ${size_prices[i]:.2f}")
    print("===========================================")
    while True:
        size_Choice = input("Enter the corresponding number to the pizza size you want to order 1-4: ")
        if size_Choice in ["1", "2", "3", "4"]:
            size_index = int(size_Choice) - 1
            selected_size = sizes[size_index]
            base_price = size_prices[size_index]
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
#toppings
    selected_toppings = []

    print("These are the available toppings and their price is $1.50 each: ")
    for i in range(len(topping_names)):
        print(f"{i + 1}. {topping_names[i]}")

    while True:
        topping_Choice = input("Enter the corresponding number to the toppings you want to add to your pizza (1-9), or type 'done' when finished: ")
        if topping_Choice.lower() == "done":
            break
        elif topping_Choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            topping_index = int(topping_Choice) - 1
            selected_toppings.append(topping_names[topping_index])
        else:
            print("Invalid choice. Please enter a number between 1 and 9, or 'done' to finish.")

    pizza_price = base_price + (len(selected_toppings) * topping_price)

    if selected_toppings:
        pizza_description = f"{selected_size} Pizza with {', '.join(selected_toppings)}"
    else:
        pizza_description = f"{selected_size} Pizza with just cheese"

    order_descriptions.append(pizza_description)
    order_prices.append(pizza_price)
    while True:
        order_another = input("Would you like to order another pizza? (yes/no): ").strip().lower()
        if order_another == "yes" or order_another == "y":
            print()
            break
    
        elif order_another == "no" or order_another == "n":
            print()
            break
    
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")
    if order_another == "no" or order_another == "n":
        break
#order summary

if not order_descriptions:
        print("No pizzas ordered.")

else:
    valid_code = {"Student10": 0.10, "HALFOFF": 0.50,}
    discount_rate = 0.0
    attempts = 0
    max_attempts = 3

    print()
    while attempts < max_attempts:
        discount_code = input("Enter a discount code (or press Enter to skip): ")
        if discount_code == "" or discount_code == "NONE":
            break
        elif discount_code in valid_code:
            discount_rate = valid_code[discount_code]
            print(f"Discount code applied: {discount_rate * 100:.0f}% off")
            break
        else:
            print("Invalid discount code. Please try again.")
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                    print(f"You have {remaining_attempts} attempt(s) left.")
            else:
                print("No more attempts left. Proceeding without discount.")
            
subtotal = 0.0
for i in range(len(order_prices)):
    subtotal += order_prices[i]


print()
print("===========================================")
print("Order Receipt")
print("===========================================")

for i in range(len(order_descriptions)):
    print(f"{i + 1}. {order_descriptions[i]}")
    print(f"${order_prices[i]:>6.2f}")

print("===========================================")

subtotal = sum(order_prices) * (1 - discount_rate)
tax = subtotal * 0.07
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("===========================================")
    
max_price = max(order_prices)
max_index = order_prices.index(max_price)

print(f"The most expensive pizza is: {order_descriptions[max_index]} at ${max_price:.2f}")

for i in range(len(sizes)):
    count = 0
    for description in order_descriptions:
        if sizes[i] in description:
            count += 1
    print(f"{sizes[i]} pizzas ordered: {count}")

print("Thank you for your order!")


