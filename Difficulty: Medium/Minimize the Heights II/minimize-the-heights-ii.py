#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        arr.sort()
        n = len(arr)
        ans = arr[-1] - arr[0]
        maxi = arr[-1] - k
        mini = arr[0] + k
        for i in range(n-1):
            large = max(maxi,arr[i] + k)
            small = min(mini,arr[i+1]-k)
            if small < 0:
                continue
            ans = min(ans,large-small)
        return ans