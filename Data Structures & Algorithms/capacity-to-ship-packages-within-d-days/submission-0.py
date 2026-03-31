class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)        # minimum possible capacity
        right = sum(weights)       # maximum possible capacity

        def canShip(cap):
            current_load = 0
            required_days = 1

            for w in weights:
                if current_load + w > cap:
                    required_days += 1
                    current_load = w
                else:
                    current_load += w

            return required_days <= days

        while left < right:
            mid = (left + right) // 2

            if canShip(mid):
                right = mid        # try smaller capacity
            else:
                left = mid + 1     # need bigger capacity

        return left        