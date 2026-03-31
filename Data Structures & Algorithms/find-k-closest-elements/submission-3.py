class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (right + left) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        
        l,r = left - 1, left
        res = []
        while k > 0:
            if l < 0:
                res.append(arr[r])
                r += 1
            elif r >= len(arr):
                res.append(arr[l])
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1
        return sorted(res)
