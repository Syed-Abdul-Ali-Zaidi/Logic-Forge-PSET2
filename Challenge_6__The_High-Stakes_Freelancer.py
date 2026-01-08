def maximize_freelance_profit(deadlines, profits):
    n  = len(deadlines)
    jobs = []
    for i in range(n):
        jobs += [[ deadlines[i], profits[i] ]]
    jobs.sort()

    Profits = 0
    Job_count = 0
    Last_deadline = 0
    for i in range(n-1,-1,-1):
        current_job = jobs[i]
        if current_job[0] != Last_deadline:
            Profits += current_job[1]
            Job_count += 1
            Last_deadline = current_job[0]

    return f'[{Job_count} Jobs, {Profits} Profit]'