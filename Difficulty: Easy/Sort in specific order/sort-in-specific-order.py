#User function Template for python3

class Solution:
    def sortIt(self, arr):
        odd = [i for i in arr if i%2 != 0]
        even = [j for j in arr if j%2 == 0]
        odd.sort(reverse = True)
        even.sort()
        arr[:] = odd + even
        return arr
        
    
