from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals.sort(key=lambda x: x[0]) 

    merged = [intervals[0]]
    for current in intervals[1:]:
        last_end = merged[-1][1]

        if current[0] <= last_end:
            merged[-1][1] = max(last_end, current[1])
        else:
            merged.append(current)
    return merged


