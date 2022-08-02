# author: mofhu@github
# 6134. Find Closest Node to Given Two Nodes

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        ans = -1
        s1 = set()
        s2 = set()
        s1.add(node1)
        s2.add(node2)
        cycle1 = 0
        cycle2 = 0
        if node1 == node2:
            ans = node1
            return ans
        while True:
            if cycle1 == 1 and cycle2 == 1 or ans != -1:
                break
            elif cycle1 != 1:
                if edges[node1] in s2:
                    ans = edges[node1]
                    # break
                elif edges[node1] in s1 or edges[node1] == -1:
                    cycle1 = 1  # use or end
                else:
                    s1.add(edges[node1])
                    node1 = edges[node1]

            if cycle1 == 1 and cycle2 == 1:
                break
            elif cycle2 != 1:
                if edges[node2] in s1:
                    if ans == -1:
                        ans = edges[node2]
                        break
                    else:
                        ans = min(ans, edges[node2])
                        break
                elif edges[node2] in s2 or edges[node2] == -1:
                    cycle2 = 1
                else:
                    s2.add(edges[node2])
                    node2 = edges[node2]
        return ans
