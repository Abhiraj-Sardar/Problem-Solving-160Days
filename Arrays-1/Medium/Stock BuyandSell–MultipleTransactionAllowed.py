# Stock Buy and Sell – Multiple Transaction Allowed

# The cost of stock on each day is given in an array price[]. 
# Each day you may decide to either buy or sell the stock i at price[i], 
# you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

# Note: A stock can only be sold if it has been bought previously and multiple stocks cannot be held on any given day.

# Examples:

# Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
# Output: 865

# Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210. 
# Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655. Maximum Profit = 210 + 655 = 865.


# Input: prices[] = [4, 2, 2, 2, 4]
# Output: 2

# Explanation: Buy the stock on day 3 and sell it on day 4 => 4 – 2 = 2. Maximum Profit = 2.

# Constraints:
# 1 <= prices.size() <= 105
# 0 <= prices[i] <= 104


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        mp=0
        for i in range(len(prices)-1):
            profit=prices[i+1]-prices[i]
            
            if profit>0:
                mp=mp+profit
        
        return mp
        
        # TC=O(N)
        # SC=O(1)


#Alternative Approach

# Function to calculate the maximum profit
def maximumProfit(prices):
    n = len(prices)
    lMin = prices[0]  # Local Minima
    lMax = prices[0]  # Local Maxima
    res = 0
  
    i = 0
    while i < n - 1:
      
        # Find local minima
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        lMin = prices[i]
        
        # Local Maxima
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        lMax = prices[i]
      
        # Add current profit
        res += (lMax - lMin)
  
    return res

# Driver Code
if __name__ == "__main__":
    prices = [100, 180, 260, 310, 40, 535, 695]
    print(maximumProfit(prices))

#TC=O(N) cause the i to n in while loop , i's value increases only once. 
#Sc=O(1)