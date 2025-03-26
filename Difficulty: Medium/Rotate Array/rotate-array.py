#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        k = d%n
        def reverse(first,last,arr):
            while first<last:
                arr[first],arr[last] = arr[last],arr[first]
                last-=1
                first +=1
        reverse(0,k-1,arr)
        reverse(k,n-1,arr)
        reverse(0,n-1,arr)
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends