class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
            
        # create cooling and ready maps for tasks A-Z
        cooling, counter = [0] * 26, [0] * 26

        # populate counter map
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
        
        # having a non zero in cooling means tasks X is unavailable
        # greedy strategy, always choose the most frequent tasks to allow it to cool

        # create total amount of cycles counter
        t = 0

        # create tasksLeft
        tasksLeft = len(tasks)

        while tasksLeft > 0:

            # get most frequent task index and counter
            nextTask, maxCount = -1, 0
            
            # iterate through tasks A-Z
            for i in range(26):

                # if cooling, decrement cooling counter
                if cooling[i] > 0:
                    cooling[i] -= 1
                
                # or else tasks is ready and check for most frequent tasks
                elif counter[i] > 0:
                    if counter[i] > maxCount:
                        maxCount = counter[i]
                        nextTask = i
                
            # if there is an available task
            if nextTask != -1:

                # cool task
                cooling[nextTask] = n

                # decrement task count
                counter[nextTask] -= 1

                # decrement total tasks
                tasksLeft -= 1
            
            # increment cycles
            t += 1
        
        return t

# Smart solution with some counting
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # find task(s) with greatest frequency
        count = [0] * 26

        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        maxCount = max(count)

        # get number of tasks with same max freq
        numOfMaxCount = 0
        for frequency in count:
            if frequency == maxCount:
                numOfMaxCount += 1
        
        
        # get number of rests needed between max tasks
        numOfIntervals = maxCount-1

        # get length of each rest period
        intervalLength = n - numOfMaxCount + 1

        # get number of cycles in each rest. If multiple maxes, each rest gets eaten up by remaining maxes
        restCycles = numOfIntervals * intervalLength

        # get remaining tasks
        remainingTaskCount = len(tasks) - maxCount * numOfMaxCount

        # if total restCycles is greater than remainder task count, some rest periods are needed. if lesser, than all tasks can be run with no breaks
        requiredRestCycles = max(0, restCycles - remainingTaskCount)

        return len(tasks) + requiredRestCycles