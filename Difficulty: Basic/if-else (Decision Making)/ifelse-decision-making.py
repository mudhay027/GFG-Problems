
class Solution:
    def compareNM(self, n : int, m : int) -> str:
        if n>m:
            return "greater"
        elif n<m:
            return "lesser"
        else:
            return "equal"
        



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        obj = Solution()
        res = obj.compareNM(n, m)
        
        print(res)
        

# } Driver Code Ends