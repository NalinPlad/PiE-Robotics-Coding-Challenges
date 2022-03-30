def can_cheese_followup(small, small_size, big, big_size, goal) -> bool:
    if small_size == 0: smalls = 0
    else: smalls = min(goal//small_size, small)

    if big_size == 0: bigs = 0
    else: bigs = min((goal-(smalls*small_size))//big_size, big)

    while 1:
        total = (smalls*small_size) + (bigs*big_size)
        if total != goal:
            if smalls == 0:
                return False
            smalls -= 1
            if total < goal:
                if bigs == big:
                    return False
                bigs += 1
        else:
            return True