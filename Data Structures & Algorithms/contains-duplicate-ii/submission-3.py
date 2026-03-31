class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for num in range(len(nums)):
            if nums[num] in window:
                return True
            window.add(nums[num])
            if len(window) > k:
                window.remove(nums[num-k])
        return False    