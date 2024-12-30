from typing import List, Literal

def move_train(board: List[str], mov: Literal['U', 'D', 'R', 'L']) -> Literal['none', 'crash', 'eat']:
	for i, row in enumerate(board):
		engine_pos = row.find('@')
		if engine_pos != -1:
			n_row = i
			break
	if mov == 'U':
		n_row -= 1
	elif mov == 'D':
		n_row += 1
	elif mov == 'R':
		engine_pos += 1
	elif mov == 'L':
		engine_pos -= 1
	
	if n_row < 0 or n_row >= len(board):
		return 'crash'
	if engine_pos < 0 or engine_pos >= len(board[0]):
		return 'crash'
	element = list(board[n_row])[engine_pos]
	if element == 'o':
		return 'crash'
	if element == '*':
		return 'eat'
	return 'none'
			
board = [
  '·····',
  '*····',
  '@····',
  'o····',
  'o····'
]

print(move_train(board, 'R'))