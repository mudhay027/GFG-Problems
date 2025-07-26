from collections import deque
class Solution:
    def maxOfSubarrays(self, arr, k):
        deq = deque()
        ans = []
        for i in range(len(arr)):
            if deq and deq[0] == i-k:
                    deq.popleft()
            while deq and arr[deq[-1]] <= arr[i]:
                deq.pop()
            deq.append(i)
            if i>=k-1:
                ans.append(arr[deq[0]])
        return ans