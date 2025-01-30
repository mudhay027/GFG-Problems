#User function Template for python3

class Solution:
    def rotate(self, arr):
        a = arr[-1]
        for i in range(len(arr)-1,-1,-1):
            arr[i] = arr[i-1]
        arr[0] = a
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        print("~")
        t -= 1

# } Driver Code Ends