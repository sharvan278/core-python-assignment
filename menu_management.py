initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
initial_menu.append(add_item)
remove_item = "Salad"
if remove_item in initial_menu:
    initial_menu.remove(remove_item)
else:
    print(f"Item '{remove_item}' not found in the menu.")
print("Updated menu:", initial_menu)
check_item = "Pizza"
if check_item in initial_menu:
    print(f"Availability: '{check_item} is available'")
else:
    print(f"Availability: '{check_item} is not available'")

