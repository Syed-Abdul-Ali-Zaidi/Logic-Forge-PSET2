def min_cancelled_bookings(intervals : list):
    # Sorting w.r.t Start Time
    intervals.sort(key= lambda x : x[0])

    previous_end_time = intervals[0][1]
    intervals_to_remove = 0
    for i in range(1,len(intervals)):
        if intervals[i][0] < previous_end_time:
            intervals_to_remove += 1

    return intervals_to_remove


a =min_cancelled_bookings([[1, 2], [5, 10], [18, 35]])
print(a)