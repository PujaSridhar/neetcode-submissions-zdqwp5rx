class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # Step 1: Count frequency of each task
        task_counts = Counter(tasks)
        
        # Step 2: Find the maximum frequency
        max_freq = max(task_counts.values())
        
        # Step 3: Find how many tasks have the maximum frequency
        max_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # Step 4: Calculate the ideal slots needed
        slots_needed = (max_freq - 1) * (n + 1) + max_count
        
        # Step 5: The result is the maximum of slots_needed and length of tasks
        return max(slots_needed, len(tasks))