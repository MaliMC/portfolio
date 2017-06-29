grocery = []
keepAdding = True
add_or_subtract = True
while keepAdding:
    groceryItem = input("Enter item to add to the grocery list:")
    grocery.append(groceryItem)

    #Check if the user wants to keep adding
    addMoreItems = input("Do you want to add or subtract items from your list? Y/N")
    if addMoreItems == "Y":
        keepAdding = False
        add_or_subtract = True
    else:
        keepAdding = False
        add_or_subtract = False
while add_or_subtract:
    add_or_subtract = input("Would you like to Add or Subtract? A/S")
    if add_or_subtract == "A":
        groceryItem = input("Enter item to add to the grocery list:")
        grocery.append(groceryItem)
        keep_going = input("Would you like to keep adding? Y/N")
        if keep_going == "N":
            add_or_subtract = False
        else:
            print(" ")
    elif add_or_subtract == "S":
        remove_item = input("Which item would you like to remove?")
        grocery.remove(remove_item)
        keep_going = input("Would you like to keep subtracting? Y/N")
        if keep_going == "N":
                add_or_subtract = False
        else:
            print(" ")
    else:
        print("I'm not sure what you want to do, type either 'A' or 'S'")

print("This is my entire grocery list: ", grocery)
print("Here is my ", grocery,"list")
print("The first item of my grocery list is ", grocery[0])

for item in grocery:
    print (item)
print("Your grocery list has items", len(grocery))
