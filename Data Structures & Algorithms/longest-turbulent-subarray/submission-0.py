class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        ans = 1
        prev = 0   # previous comparison result
        cur_len = 1

        for i in range(1, n):
            if arr[i] > arr[i-1]:
                cur = 1
            elif arr[i] < arr[i-1]:
                cur = -1
            else:
                cur = 0

            if cur == 0:
                cur_len = 1
            elif cur == -prev:
                cur_len += 1
            else:
                cur_len = 2  # reset to new pair

            ans = max(ans, cur_len)
            prev = cur

        return ans        