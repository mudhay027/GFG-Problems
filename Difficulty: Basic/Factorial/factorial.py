#User function Template for python3


class Solution:
    def factorial (self, n):
        a = 1
        for i in range(1,n+1):
            a = a * i
        return a