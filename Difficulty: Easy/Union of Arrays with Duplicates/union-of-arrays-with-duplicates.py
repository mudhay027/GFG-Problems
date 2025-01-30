#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        c = a+b
        a = set(c)
        return len(a)
        
'''    

        if (len(a)== 0 and len(b)==0):
            return 0
        elif len(a) == 0:
            return len(b)
        elif len(b) == 0:
            return len(a)
        count = 0
        for i in a:
            if i in b:
                count+=1
                b.remove(i)
            else:
                count+=1
        return (count+len(b))
'''
  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.findUnion(a, b))
        print("~")

# } Driver Code Ends