def min_cancelled_bookings(intervals : list):
    # Sorting the Start Time
    intervals.sort(key= lambda x : x[0])

    previous_end_time = intervals[0][1]
    for i in range(1,len(intervals)):
        if intervals[i][0] < previous_end_time:
            intervals.pop(i)
    return intervals



min_cancelled_bookings([[1, 2], [2, 3], [3, 4], [1, 3]])