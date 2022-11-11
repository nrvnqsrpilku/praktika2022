import math


def cycle():
    sum = 0
    k = 1
    i = 13
    while k <= i:
        sum -= ((math.sin(math.pow(k,2))*math.cos(k*k*k) - math.sin(k) + 5.2)*(k))/k
        print("{:.3f}".format (sum))
cycle()
