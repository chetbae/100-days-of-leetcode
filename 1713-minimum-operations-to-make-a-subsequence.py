class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # create hashmap for number to index
        hmap = {num:i for i, num in enumerate(target)}

        # we construct a sequence of indexes for nums in arr that exist in target
        sequence = [hmap[x] for x in arr if x in hmap]
        
        # now from the index sequence, we find the longest increasing subsequence ~ we find the longest existing nums from target in arr
        
        # maintain longest increasing subsequence (LIS) in sub
        sub = []

        for x in sequence:
            
            # if empty or greater num, extend current LIS
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)

            # otherwise find and replace lowest num >= x
            # since replacing with lesser num, replacing only opens possibilities for further subsequences
            else:
                i = bisect.bisect_left(sub, x)
                sub[i] = x
        
        # sub is the LIS of indexes for nums in arr, so min operations is to add nums from target into the subsequence
        return len(target) - len(sub)

                


                