def count_ways_to_summit(n : int):
    if n <= 1:
        return 1

    a = 1
    b = 1
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return c


# Done!
# steps = 4
# ways = count_ways_to_summit(steps)
# print("Input:",steps)
# print("Output:",ways)