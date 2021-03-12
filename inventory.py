def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(str(v) + ' ' + str(k))
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, lootlist):
    for i in range(len(lootlist)):
        if lootlist[i] in inventory:
            inventory[lootlist[i]] = inventory[lootlist[i]] + 1
        else:
            inventory.setdefault(lootlist[i],1)
    return inventory

inventory = {'rope': 1, 'torches': 1, 'gold coins': 3, 'daggers': 5, 'arrows': 12, 'knives': 5}
dragonLoot = ['gold coins', 'daggers', 'gold coins', 'gold coins', 'ruby']
updatedInventory = addToInventory(inventory, dragonLoot)
displayInventory(updatedInventory)
print("Inventory updated.")