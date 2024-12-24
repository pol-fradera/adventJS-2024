def organizeShoes(shoes):
    organized = {}
    for shoe in shoes:
        shoe_type = shoe['type']
        shoe_size = shoe['size']
        
        if shoe_type not in organized:
            organized[shoe_type] = []
        
        organized[shoe_type].append(shoe_size)
    
    # Find pairs of shoes with the same size
    pairs = []
    for size in organized.get('I', []):
        if size in organized.get('R', []):
            pairs.append(size)
            organized['R'].remove(size)
    
    return pairs