# author: mofhu@github
# 6130. Design a Number Container System

class NumberContainers:

    def __init__(self):
        self.d = {}
        self.di = {}
        return None

    def change(self, index: int, number: int) -> None:
        if index not in self.d:
            self.d[index] = number
            if number in self.di:
                self.di[number].add(index)
            else:
                self.di[number] = {index}

        else:
            num0 = self.d[index]
            self.di[num0].remove(index)  # lead to O(n^2)?
            self.d[index] = number
            if number in self.di:
                self.di[number].add(index)
            else:
                self.di[number] = {index}
        return None


    def find(self, number: int) -> int:
        if number in self.di:
            if len(self.di[number]) > 0:
                return sorted(self.di[number])[0]
            else:
                return -1
        else:
            return -1
