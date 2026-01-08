def maximize_freelance_profit(deadlines, profits):
    n  = len(deadlines)
    jobs = []
    for i in range(n):
        jobs += [[ deadlines[i], profits[i] ]]
    jobs.sort()

    Profits = 0
    Job_count = 0
    Last_deadline = 0
    Max_deadline = jobs[-1][0]
    print(Max_deadline)
    for i in range(n-1,-1,-1):
        current_job = jobs[i]
        if Max_deadline != 0 and Last_deadline != 1:
            Profits += current_job[1]
            Job_count += 1
            Last_deadline = current_job[0]
            Max_deadline -= 1

    return f'[{Job_count} Jobs, {Profits} Profit]'