class Solution:
    def segregateElements(self, arr):
        l = len(arr)
        if l==0 or l==1:
            return arr
        A=[]
        for i in arr:
            if i>=0:
                A.append(i)
        for i in arr:
            if(i<0):
                A.append(i)
        arr[:] = A
        return arr
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.segregateElements(a)
        print(*a)

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends