def countPossibleWinners(initialRewards):
    max_val, n = max(initialRewards), len(initialRewards)
    res, num_of_max = 0, 0
    for num in initialRewards:
        if num == max_val:
            num_of_max += 1
        else:
            if num + n  >= max_val + n-1:
                res += 1
    return res + num_of_max

initialRewards = [8, 10, 9]
val = countPossibleWinners(initialRewards)
print(val)