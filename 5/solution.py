def organizeShoes(shoes):
	left_shoes = []
	right_shoes = []
	for shoe in shoes:
		if shoe['type'] == 'I':
			left_shoes.append(shoe['size'])
		elif shoe['type'] == 'R':
			right_shoes.append(shoe['size'])
	
	left_shoes.sort()
	right_shoes.sort()
	organized_shoes = []
	for left_shoe in left_shoes:
		for i, right_shoe in enumerate(right_shoes):
			if left_shoe == right_shoe:
				organized_shoes.append(left_shoe)	
				right_shoes.pop(i)
			elif left_shoe > right_shoe:
				right_shoes.pop(i)
			else:
				break
	return organized_shoes