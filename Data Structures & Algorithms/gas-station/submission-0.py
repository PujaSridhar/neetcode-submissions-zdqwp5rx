class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0
        current_tank = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            
            # If current_tank is negative, reset the start index and current_tank
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
        
        # If total_tank is negative, no solution exists
        if total_tank < 0:
            return -1
        else:
            return start_index        