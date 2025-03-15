def minimum_net_price(stockPrices):
    n = len(stockPrices)
    if n < 2:
        return 0  # If there's less than 2 prices, the net price is trivially 0

    # Step 1: Calculate the total sum of stockPrices
    total_sum = sum(stockPrices)
    
    # Initialize variables
    min_net_price = float('inf')
    current_sum = 0
    
    # Step 2: Iterate through the list to compute net prices
    for i in range(1, n):
        current_sum += stockPrices[i - 1]
        first_avg = round(current_sum / i)
        second_avg = round((total_sum - current_sum) / (n - i))
        net_price = abs(first_avg - second_avg)
        min_net_price = min(min_net_price, net_price)
    
    return min_net_price

stockPrices = [10, 20, 15, 30, 25]
stockPrices = [1, 3, 2, 4, 5]
result = minimum_net_price(stockPrices)

 # Output will be the minimum net price
print(f"Result: {result}")