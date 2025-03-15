def min_error(s, x, y):
    n = len(s)
    
    # Initialize DP table
    # dp[i][j][k] represents the minimum errors up to index i with the last character being j (0 or 1)
    # and the count of errors being k (X or Y)
    dp = [[[float('inf')] * 2 for _ in range(2)] for _ in range(n + 1)]
    
    # Base case
    dp[0][0][0] = dp[0][1][0] = 0
    dp[0][0][1] = dp[0][1][1] = 0
    
    for i in range(1, n + 1):
        for j in range(2):
            ch = s[i - 1]
            if ch == '?':
                ch_0 = '0'
                ch_1 = '1'
            else:
                ch_0 = ch_1 = ch
            
            # Transition if the last character is '0'
            if ch_0 == '0':
                dp[i][0][0] = min(dp[i][0][0], dp[i - 1][0][0])
                dp[i][0][0] = min(dp[i][0][0], dp[i - 1][1][1] + y)  # error Y
                dp[i][0][1] = min(dp[i][0][1], dp[i - 1][0][1])
                dp[i][0][1] = min(dp[i][0][1], dp[i - 1][1][0] + x)  # error X
            
            # Transition if the last character is '1'
            if ch_1 == '1':
                dp[i][1][0] = min(dp[i][1][0], dp[i - 1][1][0])
                dp[i][1][0] = min(dp[i][1][0], dp[i - 1][0][1] + x)  # error X
                dp[i][1][1] = min(dp[i][1][1], dp[i - 1][1][1])
                dp[i][1][1] = min(dp[i][1][1], dp[i - 1][0][0] + y)  # error Y

    # Minimum of ending with '0' or '1' and considering both types of errors
    return min(dp[n][0][0], dp[n][0][1], dp[n][1][0], dp[n][1][1])

# Example usage:
s = "0?1??0"
x = 3
y = 2
min_errors = min_error(s,x,y)
print(f"Minimum errors: {min_errors}")
