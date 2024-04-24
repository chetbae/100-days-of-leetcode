class Node:
    def __init__(self, val=False):
        self.refs = [None] * 26
        self.val = val

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root

        for letter in word:
            index = ord(letter) - ord('a')
            
            if not current.refs[index]:
                current.refs[index] = Node()
            
            current = current.refs[index]
        
        current.val = True

    def search(self, word: str) -> bool:
        return self.search_rec(word, self.root)
        
    def search_rec(self, word: str, node: Node):

        if len(word) == 0:
            return node.val
        
        if word[0] == '.':

            for i in range(26):
                if node.refs[i] and self.search_rec(word[1:], node.refs[i]):
                    return True

            return False
        
        else:
            index = ord(word[0]) - ord('a')

            if node.refs[index]:            
                return self.search_rec(word[1:], node.refs[index])
            else:
                return False
                
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)