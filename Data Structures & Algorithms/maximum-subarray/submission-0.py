class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize max_sum with a very small number and current_sum with 0
        max_sum = float('-inf')
        current_sum = 0
        
        # Traverse through each number in the array
        for num in nums:
            # Add the current number to current_sum
            current_sum += num
            
            # Update max_sum if the current_sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
            
            # If current_sum is negative, reset it to 0
            if current_sum < 0:
                current_sum = 0
        
        return max_sum        