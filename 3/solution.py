def organizeInventory(inventory):
  organized_inventory = {}
  for gift in inventory:
    organized_inventory[gift['category']] = {}

  for gift in inventory:
    previous_quantity = organized_inventory[gift['category']].get(gift['name'], 0)
    organized_inventory[gift['category']][gift['name']] = previous_quantity + gift['quantity']
  return organized_inventory