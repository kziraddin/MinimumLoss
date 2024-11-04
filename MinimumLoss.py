#Seaching Algorithm

'''
Lauren has a chart of distinct projected prices for a house over the next several years. 
She must buy the house in one year and sell it in another, and she must do so at a loss. 
She wants to minimize her financial loss.

Example

price = 20,15, 8, 2, 12
Her minimum loss is incurred by purchasing in year 2 at price 1 = 15 and
reselling in year 5 at price 4 = 12. Return 15 - 12 = 3.

Function Description

Complete the minimumLoss function in the editor below.
minimumLoss has the following parameters):
• int priceln]: home prices at each year

Returns
• int: the minimum loss possible

Input Format
The first line contains an integer n, the number of years of house data.
The second line contains n space-separated long integers that describe each price i].

Constraints
• 25n≤2×105
• 1 ≤ priceli] ≤ 1016
• All the prices are distinct.
• A valid answer exists.

Subtasks
• 2≤ n ≤ 1000 for 50% of the maximum score.
Sample Input 0
3
5 10 3

Sample Output 0
2
Explanation O
Lauren buys the house in year 1 at price|0] = 5 and sells it in year 3 at
price 2] = 3 for a minimal loss of 5 - 3 = 2.

Sample Input 1
5
207825
Sample Output 1
2
Explanation 1
Lauren buys the house in year 2 at price 1] = 7 and sells it in year 5 at
price 4] = 5 for a minimal loss of 7 - 5 = 2.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    prices_with_index = [(p, i) for i, p in enumerate(price)]
    prices_with_index.sort()
    
    min_loss = float('inf')
    
    for i in range(1, len(prices_with_index)):
        current_price, current_index = prices_with_index[i]
        previous_price, previous_index = prices_with_index[i-1]
        
        if current_index < previous_index:
            loss = current_price - previous_price
            min_loss = min(min_loss, loss)
    return min_loss
    

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()

