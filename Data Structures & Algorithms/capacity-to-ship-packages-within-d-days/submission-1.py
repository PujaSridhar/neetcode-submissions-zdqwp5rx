class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        def canship(cap):
            current_weight = 0
            required_days = 1
            for w in weights:
                if current_weight + w > cap:
                    required_days += 1
                    current_weight = w
                else:
                    current_weight += w
            return required_days <= days
        while left < right:
            mid = (right + left) // 2
            if canship(mid):
                right = mid
            else:
                left = mid + 1
        return left    