def in_box(box):
    for i in range(1, len(box) - 1):
        for j in range(1, len(box[i]) - 1):
            if box[i][j] == '*':
                return True
    return False