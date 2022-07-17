def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    you_time = pontoon_distance/you_speed
    shark_time = shark_distance/shark_speed
    if dolphin:
        shark_time *= 2
    return "Alive!" if you_time < shark_time else "Shark Bait!"
