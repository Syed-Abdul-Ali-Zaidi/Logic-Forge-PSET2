def maximize_freelance_profit(deadlines, profits):
    n  = len(deadlines)

    # Making pairs of [deadline, job]
    jobs = []
    for i in range(n):
        jobs += [[ deadlines[i], profits[i] ]]

    # Sorting pairs in Desc wrt Profit
    jobs.sort(key=lambda x: x[1], reverse=True)

    Profits = 0
    Job_count = 0
    Max_deadline = max(i[0] for i in jobs)
    slots = [False]  * Max_deadline

    for job in jobs:
        deadline = job[0] - 1   # "-1" for indexing purpose
        for j in range(deadline,-1,-1):
            if slots[j] == False:
                slots[j] = True
                Profits += job[1]
                Job_count += 1
                break

    return f'[{Job_count} Jobs, {Profits} Profit]'

# # Done!
# Deadlines = [2, 1, 2, 1, 1]
# Profits = [100, 19, 27, 25, 15]
# Output = maximize_freelance_profit(Deadlines,Profits)
# print("Deadlines:",Deadlines)
# print("Profits:",Profits)
# print("Output:",Output)