#!/bin/python3

# Az összes nullát nem tartalmazó négyjegyű szám
a = [i for i in range(1111,10000) if "0" not in str(i)]

# Az összes egyedi szám
b = []

for i in a:
    # Megszámoljuk, hányszor fordul elő egy-egy számjegy az adott számban
    c = [0 for _ in range(9)]
    for j in str(i):
        c[int(j)-1] += 1

    w = True
    # Ha egynél többször, a számot nem rakjuk be az egyedi számok listájába
    for j in c:
        if j > 1:
            w = False

    # Ha nem, belerakjuk
    if w:
        b.append(i)

# Egyedi számpárok listája
ps = []

for i in b:
    for j in b:
        w = True
        # Ha a második szám tartalmazza az első szám bármelyik számjegyét, nem helyezzük az egyedi párok listájába
        for k in range(len(str(i))):
            if str(i)[k] in str(j):
                w = False
                break
            else:
                continue

        # Ha nem, belehelyezzük
        if w:
            ps.append([i, j])

# Az összes számjegy egy string-ben lista helyett
e = "123456789"

for p in ps:
    f = 0
    for i in e:
        # Eredményként vesszük azt a számjegyet, amely nem szerepel a pár egyik számában sem
        if i not in str(p[0])+str(p[1]):
            f = int(i)
            break

    # Ha tényleg ez az osztás eredménye, megtaláltunk egy megfelelő párt
    if p[0] / p[1] == f:
        print(f'Found one! It\'s {p[0]}/{p[1]}, which is equal to {f}')
