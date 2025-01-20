#User function Template for python3

class Solution:
    def rearrange(self,arr):
        positive = [x for x in arr if x>=0]
        negative = [y for y in arr if y<0]
        A = []
        i=0
        while i<len(positive) and i<len(negative):
            A.append(positive[i])
            A.append(negative[i])
            i+=1
        if i<len(positive):
            A = A + positive[i:]
        if i<len(negative):
            A = A + negative[i:]
        arr[:] = A
        return arr
        
            
            
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends