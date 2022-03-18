def can_cheese(small: int, big: int, goal: int) -> bool: # whackalenso
    bigs = min(goal//5, big)
    return (goal - bigs*5) <= small