#  Online Drink Order by MAYURI CAFÉ 

Project Title: Online Drink Order by MAYURI CAFÉ 
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
Development Environment: VS CODE editor 
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
    print("welcome to Online Drink Order by MAYURI CAFE")
    name = input("Please enter your name:")
    print(f"what would you like to Drink,{name}? \n\nHERE IS OUR MENU")

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
