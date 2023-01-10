def fold_to(distance):
    if distance < 0:
        return None
    thickness = 0.0001
    folds = 0
    while thickness < distance:
        thickness *= 2
        folds += 1
    return folds
