def in_box(box):
	for i, row in enumerate(box):
		if (i == 0 or i == (len(box)-1)) and '*' in row:
			return False
		if '*' in (row[0], row[-1]):
			return False
		if '*' in row:
			return True
	return False