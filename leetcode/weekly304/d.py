# author: mofhu@github
# 2360. Longest Cycle in a Graph

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        nodes = [0 for i in range(len(edges))]
        ans = -1
        for i in range(len(edges)):
            # print(f'i {i} {nodes}')
            if nodes[i] != 0:
                continue
            if edges[i] == -1:
                nodes[i] = 1
                continue
            t = {}
            j = 0
            while edges[i] not in t:
                # print(t)
                t[edges[i]] = j  # final note: have to use dict (list is not fast enough for finding index)
                if edges[i] == -1 or nodes[edges[i]] == 1:
                    break
                i = edges[i]
                j += 1
                nodes[i] = 1
            else:
                # print(t)
                if len(t) - t[edges[i]] > ans:
                    ans = len(t) - t[edges[i]]
        return ans

