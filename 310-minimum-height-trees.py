class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # make a tree map
        tree = defaultdict(set)

        # populate tree map, undirected
        for edge in edges:
            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])

        # make a perimeter (leaf) set
        leaves = [i for i in range(n) if len(tree[i]) == 1]

        # narrow down perimeter until 1 or 2 nodes left in tree
        while n > 2:
            newLeaves = []
            n -= len(leaves)

            # prune all leaves from tree
            for leaf in leaves:

                # get the one neighbour from tree map
                nb = tree[leaf].pop()
                del tree[leaf]
            
                # remove leaf from neighbouring branches
                tree[nb].remove(leaf)
                if len(tree[nb]) == 1:
                    newLeaves.append(nb)
            
            leaves = newLeaves
        
        return list(tree.keys())


            