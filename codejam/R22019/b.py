ncase = int(input())
import time
from math import floor

output = open('b.out', 'w')

for case in range(1, ncase+1):
    nv = [100 for i in range(20)]
    final_vase = -1
    while (True):
        day = int(input())
        idx = []
        if day <= 75:
            mod = day % 15
            div = int(floor(day / 15))
            ans = '{} {}'.format(mod+1, 100-div)
            print(ans)
        elif day < 100:
            mod = day - 75 + 15 - 1
            if day <= 80:
                ans = '{} 0'.format(mod+1)
                print(ans)
                # output.write(ans+'\n')
                line = input()
                nv[mod] = len([s for s in line.split(' ')]) -1
            else:
                min_value = min(nv)
                for i in range(15, len(nv)):
                    if nv[i] == min_value:
                        idx.append(i)
                if final_vase == -1:
                    final_vase = idx[0] + 1
                    nv[idx[0]] = 100
                    del idx[0]
                    if len(idx) == 0:
                        min_value = min(nv)
                        for i in range(15, len(nv)):
                            if nv[i] == min_value:
                                idx.append(i)
                mod = idx[0]
                nv[mod] += 1
                ans = '{} 100'.format(mod+1)
                print(ans)
                # output.write(ans+'end {}\n'.format(final_vase))
        else:
            print('{} 100'.format(final_vase))
            # output.write('final {}\n'.format(final_vase))
            break
    time.sleep(0.01)



