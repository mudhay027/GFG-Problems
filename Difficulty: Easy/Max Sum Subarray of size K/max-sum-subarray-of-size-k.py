#User function Template for python3
class Solution:
    def maximumSumSubarray (self,arr,k):
        n = len(arr)
        start = 0
        if n <= k:
            return sum(arr)
        Max_sum = sum(arr[0:k])
        maxi = Max_sum
        for i in range(1,n):
            if k == n:
                break
            start = arr[i-1]
            Max_sum = Max_sum - start + arr[k]
            maxi = max(maxi,Max_sum)
            
            k+=1
        return maxi