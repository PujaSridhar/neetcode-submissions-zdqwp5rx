class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()          # stack asteroid explodes
                    continue
                elif stack[-1] == -a:
                    stack.pop()          # both explode
                alive = False            # current asteroid explodes

            if alive:
                stack.append(a)

        return stack        