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


n = 45
print('Steps =',n)

import time
start_time = time.perf_counter()  # Record start
ways = count_ways_to_summit(5)
end_time = time.perf_counter()    # Record end
elapsed_time = end_time - start_time

print('Number of ways =',ways)
print(f"Time taken: {elapsed_time} seconds")