# GCJ Qualification Round 2009 - B
# Author: Mo Frank Hu

t = int(input())

for ncase in range(1, t+1):
    h, w = [int(z) for z in input().split(" ")]
    # print(h, w)  #
    s = []
    basin = []
    for i in range(h):
        s.append([int(z) for z in input().split(" ")])
        basin.append([False for z in range(w)])
    # print(s)  #

    d_link = {}
    for i in range(h):
        for j in range(w):
            links = (i, j, s[i][j])  #init links
            if i > 0:  # north
                if s[i-1][j] < links[2]:
                    links = (i-1, j, s[i-1][j]) 
            if j > 0:  # west
                if s[i][j-1] < links[2]:
                    links = (i, j-1, s[i][j-1])
            if j < w-1:  # east
                if s[i][j+1] < links[2]:
                    links = (i, j+1, s[i][j+1])
            if i < h-1:  # south
                if s[i+1][j] < links[2]:
                    links = (i+1, j, s[i+1][j])
            if (i,j) == (links[0], links[1]):
                basin[i][j] = True
                d_link[(i,j)] = (i, j)
            else:
                d_link[(i,j)] = (links[0], links[1])
    # print(basin)  #
    # print(d_link)  #

    # scan to define all labels        
    labels = "abcdefghijklmnopqrstuvwxyz"
    label = {}
    k = 0
    # scan to define basin
    for i in range(h):
        for j in range(w):
            basin_ij = (i,j)
            while(basin[basin_ij[0]][basin_ij[1]] is False):
                basin_ij = d_link[basin_ij]
                # print(basin_ij)
            # define labels from north-west
            if basin_ij not in label:
                label[basin_ij] = labels[k]
                k += 1
            s[i][j] = label[basin_ij]

    print("Case #{}:".format(ncase))
    for i in range(h):
        print(" ".join(s[i]))