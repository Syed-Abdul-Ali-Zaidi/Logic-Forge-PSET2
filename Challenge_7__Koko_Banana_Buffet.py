def calculate_minimum_speed(piles : list,k : int):
    Min = 1
    Max = max(piles)
    while Min != Max:
        speed = (Min + Max) // 2
        total_hours = 0
        for pile in piles:
            hrs_per_pile = (pile + speed - 1) // speed # Finding ceiling of pile/speed
            total_hours += hrs_per_pile
        if total_hours <= k:
            Max = speed
        else:
            Min = speed + 1
    return Max

# Done!
# Piles = [5, 10, 15, 20]
# k = 7
# Output = calculate_minimum_speed(Piles,k)
# print("Piles:",Piles)
# print("K:",k)
# print("Output:",Output)