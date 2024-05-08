class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = collections.Counter(words)
        
        arr = [(frequency[word], word) for word in frequency]

        self.mergesort(arr, 0, len(frequency))
        
        n = len(arr)
        return [word for freq, word in arr[:min(n,k)]]

    # sort by descending freq, ascending lexico
    def mergesort(self, arr, start, stop):
        if start+1 == stop:
            return arr[start:stop]
        
        mid = start + (stop - start) // 2 # mid ceiling = start + ((stop - 1) - start + 1) // 2

        left = self.mergesort(arr, start, mid)
        right = self.mergesort(arr, mid, stop)

        l, r = 0, 0
        
        for i in range(start, stop):
            if l == mid - start:
                arr[i] = right[r]
                r += 1
                continue
                
            if r == stop - mid:
                arr[i] = left[l]
                l += 1
                continue

            freq1, word1 = left[l]
            freq2, word2 = right[r]

            # left is greater
            if freq1 > freq2 or (freq1 == freq2 and word1 < word2):
                arr[i] = left[l]
                l += 1
            # right is greater
            else:
                arr[i] = right[r]
                r += 1
        
        return arr[start:stop]