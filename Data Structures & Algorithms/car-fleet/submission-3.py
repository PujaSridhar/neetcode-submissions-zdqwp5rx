class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos,spd)for pos, spd in zip(position, speed)]
        cars.sort(reverse = True)
        fleets = 0
        timeToDest = 0
        for pos, spd in cars:
            time = (target-pos)/spd
            if time > timeToDest:
                fleets += 1
                timeToDest = time
        return fleets