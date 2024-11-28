# Second Largest

# Given an array of positive integers arr[], return the second largest element from the array.
# If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
# Input: arr[] = [10, 5, 10]
# Output: 5
# Explanation: The largest element of the array is 10 and the second largest element is 5.
# Input: arr[] = [10, 10, 10]
# Output: -1
# Explanation: The largest element of the array is 10 and the second largest element does not exist.

# Constraints:
# 2 ≤ arr.size() ≤ 105
# 1 ≤ arr[i] ≤ 105

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        num1=num2=-1
        for i in arr:
            
            if num1<i:
                num2=num1
                num1=i
            elif num2<i and i!=num1:
                num2=i
        
        if num2==num1:
            return -1
        return num2
        
        # TC=O(N)
        # SC=O(1)
                



