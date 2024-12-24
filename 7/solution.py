def fix_packages(packages):
	if not packages:
		return ''
	if len(packages) == 1:
		return packages
	if packages[0] == '(':
		if packages[-1] == ')':
			return fix_packages(packages[1:-1])[::-1]
		else:
			return fix_packages(packages[:-1]) + packages[-1]
	return packages[0] + fix_packages(packages[1:]) 