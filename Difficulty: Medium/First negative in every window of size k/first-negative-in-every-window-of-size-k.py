#User function Template for python3
from collections import deque

class Solution:
    def firstNegInt(self, arr, k): 
        ans = []
        dq = deque()
        n = len(arr)
        for i in range(k):
             if arr[i] < 0:
                 dq.append(i)
        for i in range(k,n):
            if dq:
                ans.append(arr[dq[0]])
            else:
                ans.append(0)
            if dq and dq[0] == i-k:
                dq.popleft()
            if arr[i]<0:
                dq.append(i)
        if dq:
            ans.append(arr[dq[0]])
        else:
            ans.append(0)
        return ans
        
             