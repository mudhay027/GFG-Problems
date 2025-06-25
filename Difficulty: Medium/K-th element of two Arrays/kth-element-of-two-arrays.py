#User function Template for python3


class Solution:

    def kthElement(self, a, b, k):
        i = j = 0
        count = 0
        aa = 0
        n, m = len(a), len(b)
        
        while count<k:
            if i<n and (j>=m or a[i] <= b[j]):
                aa = a[i]
                i += 1
            else:
                aa = b[j]
                j += 1
            count += 1
        return aa
        
        
'''
        minn = min(a,b)
        j=0
        aa = 0
        aaa = 0
        i=0
        while k>aaa:
            if a[i]<b[j]:
                aa = a[i]
                i+=1
            elif b[j]<a[i]:
                aa = b[j]
                j+=1
            else:
                i+=1
                j+=1
                aa = b[j]
                aaa+=1
            aaa+=1
        return aa
        
'''        
            
