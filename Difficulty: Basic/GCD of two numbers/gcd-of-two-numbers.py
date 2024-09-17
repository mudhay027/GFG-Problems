
class Solution:
    def gcd(self, a : int, b : int) -> int:
        while(a>0 and b>0):
            if a>b:
                a=a%b
            else:
                b=b%a
        if a == 0:
            return b
        else:
            return a
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

# } Driver Code Ends