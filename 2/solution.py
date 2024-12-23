def createFrame(names):
  max_length = 0
  for name in names:
    max_length = max(max_length, len(name))

  frame = '*' * (max_length + 4) + '\n'
  for name in names:
    right_margin = max_length - len(name)
    frame += '* ' + name + ' ' * right_margin + '*\n'
  return frame + '*' * (max_length + 4)