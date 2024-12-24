def fix_packages(packages):
  while '(' in packages:
        start = packages.rfind('(')
        end = packages.find(')', start)
        packages = packages[:start] + packages[start+1:end][::-1] + packages[end+1:]
  return packages