class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)

        # use stacks to track next candidate for warmer temp
        stack = []

        # case 1: top of stack is warmer than current -> keep element in stack, it could be the next warmest for another, i.e. current < next < top of stack
        # case 2: top of stack is colder than current -> pop element. for anything down the line, current would be next warmest

        for i in range(len(temperatures)-1, -1, -1):
            current = temperatures[i]

            # search for the next warmest element in stack
            while stack:

                # if top of stack is warmer, record index, add to stack, and continue to next temperature
                if stack[-1][0] > current:
                    ans[i] = stack[-1][1] - i
                    stack.append((current, i))
                    break
                
                # if top is colder, pop stack and keep searching
                else:
                    stack.pop()

            # if stack is empty, append current temp as candidate
            if not stack:
                stack.append((current, i))
        
        return ans
                