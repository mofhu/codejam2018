# 时间复杂度和空间复杂度分析

## 任务：

1. 自己尝试找一段代码，对其进行复杂度分析。
2. 同时，完成一篇时间复杂度学习心得。

## answer

### 1. 自己尝试找一段代码，对其进行复杂度分析。

```python
# code from fbhackercup2020-QR, my answer

ncase = int(input())

for case in range(1, ncase + 1):  # O(ncase)
    n = int(input())
    i = input()
    o = input()
    ans = [['N' for j in range(n)] for k in range(n)]
    # print(i,o, ans)
    for oi in range(n):  # O(n^2)
        for ii in range(n):
            if oi == ii:
                # print(oi, ii)
                # print(ans[oi][ii])
                ans[oi][ii] = 'Y'
            else:
                if o[oi] == 'Y' and i[ii] =='Y' and abs(oi-ii) == 1:
                    # print(oi, ii)
                    # print(ans[oi][ii])
                    ans[oi][ii] = 'Y'
    for oi in range(n):  # O(n^2)
        for ii in range(n):
            if abs(oi-ii) > 1:
                if oi > ii:
                    p = oi
                    while p-1 >= ii:
                        if ans[p][p-1] == 'N':
                            break
                        else:
                            p -= 1
                    else:
                        # print(oi, ii)
                        ans[oi][ii] = 'Y'
                elif oi < ii:
                    p = oi
                    while p+1 <= ii:
                        if ans[p][p+1] == 'N':
                            break
                        else:
                            p += 1
                    else:
                        # print(oi, ii)
                        ans[oi][ii] = 'Y'


    print('Case #{}:'.format(case))
    # print(ans)
    for line in ans:
        print(''.join(line))
```

standard O(n^2) code

### 2. 同时，完成一篇时间复杂度学习心得。

brief: 了解时间复杂度, 空间复杂度概念. 并应用于日常工作(competitive programming)

#### 常用的时间复杂度

- 1
- log(n)
- n
- nlog(n)
- n^2
- n^3
- 2^n
- n!

简单推论: n > 10 时, O(2^n) 和 O(n!) 增长速度极快!

#### 递归函数时间复杂度的计算: master theorem (主定理)

- 二分搜索 O(log n)
- 二叉树遍历 O(n)
- 矩阵搜索 O(n)
- 归并排序 O(nlog n)

#### 空间复杂度

内存占用等.

#### how to use it?

- 每写一段代码, 应习惯性分析其时间和空间复杂度 (特别对于 n 可能会很大的工程代码)
- 优先考虑优化时间复杂度, 如有余力再试图优化空间复杂度
