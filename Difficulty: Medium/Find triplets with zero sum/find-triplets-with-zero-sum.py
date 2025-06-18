class Solution:
    # Function to find triplets with zero sum.
    def findTriplets(self, arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                sum = arr[i]+arr[j]
                if (sum * -1) in arr[j+1:]:
                    return True
        return False
                
                
                
                
                
            