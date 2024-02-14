#!/bin/python3

a = [i for i in range(1111,10000)]

b = [i for i in a if "0" not in str(i)]

c = []

for i in b:
    d = [0 for _ in range(9)]
    for j in str(i):
        d[int(j)-1] += 1

    w = True
    for j in d:
        if j > 1:
            w = False

    if w:
        c.append(i)

ps = []

for i in c:
    for j in c:
        w = True
        for k in range(len(str(i))):
            if str(i)[k] in str(j):
                w = False
                break
            else:
                continue

        if w:
            ps.append([i, j])

e = "123456789"

for p in ps:
    f = 0
    for i in e:
        if i not in str(p[0])+str(p[1]):
            f = int(i)
            break

    if p[0] / p[1] == f:
        print(f'Found one! It\'s {p[0]}/{p[1]}, which is equal to {f}')
