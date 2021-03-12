def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + str(k))
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addItems):
    for k in range(len(addItems)):
        inventory.setdefault(addItems[k], 0)
        inventory[addItems[k]] += 1
    return(inventory)

inventory = {'rope': 1, 'torches': 1, 'gold coins': 3, 'daggers': 5, 'arrows': 12, 'knives': 5}
dragonLoot = ['gold coins', 'daggers', 'gold coins', 'gold coins', 'ruby']
updatedInventory = addToInventory(inventory, dragonLoot)
displayInventory(updatedInventory)
print("Inventory updated.")