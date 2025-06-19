class Solution:
    def fourSum(self, arr, target):
        aa = set()
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                s = set()
                for k in range(j+1,n):
                    sum = target - (arr[i] + arr[j] + arr[k])
                    if sum in s:
                        curr = sorted([arr[i],arr[j],arr[k],sum])
                        aa.add(tuple(curr))
                    s.add(arr[k])
        return [list(l) for l in aa]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.fourSum(A, D)
        ans.sort()
        # print(ans)
        for v in ans:
            for u in v:
                print(u, end=" ")
            print()
        if (len(ans) == 0):
            print(-1)

        print("~")

# } Driver Code Ends