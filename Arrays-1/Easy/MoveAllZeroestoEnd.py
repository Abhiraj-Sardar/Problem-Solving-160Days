# Move All Zeroes to End

# Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place.

# Examples:

# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.

# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105


class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	i=0
    	n=len(arr)
    	count=0
        while i<n:
            
            if arr[i]!=0:
                arr[count]=arr[i]
                count+=1
            i+=1
        
        while count!=n:
            arr[count]=0
            count+=1
        
        return arr
            
        # TC=O(N)
        # SC=O(1)
