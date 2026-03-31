class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def ship(cap):
            requiredDays = 1
            currentWeight = 0
            for w in weights:
                if currentWeight + w > cap:
                    requiredDays += 1
                    currentWeight = w
                else:
                    currentWeight += w
            return requiredDays <= days

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (right + left) // 2
            if ship(mid):
                right = mid
            else:
                left = mid + 1
        return left