class Solution:
    def minRow(self,a):
        n = len(a)
        mark = 1
        count = 0
        mini = float('inf')
        for i in range(n):
            count = 0
            for j in a[i]:
                if j == 1:
                    count+=1
            if count < mini:
                mark = i+1
                mini = count
        return mark