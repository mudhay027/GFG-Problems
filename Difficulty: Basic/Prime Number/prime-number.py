import math

class Solution:
    def isPrime (self, N):
        count = 0
        A = int(math.sqrt(N))
        for i in range(1,A+1):
            if N%i == 0:
                count+=1
                if (N/i) != i:
                    count+=1
        if count == 2:
            return "1"
        else:
            return "0"
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isPrime(N))
# } Driver Code Ends