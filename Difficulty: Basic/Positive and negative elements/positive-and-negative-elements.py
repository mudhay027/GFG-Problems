#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3



class Solution:
    def arranged(self,arr):
        pos = [x for x in arr if x>=0]
        neg = [x for x in arr if x<0]
        a = []
        for i in range(len(arr)//2):
            a.append(pos[i])
            a.append(neg[i])
        return a

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.arranged(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends