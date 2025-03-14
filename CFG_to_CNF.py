
productii = {}
aux = {}
litereNeterminale = []
litereTerminale = []

with open("in.txt") as f:
    for line in f.readlines():
        line = line.rstrip()
        a, b = line.split("->")

        a = a.strip()
        if a not in litereNeterminale:
            litereNeterminale.append(a)
        b = [x.strip() for x in b.split("|")]

        productii[a] = b
        for x in b:
            for litera in x:
                if 'a' <= litera <= 'z' and litera not in litereTerminale:
                    litereTerminale.append(litera)

# redefinesc productia initiala
litereNeterminale.append("S0")
productii[litereNeterminale[-1]] = [litereNeterminale[0]]

# creez stariNeterminale care duc direct in stariFinale pentru convenienta
i = 0
for x in litereTerminale:
    litereNeterminale.append("Z"+str(i))
    productii["Z"+str(i)] = [x]
    i += 1

for key in productii:
    temp2 = productii[key].copy()
    j = 0
    if key == "Z":
        j = len(litereTerminale)
    if key == "S":
        j += 1

    for x in temp2:
        if x in litereTerminale or x == litereNeterminale[0] or x == ".":
            continue
        elif len(x) == 1 and "A" <= x[0] <= "Z":
            continue
        elif len(x) == 2:
            if 'A' <= x[0] <= 'Z' and 'A' <= x[1] <= 'Z':
                continue
        # Daca nu e de forma Chomsky, e eliminata din dict aici
        productii[key].remove(x)

        i, z = 0, []

        for i in range(len(x)):
            if "a" <= x[i] <= "z":
                z.append("Z" + str(litereTerminale.index(x[i])))
                litereNeterminale.append("Z" + str(litereTerminale.index(x[i])))
            else:
                z.append(x[i])

        nextt = key + str(j)
        j += 1
        if key not in aux:
            aux[key] = []
        aux[key].append(z[0]+nextt)
        litereNeterminale.append(nextt)

        for i in range(1, len(z)-2):
            current = nextt
            nextt = key + str(j)
            litereNeterminale.append(nextt)
            j += 1
            aux[current] = [z[i]+nextt]

        aux[nextt] = [z[-2]+z[-1]]

for key in aux:
    if key not in productii:
        productii[key] = []
    productii[key] += aux[key]

ele = []
for key in productii:
    if "." in productii[key]:
        ele.append(key)
        productii[key].remove(".")

for el in ele:
    for key in productii:
        for x in productii[key]:
            if el in x:
                if x == el:
                    if key not in ele:
                        ele.append(key)
                    if key == "S0":
                        productii[key].append(".")
                elif x[-1] == el:
                    if x[:-1] not in productii[key]:
                        productii[key].append(x[:-1])
                elif x[0] == el and "A" <= x[1] <= "Z":
                    if x[1:] not in productii[key]:
                        productii[key].append(x[1:])

sotp = {}
for key in productii:
    sotp[key] = []

repet = 1

while repet:
    repet = 0
    for key in productii:
        for x in productii[key]:
            if x in sotp[key]:
                while x in productii[key]:
                    productii[key].remove(x)
            elif x == key:
                while x in productii[key]:
                    productii[key].remove(x)
            elif x in litereNeterminale:
                repet = 1
                sotp[key].append(x)
                productii[key] += productii[x]
                while x in productii[key]:
                    productii[key].remove(x)

# del productii[litereNeterminale[0]]

for key in productii:
    print(key, "->", end=" ")
    print(*productii[key], sep=" | ")

