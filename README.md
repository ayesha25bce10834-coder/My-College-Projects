#  Online Drink Order by MAYURI CAFE

Project Title: Online Drink Order by MAYURI CAFE 
Chosen Domain: Retail & E-commerce 
Real-World Problem Identified: Wastage of 
‘time’ in actually going and purchasing. 
Project Objectives: Reduce time wastage and 
make the process less stressful  
Requirement Analysis and Technology 
Stack 


Functional Requirements: The Program first 
offers the user a variety of items and then generates 
the bill according to the user's chosen items. 
Technology Stack and Tools: 
Course Applied: Fundamentals of Python 
Programming  
Programming Language(s): Python 
Development Environment:Google Colab and VS CODE editor 
Top-Down Design and Modularisation: 


High-Level Architecture:  
The "MAYURI CAFE Online Drink Order System" consists 
of three main logical components: 
1. Initialization: This component sets up the 
application by defining the menu (a dictionary 
holding drink names and prices), and initializing 
variables like order_total (to 0) and selected_items 
(an empty list). 
2. Order Processing Loop: This is the interactive core. 
It repeatedly: 
Takes User Input: Prompts the user for a drink 
choice or to indicate they are "done". 
Validates Input: Checks if the entered drink 
exists in the menu. 
Updates Order: If valid, it adds the drink's 
price to order_total and the drink name to 
selected_items. 
Continues/Exits: Asks if the user wants to add 
more items or if they are "done," controlling 
the loop's continuation. 
3. Order Summary Output: Once the user is done 
ordering, this component takes the selected_items


Implementation, Testing, and 
Refinement: 
Key Implementation Details: The use of the 
.lower() method on the user input ensures that the 
system accepts items regardless of capitalisation 
e.g., 'Cappucchino' or 'cappucchino' 
Testing Strategy: The program was tested by 
making it use to many students around the campus 


Results and Validation: The program offers 
correct results; validation depends on the professor  
Future Scope and Improvements: Can be 
developed at a higher level by including all the items of 
the café and taking the project to a web level. 
and order_total to print a personalized, itemized 
bill.

# CODES
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
