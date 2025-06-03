gold = int(input("How much money have you got? "))
# print(type(gold))

health_potion_price = 20
mana_potion_price = 30
sword_price = 75

print(f"Buying \"Health Potion\" will cost you {health_potion_price} gold")
print(f'Buying "Mana Potion" will cost you {mana_potion_price} gold')
print(f"Buying 'Sword' will cost you {sword_price} gold")
# print(f'Buying \'mana_potion\' will cost you {mana_potion_price} gold')

error_message = "You cannot purchase this item, you don't have gold for it!"

if gold == 0:
    print("You are a beggar! GET OUT OF MY STORE THIEFFF!")
else:
    if gold < health_potion_price:
        # indented code is called block
        print(error_message)
    else:
        gold -= health_potion_price
        print(f"You purchased Health potion for {health_potion_price} gold and you have left {gold} gold")

    if gold < sword_price:
        print(error_message, "Sword")
    else:
        gold -= sword_price
        print(f"You purchased Sword for {sword_price} gold and you have left {gold} gold")
