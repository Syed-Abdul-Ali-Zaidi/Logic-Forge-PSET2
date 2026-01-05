def find_longest_mirror_length(s : str):
    L = 0
    R = len(s) - 1
    if L == R:
        return 1
    if s[L] == s[R]: # True if first and last character is same
        lenght = find_longest_mirror_length(s[L + 1: R])
        return lenght + 2

    # First and last are not same so:
    # Droping last character and checking again
    left_length = find_longest_mirror_length(s[L: R])

    # Droping first character and checking again
    right_length = find_longest_mirror_length(s[L+1 : R+1 ])

    # Taking largest palindrome
    if left_length > right_length:
        return left_length
    return right_length
