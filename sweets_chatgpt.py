def max_sweets_chatgpt(n, rating):
    dp = [0] * n  # Make list with N 0's in it
    dp[0] = rating[0]
    dp[1] = max(rating[0], rating[1])

    for i in range(2, n):  #  iterates over 2 ... N
        dp[i] = max(dp[i - 1], dp[i - 2] + rating[i])

    return dp[n - 1]


# Build up program from past results  => Dynamic programming

def max_sweets_class(ratings):
    if len(ratings) == 1:
        return ratings[0]
    
    best = [0] * len(ratings) # Makes an array with all zeroes in it


    best[-1] = ratings[-1]  # Base case (last item)
    best[-2] = max(ratings[-1], ratings[-2])  # Base case (second to last)

    # Fill in remaining spots, working right to left
    # Start at second from last, stop at index 0, going backwards
    for i in range(len(ratings) - 3, -1, -1):  # 
        best[i] = max(ratings[i] + best[i + 2],
                      best[i + 1])
        
    return best[0]

sweets = [3, 10, 12, 16, 4]
print(max_sweets_chatgpt(len(sweets), sweets))
print(max_sweets_class(sweets))