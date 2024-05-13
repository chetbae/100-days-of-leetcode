class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # 1) given an existing subsequence, a greater num can only extend it
        # 2) given an existing subsequence, a num lesser than last in subsequence can only extend possibilities
        #   i.e.) arr: [1,6,3,7,4,6,8], existing: [1,3,7], next nums: [4,6,8] -> ans: [1,3,4,6,8]
        #   cont.) num 4: [1,3,7] -> [1,3,4], num 6: [1,3,4] -> [1,3,4,6] then ... [1,3,4,6,8]
        
        # track longest increasing subsequence
        seq = []
        
        # check all nums in order
        for num in nums:

            # if seq is empty or curret num is greater than last in seq, add to seq
            if not seq or num > seq[-1]:
                seq.append(num)
            
            # otherwise num can replace part of sequence for all subsequence possibilities
            else:
                
                # find index of the smallest element greater or equal to num
                index = bisect_left(seq, num)
                seq[index] = num
        
        # return length of seq, where the longest length is maintained as algorithm only adds
        return len(seq)





            

