import math

a = [0, 0]
b = [13, 12]
c = [-13, 14]

side1 = math.sqrt((math.pow(a[0] - a[1], 2)) + (math.pow(b[0] - b[1], 2)))
side2 = math.sqrt((math.pow(b[0] - b[1], 2)) + (math.pow(c[0] - c[1], 2)))
side3 = math.sqrt((math.pow(c[0] - c[1], 2)) + (math.pow(a[0] - a[1], 2)))

p = (side1+side2+side3)/3

h = (2 / side1) * math.sqrt (p * (p - side1) * (p - side2) * (p - side3))

l = math.sqrt(side1 * side2 * (side1 + side2 + side3) * (side1 + side2 - side3)) / side1 + side2

print("Висота h = {:.1f}".format(h))
print("Медіана m = {:.1f}".format(l))
