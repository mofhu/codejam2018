# author: mofhu@github
# B - Triangle (Easier)

n, m = [int(s) for s in input().split(' ')]
nodes = {i:[] for i in range(1, n+1)}
edges = set()

for i in range(m):
    u, v = [int(s) for s in input().split(' ')]
    nodes[u].append(v)
    edges.add((u,v))

# print(nodes)
# print(edges)
ans = 0
for i in range(1, n+1):
    if len(nodes[i]) >= 2:
        for j in range(len(nodes[i])-1):
            for k in range(j+1, len(nodes[i])):
                if (nodes[i][j], nodes[i][k]) in edges or (nodes[i][k], nodes[i][j]) in edges:
                    ans += 1
print(ans)
