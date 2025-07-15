class Solution:
    def inversionCount(self, arr):
        low = 0
        high = len(arr)-1
 #       mid = len(arr)//2
        def merge(arr,low,mid,high):
            temp = []
            left = low
            right = mid+1
            count = 0
            while left<=mid and right<= high:
                if arr[left]<= arr[right]:
                    temp.append(arr[left])
                    left+=1
                else:
                    temp.append(arr[right])
                    count += mid - left +1
                    right+=1
            if left<=mid:
                temp += arr[left:mid+1]
            if right<=high:
                temp += arr[right:high+1]
            arr[low:high+1] = temp
            return count
        def merge_sort(arr,low,high):
            count = 0
            if low >= high: return count
            mid = (low+high) // 2
            count += merge_sort(arr,low,mid)
            count += merge_sort(arr,mid+1,high)
            count += merge(arr,low,mid,high)
            return count
        return merge_sort(arr,low,high)