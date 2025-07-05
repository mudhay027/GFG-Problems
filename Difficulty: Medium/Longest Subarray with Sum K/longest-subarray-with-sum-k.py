# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):
        dict1={0:-1}
        sm,ans=0,0
        for i in range(len(arr)):
            sm+=arr[i]
            if sm-k in dict1:
                ans=max(ans,i-dict1[sm-k])
            if sm not in dict1:
                dict1[sm]=i
        return ans
'''
    def longestSubarray(self, arr, k):  
        right = 0
        left = 0
        n = len(arr)
        sum = arr[0]
        Max = 0
        while right < n:
            while ((left<=right) and (sum >k)):
                sum -= arr[left]
                left+=1
            if sum == k:
                Max = max(Max,right-left+1)
            right+=1
            if (right < n):
                sum += arr[right]
        return Max
        
'''

        
    
