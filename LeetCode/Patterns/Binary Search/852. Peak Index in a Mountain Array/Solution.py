class Solution:
    def peakIndexInMountainArray(self, arr):
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] > arr[m-1] and arr[m] > arr[m+1]:
                return m
            elif arr[m] > arr[m-1] and arr[m] < arr[m+1]:
                l = m
            else:
                r = m