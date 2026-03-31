class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Step 1: Binary search for insertion point
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid

        # Step 2: Two pointers
        l, r = left - 1, left
        result = []

        while k > 0:
            if l < 0:
                result.append(arr[r])
                r += 1
            elif r >= len(arr):
                result.append(arr[l])
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                result.append(arr[l])
                l -= 1
            else:
                result.append(arr[r])
                r += 1
            k -= 1

        return sorted(result)        