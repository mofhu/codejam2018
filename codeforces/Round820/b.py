# author: mofhu@github
# B. Decode String

t = int(input())

for ncase in range(1, t+1):
    n = int(input())
    s = input()
    ans = []
    i = n-1
    while i >= 0:
        # print(s[i])
        if s[i] == '0':
            # print(s[i-2:i+1])
            ans.append(''.join(s[i-2:i+1]))
            i -= 3
        else:
            ans.append(s[i:i+1])
            i -= 1
    d = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e',
        '6': 'f', '7': 'g', '8': 'h', '9': 'i',
        '100': 'j', '110': 'k', '120': 'l', '130': 'm',
        '140': 'n', '150': 'o', '160': 'p', '170': 'q',
        '180': 'r', '190': 's', '200': 't', '210': 'u',
        '220': 'v', '230': 'w', '240': 'x', '250': 'y',
        '260': 'z'
    }
    ans.reverse()


    print(''.join(d[i] for i in ans))


