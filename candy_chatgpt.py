# Solution from chatgpt
def max_candy(grid):
    m = len(grid) # number of rows
    n = len(grid[0]) # number of columns

    # Initialize the memo table with the same values as the bottom row of the grid
    memo = [list(row) for row in grid[-1:]]


    # Fill in the memo table by working our way up from the second-to-last row
    for i in range(m-2, -1, -1):
        for j in range(n):
            # Calculate the maximum number of candy pieces that can be collected 
            # from the next house by taking the maximum of the three possible 
            # moves from the next row's corresponding houses, plus the value of      
            # the current house.
            candy = grid[i][j] + max(
                memo[-1][j],
               memo[-1][max(j-1, 0)],
                memo[-1][min(j+1, n-1)]
            )

            # Store the maximum number of candy pieces in the table for this house
            memo.insert(0, [candy])

    # Find the max collection by checking the values in the top row of the table
    max_candy = max(memo[0])
    return max_candy