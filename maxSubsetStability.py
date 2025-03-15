MOD = 10**9 + 7

def max_stability(availability, reliability):
    n = len(availability)
    
    # Initialize dp table with zeros
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize auxiliary table for minimum availability
    min_avail = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        min_avail[i][1] = availability[i - 1]
    
    # Iterate through all servers
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # Calculate minimum availability for subset of size j ending at i
            min_avail[i][j] = min(min_avail[i - 1][j], availability[i - 1])
            
            # Calculate dp[i][j] by either including the i-th server or not
            dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - 1] + reliability[i - 1]) * min_avail[i][j] % MOD)
    
    # Find the maximum stability across all subsets
    max_stab = 0
    for j in range(1, n + 1):
        max_stab = max(max_stab, dp[n][j])
    
    return max_stab

# Example usage:
availability = [5, 3, 2]
reliability = [10, 20, 30]
result = max_stability(availability, reliability) # Example input


print(f"Result: {result}")