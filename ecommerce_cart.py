def cal_total(cart_items):
    if not cart_items:
        return "cart is empty"
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        print(f"before discount price: {total}")
        total *= 0.9  # 10% discount applied
    return total

cart_items = {}
print(cal_total(cart_items)) 

cart_items1 = {
    'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 
    'Keyboard': 1500, 'Cell': 6000, 'Phone': 10000
}
print(cal_total(cart_items1)) 
