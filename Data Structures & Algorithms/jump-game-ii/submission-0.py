class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            # Update the farthest we can reach
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the current jump, increment jumps
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # If we can already reach the end, return the jumps
                if current_end >= len(nums) - 1:
                    break
        
        return jumps        