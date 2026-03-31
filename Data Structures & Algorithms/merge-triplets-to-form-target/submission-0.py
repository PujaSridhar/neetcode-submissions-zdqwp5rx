class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found_a = found_b = found_c = False
        
        for triplet in triplets:
            # Check if the triplet can contribute to forming the target
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                # Check for each component
                if triplet[0] == target[0]:
                    found_a = True
                if triplet[1] == target[1]:
                    found_b = True
                if triplet[2] == target[2]:
                    found_c = True
        
        # We can only form the target if all components can be matched
        return found_a and found_b and found_c        