def draw_race(indices, length):
  race = []
  lane = list('~' * length)
  for i, position in enumerate(indices):
    current_lane = lane.copy()
    if position != 0:
      current_lane[position] = 'r'
    current_lane.append(f' /{i+1}')
    current_lane.append('\n')
    race.extend([' '] * (len(indices) - (i+1)))
    race.extend(current_lane)
  return ''.join(race)