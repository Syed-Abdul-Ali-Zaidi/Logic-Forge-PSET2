def maximize_freelance_profit(deadlines, profits):
    jobs = []
    for i in range(len(deadlines)):
        jobs += [[ deadlines[i], profits[i] ]]
    jobs.sort()
    print(jobs)