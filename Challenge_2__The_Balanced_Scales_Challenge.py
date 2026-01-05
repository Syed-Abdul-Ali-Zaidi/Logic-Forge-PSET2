def can_balance_scales(arr : list):
    S = sum(arr)
    if S % 2 != 0:
        return False
    count = 0
    half_weight = S/2
    for i in arr:
        if count + i <= half_weight:
            count += i
    if count == half_weight:
        return True
    return False
