def create_xmas_tree(height, ornament):
	xmas_tree = ''
	for i in range(height):
		ornaments = ornament * (2 * i + 1)
		margin = height - i - 1
		xmas_tree += f"{' ' * margin}{ornaments}{' ' * margin}\n"
	margin = height - 1
	trunk = f"{margin * ' '}#{margin * ' '}"
	xmas_tree += f"{trunk}\n{trunk}"
	return xmas_tree