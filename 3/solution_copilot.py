def organizeInventory(inventory):  
    organized = {}
    for item in inventory:
        category = item['category']
        name = item['name']
        quantity = item['quantity']
        
        if category not in organized:
            organized[category] = {}
        
        if name in organized[category]:
            organized[category][name] += quantity
        else:
            organized[category][name] = quantity
    
    return organized