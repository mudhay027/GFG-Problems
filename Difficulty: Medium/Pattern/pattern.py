#User function Template for python3

class Solution:
    def printDiamond(self, N):
        for i in range(0,N):
            print(' '*(N-i-1),end = '')
            print('* '*(i+1))
        for j in range(N,0,-1):
            print(' '*(N-j),end = '')
            print('* ' * j)
            