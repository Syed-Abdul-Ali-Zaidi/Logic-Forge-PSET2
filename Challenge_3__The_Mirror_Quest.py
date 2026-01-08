def find_longest_mirror_length(s : str):
    if len(s) == 0: # Basecase 1 when there is empty string
        return 0
    elif len(s) == 1: # Basecase 2 when there is only one character
        return 1

    L = 0
    R = len(s) - 1

    if s[L] == s[R]: # True if first and last character is same
        s = s[L + 1: R]
        length = find_longest_mirror_length(s)
        return length + 2

    # First and last are not same so:

    # Dropping last character and checking again
    left_s = s[L: R]
    left_length = find_longest_mirror_length(left_s)

    # Dropping first character and checking again
    right_s = s[L+1 : R+1]
    right_length = find_longest_mirror_length(right_s)

    # Taking largest palindrome
    if left_length > right_length:
        return left_length
    return right_length

# Done!
# word = 'bbabcbcab'
# length = find_longest_mirror_length(word)

# print(length)
