print("Welcome to Online Drink Order by MAYURI CAFE")
name = input("Please enter your name: ")
print(f"What would you like to drink, {name}? \n\nHERE IS OUR MENU")

# items in menu
menu = {
    'water melon seasonal': 100,
    'pineapple-juice': 100,
    'mix-fruite-juice': 120,
    'orange-juice': 160,
    'cappuccino': 70,
    'espresso': 70,
    'rose-shake': 100,
    'black-current-shake': 100,
    'kitkat-shake': 130,
    'oreo-milk-shake': 140,
    'cold-coffee': 110,
    'cold-coffee-with-icecream': 130,
    'iced-cold-coffee': 120,
    'mint mojito': 100,
    'pink panther': 130,
    'regular tea': 20,
    'masala tea': 25,
}

# MENU DISPLAY
print("""
************ MENU ************

Juices & Shakes
water melon seasonal: rs100
pineapple-juice: rs100
mix-fruite-juice: rs120
orange-juice: rs160
rose-shake: rs100
black-current-shake: rs100
kitkat-shake: rs130
oreo-milk-shake: rs140

Coffee
cappuccino: rs70
espresso: rs70
cold-coffee: rs110
cold-coffee-with-icecream: rs130
iced-cold-coffee: rs120

Mocktails
mint mojito: rs100
pink panther: rs130

Tea
regular tea: rs20
masala tea: rs25

*******************************
""")

order_total = 0
selected_items = []

while True:
    item = input("Enter the item you want to drink (or type 'done' to finish): ").lower()

    if item == "done":
        break

    if item in menu:
        order_total += menu[item]
        selected_items.append(item)
        print(f"{item} (Rs{menu[item]}) has been added to your order.")
        print(f"Current total: Rs{order_total}")
    else:
        print("Item not found in our menu. Please check spelling.")

# ORDER SUMMARY
print("\n--- ORDER SUMMARY ---")
print(f"Hello, {name}. You ordered:")

for drink in selected_items:
    print(f"- {drink}: Rs{menu[drink]}")

print("----------------------")
print(f"Final Amount to PAY: Rs{order_total}")
print("Thank you for ordering with MAYURI CAFE!")
