class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        deq = deque()
        result = []

        for i in range(len(nums)):
        # Remove indices that are out of the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()

        # Remove elements from the deque that are less than the current element
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

        # Add the current element's index to the deque
            deq.append(i)

        # Add the maximum element of the current window to the result list
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result