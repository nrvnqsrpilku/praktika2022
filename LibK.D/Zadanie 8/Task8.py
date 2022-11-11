import math

def tabulation_x_y():
    k = 1
    y = 0
    f = math.sin(math.pow(k,2))*math.cos(math.pow(k,3)) - math.sin(k) + 5.2
    x = 0
    h = 0
    for i in range(0, 13):
        if x <= 13:
            h += 1.1
            y += f
        print("x = {:.1f}".format(h) ,", " "y = {:.1f}".format(y))
    y1 = 47.1
    y2 = 4.3
    u = math.fabs(y1 - y2)
    print("y = {:.1f}".format(u))

tabulation_x_y()
