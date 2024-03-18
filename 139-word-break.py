# using DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # convert list to hashset
        db = set(wordDict)

        # make dp array from 0 to n, where dp[i] ~ substring s[0:i+1] can be broken by wordDict
        dp = [False] * (len(s) + 1)

        # initial condition, empty substring is True
        dp[0] = True
        
        # build up dp array from i in [0,n] == [0,n+1)
        for i in range(len(s)):

            # let j be the index where the substring is divided
            for j in range(i+1):
                
                # if dp[j] is True ~ s[0:j] can be broken,
                # AND,
                # rest of substring is a word,
                # s[0:i+1] can be broken
                if dp[j] and s[j:i+1] in db:

                    # mark dp array as True
                    dp[i+1] = True

                    # if there are other permutations of words, same result therefore skip
                    break
            
        return dp[len(s)]