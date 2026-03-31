class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        tasks_count = Counter(tasks)
        max_freq = max(tasks_count.values())
        max_count = sum(1 for count in tasks_count.values() if count == max_freq)    
        slots_needed = (max_freq - 1) * (n + 1) + max_count
        return max(slots_needed,len(tasks))