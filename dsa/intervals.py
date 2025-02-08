# sorting overlapping intervals

def sort_interval_by_starttime(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


# mergining intervals
def merge_intervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    merged = []
        
    for interval in sortedIntervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
            print(merged)
        else:
            # overlape
            merged[-1][1] = max(interval[1], merged[-1][1])
    return merged

# Can attend meeting
# Write a function to check if a person can attend all the meetings scheduled without any time conflicts. Given an array intervals, where each element [s1, e1] represents a meeting starting at time s1 and ending at time e1, determine if there are any overlapping meetings. If there is no overlap between any meetings, return true; otherwise, return false.

# Note that meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.

# EXAMPLES
# Input:
# intervals = [(1,5),(3,9),(6,8)]

# Output:
# false

def check_meeting_overlap(intervals):  # O(n*logn)
    intervals.sort(key = lambda x:x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False  # has overlap in meeting
    return True  # no overlap in meeting




if __name__ == "__main__":
    res = merge_intervals([[1,5],[3,6],[4,9],[8,10],[15,18]])
    print(res)