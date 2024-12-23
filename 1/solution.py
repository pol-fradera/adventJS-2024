def prepare_gifts(gifts):
	unique_gifts = list(dict.fromkeys(gifts))
	unique_gifts.sort()
	return unique_gifts


prepare_gifts([3,1,2,3,4,2,5])