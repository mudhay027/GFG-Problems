class Solution:
    def maxSubarraySum(self, arr):
        maxi = float('-inf')
        sum = 0
        for i in arr:
            sum += i
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxi