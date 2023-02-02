def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    count = 0
    for first, last in permanence_period:
        if (first is None or last is None) or (
            not type(first) is int or not type(last) is int
        ):
            return None
        if first <= target_time <= last:
            count += 1
    return count
