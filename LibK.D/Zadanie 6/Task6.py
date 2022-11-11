import math
z = 0
x = 0
y = 1
k = 1

for i in range(5):
        if i <= 18:
                x += math.sin(math.pow(k,2))*math.cos(math.pow(k,3)) - math.sin(k) + 5.2
        print("Сума = {:.1f}".format (x))

for i in range(5):
        if i <= 18:
                y *= math.sin(math.pow(k,2))*math.cos(math.pow(k,3)) - math.sin(k) + 5.2
        print("Добуток = {:.1f}".format (y))

z = 5*x - 2*y
print("z = {:.1f}".format (z))
