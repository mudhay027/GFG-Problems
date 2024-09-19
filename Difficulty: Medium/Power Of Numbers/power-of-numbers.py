class Solution:
    def power(self,N,R):
        mod = 1000000007
        ans = 1
        N = N % mod 
        while R>0:
            if R % 2 == 1:
                ans = (ans * N) % mod
            N = (N * N) % mod
            R //= 2
        return ans

'''
    def power(self,N,R):
        ans,nn = 1,R
        if nn<0: nn = abs(n)
        while(nn>0):
            if nn%2 == 1: 
                ans,nn = ans * N,nn - 1
                
            else: 
                N,nn = N * N,nn//2
        if R<0: ans = 1/ans
        return ans % 1000000007
'''
            
'''       
def myPow(x, n):
    
    def helper(x, n):
        if x == 0: return 0
        if n == 0: return 1
        res = helper(x*x, n // 2)
        return x * res if n % 2 else res
    res=helper(x, abs(n))
    return res if n >= 0 else 1 / res
print(myPow(2,5))
        
'''
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends