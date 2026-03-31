class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_bananas(k):
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile/k)
            return hours_needed <= h
        left,right = 1,max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if can_eat_bananas(mid):
                right = mid
            else:
                left = mid + 1
        return left    