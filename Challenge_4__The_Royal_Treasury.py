def count_payment_combinations(coins, total_sum):
    arr = []
    coin_count = len(coins)
    for i in range(coin_count): # Creating 2D_arr where cols = 0 to total_sum & rows = no._of_coins
        arr += [[0 for j in range(total_sum+1)]]

    for i in range(coin_count):
        arr[i][0] = 1   # for total_sum=0 there will be always 1 way no matter what the coin is.
        for j in range(1,total_sum+1):
            if coins[i] > j:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-coins[i]]

    # Bottom_right element of 2D_arr will be the answer
    return arr[coin_count-1][total_sum]

# Done!
print(count_payment_combinations([2],3))