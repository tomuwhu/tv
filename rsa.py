p = 7
q = 11
n = p * q
fin = (p - 1) * (q - 1)

a = 2
h = {1}
ht = [1]

i = 2
while a not in h:
    h.add(a)
    ht.append(a)
    a = (a ** i) % fin
    i += 1
z = len(ht)

print(ht, z, fin, fin/z)