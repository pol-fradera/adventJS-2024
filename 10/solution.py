def compile(instructions):
	registers = {}
	i = 0
	while i < len(instructions):
		items = instructions[i].split(' ')
		try:
			value = int(items[1])
		except ValueError:
			value = registers.get(items[1], 0)
		if items[0] == 'INC':
			registers[items[1]] = value + 1 
		elif items[0] == 'DEC':
			registers[items[1]] = value - 1 
		elif items[0] == 'MOV':
			registers[items[2]] = value
		elif items[0] == 'JMP' and value == 0:
			i = int(items[2])
			continue
		i += 1
	return registers['A']

instructions = [
  'MOV 5 B',
  'DEC B',
  'MOV B A',
  'INC A'
]
print(compile(instructions))