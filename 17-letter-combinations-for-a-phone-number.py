class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # edge case for no digits
        if len(digits) == 0:
            return []

        # make a hashmap of digit to letters
        digitMap = { 
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # output
        ans = []

        # backtracking to find all combinations
        def dfs(remaining, path):
            
            # if at end of digit sequence, append combination to output array
            if len(remaining) == 0:
                ans.append(path)
                return
            
            # search for current digit possibilities
            for letter in digitMap[remaining[0]]:

                # add current letter to path and search
                dfs(remaining[1:], path + letter)
        
        # search for all combinations
        dfs(digits, "")

        return ans