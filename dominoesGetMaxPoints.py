def solve(domino, remove, min_order):
    n = len(domino)
    removed_at = [0] * n
    dp = [0] * n
    
    for i in range(n):
        removed_at[remove[i]] = i

    def length_of_lis(moves):
        ans = 0
        for i in range(n):
            if removed_at[i] < moves:
                continue
            x = domino[i]
            left, right = -1, ans
            while right - left > 1:
                mid = (right + left) // 2
                if dp[mid] >= x:
                    right = mid
                else:
                    left = mid
            dp[right] = x
            ans = max(ans, right + 1)
        return ans
    
    if length_of_lis(0) < min_order:
        return -1
    
    left, right = 0, n
    while right - left > 1:
        mid = (right + left) // 2
        if length_of_lis(mid) >= min_order:
            left = mid
        else:
            right = mid
    
    return left

# Test case
dominoes = [4,5,58,5,4]#[1,2,3,4] #[1,4,4,2,5,3]
remove = [1,0,2,3,4] #[3,2,1,0] #[2,1,4,0,5,3]
min_order = 1 #2 #3
val = solve(dominoes, remove, min_order)
print(val)
