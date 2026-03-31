class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        if not nums:
            return 0
        
        # Initialize the maximum, minimum, and result with the first element.
        max_product = min_product = result = nums[0]
        
        # Iterate through the array starting from the second element.
        for i in range(1, len(nums)):
            current = nums[i]
            
            # When current element is negative, max_product and min_product are swapped.
            if current < 0:
                max_product, min_product = min_product, max_product
            
            # Update max_product and min_product.
            max_product = max(current, max_product * current)
            min_product = min(current, min_product * current)
            
            # Update the result with the maximum product found so far.
            result = max(result, max_product)
        
        return result        