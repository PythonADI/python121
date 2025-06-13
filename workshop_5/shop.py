shop = [
    ["Health Potion", 25],
    ["Mana Potion", 30],
    ["Sword", 100],
    ["Shield", 200],
    ["Invisibility Potion", 50]
]


# print(shop)

for item in shop:
    print(f"{item[0]} costs {item[1]}")
    # print(item)

removed_item = shop.pop()
print(f"we are out of {removed_item[0]}")
# shop.remove("Invisibility Potion")
