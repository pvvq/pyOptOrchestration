import target


# Relative Improvement Percentage
def RIP(old, new):
    return (new - old) / old

# Batch Elimination
def BE():
    # get baseline execution time
    separator = ' '
    flags = separator.join(opts)
    target.compile(flags)
    target.exec()
    baseline_time = target.time()

    # turn off each optimization to test whether it has neagtive effect
    negative_indices = [0] * n_opt
    for off in range(n_opt):
        local_opts = [opts[i] for i in range(n_opt) if i != off]

        flags = separator.join(local_opts)
        target.compile(flags)
        target.exec()
        local_time = target.time()

        # if RIPb < 0, this flag has negative effect
        if local_time < baseline_time:
            negative_indices[off] = 1

    # select optimization with non-negative effects
    result = [opts[index] for index in range(n_opt) if negative_indices[index] == 0]
    print("optimization choosen with BE method is :\n", result, "\n")

# Iterative Elimination
def IE():
    # get baseline execution time
    separator = ' '
    flags = separator.join(opts)
    target.compile(flags)
    target.exec()
    baseline_time = target.time()
    target.record("T_baseline", baseline_time)

    B = [1] * n_opt

    while True:
        # list of indexes of optimizations which are still enabled
        S = [index for index in range(len(B)) if B[index] == 1]
        if len(S) <= 0:
            break
        times = []
        # turn each off to find effect of each optimization
        for off in S:
            local_opts = [opts[i] for i in S if i != off]

            flags = separator.join(local_opts)
            target.compile(flags)
            target.exec()
            times.append(target.time())

        most_negative = min(times)
        target.record("most_neg_"+str(S[times.index(most_negative)]), most_negative)
        # if all in S have non-negative effects, finish
        # otherwise remove the most negative effect optimization
        if most_negative >= baseline_time:
            break
        else:
            B[S[times.index(most_negative)]] = 0

    # select optimizations which are still enable
    result = [opts[index] for index in range(n_opt) if B[index] == 1]
    print("optimization choosen with IE method is :\n", result, "\n")

# Combined Elimination
def CE():
    # get baseline execution time
    baseline_time = target.measure(opts)
    target.record("T_baseline", baseline_time)

    B = [1] * n_opt

    def get_enable(exclude=None):
        result = [opts[index] for index, enable in enumerate(B) if enable == 1]
        if exclude != None:
            result.pop(exclude)
        return result

    while True:
        # list of optimizations which are still enabled
        S = get_enable()
        if len(S) <= 0:
            break
        times = []
        # turn each off to find effect of each optimization
        for off in S:
            local_opts = S.copy()
            local_opts.remove(off)
            times.append(target.measure(local_opts))
        print(times)

        sorted_time = sorted(enumerate(times), key=lambda x:x[1])
        # if all in S have non-negative effects, finish
        if sorted_time[0][1] >= baseline_time:
            break
        else:
            # negative optimizations
            X = [S[i] for i, time in sorted_time if time < baseline_time]
            # remove most negetive optimization
            target.record(X[0], sorted_time[0][1])
            B[opts.index(X[0])] = 0
            X.pop(0)

            # then test all other negetive optimization in order,
            # if they are still negetive, remove them
            for l in X:
                local_opts = X.copy()
                local_opts.remove(l)
            
                local_time = target.measure(local_opts)
                if local_time >= baseline_time:
                    continue
                else:
                    B[opts.index(l)] = 0
                    target.record(l, local_time)

    # select optimizations which are still enable
    result = get_enable()
    print("optimization choosen with CE method is :\n", result, "\n")

opts = target.get_opts()
n_opt = len(opts)
print("Avail optimizations: \n", opts, "\n")

CE()