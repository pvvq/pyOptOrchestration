import target


# Relative Improvement Percentage
def RIP(old, new):
    return (new - old) / old

def BE():
    # switches of optimizations, 1 means on, 0 means off
    B = [1] * n_opt
    
    # get baseline execution time
    separator = ' '
    flags = separator.join(opts)
    target.compile(flags)
    target.exec()
    baseline_time = target.time()

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


opts = target.get_opts()
n_opt = len(opts)
print("Avail optimizations: \n", opts, "\n")

BE()