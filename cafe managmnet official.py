print("welcome to Online Drink Order by MAYURI CAFE")
name = input("Please enter your name:")
print(f"what would you like to Drink,{name}? \n\nHERE IS OUR MENU")

# items in menu
menu = {
    'water melon seasonal': 100,
    'pineapple-juice': 100,
    'mix-fruite-juice': 120,
    'orange-juice': 160,
    'cappucchino': 70,
    'expresso': 70,
    'rose-shake': 100,
    'black-current-shake': 100,
    'kitkat-shake': 130,
    'oreo-milk-shake': 140,
    'cold-coffee': 110,
    'cold-coffee-with-icecream': 130,
    'iced-cold-coffee': 120,
}


print(" water melon seasonal: rs100\npineapple-juice: rs100\nmix-fruite-juice: rs120\norange-juice: rs160\ncappucchino: " \
"rs70\nexpresso: rs70\nrose-shake: rs100\nblack-current-shake: rs100\nkitkat-shake: rs130\noreo-milk-shake: rs140\ncold-coffee: rs110\ncold-coffee-with-icecream: rs130\niced-cold-coffee: rs120  ")

order_total = 0
ordering = True 
selected_items = [] 

while ordering:
    item = input("\nEnter the name of item you would like to drink (or 'done' to finish): ").lower()

    if item == 'done':
        ordering = False
        continue 

    if item in menu:
       
        order_total += menu[item]
       
        selected_items.append(item) 
        print(f" Your item **{item} (Rs{menu[item]})** has been added to your order.")
        print(f"Current total is **Rs{order_total}**.")
    else:
        print(f" Your selected item **{item}** does not exist in our menu. Please check the spelling.")


    another_order = input("Do you want to add another item? (Yes/No): ").lower()
    if another_order != "yes":
        ordering = False


print("\n--- ORDER SUMMARY ---")
print(f"Hello, **{name}**.")
print("You ordered the following items:")
for drink in selected_items:
    
    print(f"- {drink.title()}: Rs{menu[drink]}")
print("---")
print(f"The Final Total amount to PAY is **Rs{order_total}**.")
print("Thank you for ordering with MAYURI CAFE!")

