class Solution:
    def climbStairs(self, n: int) -> int:
        global store
        store = [1,2]
        def iter_stairs(n):
            global store
            if n <= len(store):
                return store[n-1]
            else:
                t = iter_stairs(n-1) + iter_stairs(n-2)
                store.append(t)
                return store[n-1]
        return iter_stairs(n)

