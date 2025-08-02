#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        first = 0
        last = 0
        sum = 0
        for last in range(len(arr)):
            sum += arr[last]
            while sum > target and first <= last:
                sum = sum - arr[first]
                first += 1
            if sum == target:
                    return [first+1,last+1]
        return [-1]
                