import math

k1 = int(input("1 kat = "))
k2 = int(input("2 kat = "))

hypo = math.sqrt(k1*k1 + k2*k2)
S = (1/2)*(k1*k2)

print("hypo = ", hypo)
print("S = ", S)
