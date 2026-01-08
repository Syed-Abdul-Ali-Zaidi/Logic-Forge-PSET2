def min_cancelled_bookings(intervals : list):
    # Sorting w.r.t End Time
    intervals.sort(key= lambda x : x[1])

    previous_end_time = intervals[0][1]
    intervals_to_remove = 0
    for i in range(1,len(intervals)):
        if intervals[i][0] < previous_end_time:
            intervals_to_remove += 1
        else:
            previous_end_time = intervals[i][1]


    return intervals_to_remove

# Done!
