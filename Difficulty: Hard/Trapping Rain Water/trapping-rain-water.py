
class Solution:
    def maxWater(self, arr):
        n = len(arr)
        left,right = 0, n-1
        res = 0
        maxLeft, maxRight = 0, 0
        
        while (left <= right):
            if arr[left] <= arr[right]:
                if arr[left] >= maxLeft:
                    maxLeft = arr[left]
                else:
                    res += maxLeft - arr[left]
                left+=1
            else:
                if arr[right] >= maxRight:
                    maxRight = arr[right]
                else:
                    res += maxRight - arr[right]
                right -= 1
                
        return res