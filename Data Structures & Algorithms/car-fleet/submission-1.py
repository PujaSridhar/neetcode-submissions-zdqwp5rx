class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(reverse=True)  # Sort by position in descending order
    
        fleets = 0
        time_to_dest = 0
    
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > time_to_dest:
                fleets += 1
                time_to_dest = time
    
        return fleets       