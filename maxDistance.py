def check(vl, b, n, d):
    cost = 0
    for i in range(n):
        cost += abs(b[i] - vl)
    cost *= 2
    return cost <= d
 
def main():
    n, d = map(int, input().split())
    b = list(map(int, input().split()))
 
    b.sort()
 
    count = 0
    u = left = low = high = right = id = 0
 
    if n % 2 != 0:
        u = 0
        left = b[n//2] - 1
        low = -1e9
        high = left
    else:
        u = 0
        id = (b[n // 2 - 1] + b[n // 2]) // 2
        left = id - 1
        low = -1e9
        high = left
 
    ans = 0
    while low <= high and u == 0:
        mi = (low + high) // 2
 
        if check(mi, b, n, d):
            if not check(mi - 1, b, n, d):
                ans = mi
                u = 1
            else:
                high = mi - 1
        else:
            low = mi + 1
 
    v1 = ans
 
    if n % 2 != 0:
        right = b[n//2]
        u = 0
        low = right
        high = 1e9
    else:
        u = 0
        right = (b[n // 2 - 1] + b[n // 2]) // 2
        low = right
        high = 1e9
 
    while low <= high and u == 0:
        mi = (low + high) // 2
        if check(mi, b, n, d):
            if check(mi + 1, b, n, d):
                low = mi + 1
            else:
                u = 1
                ans = mi
        else:
            high = mi - 1
 
    v5 = ans
    count = count + abs(v5 - v1) + 1
    print(count)
 
if __name__ == "__main__":
    main()
 