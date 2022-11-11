import math

def math_f():
    x = int(input("Число x:"))
    a = int(input("Число a:"))
    b = int(input("Число b:"))
    c = int(input("Число c:"))
    d = int(input("Число d:"))

    fi = math.tan((x + a)) - math.log(11, math.fabs(b + 7))
    wi = math.pow(c, 5) * math.sqrt( (math.pow (x, 2)) + d * math.pow (math.e, 1.3))
    
    def calc_y():
        if math.sin(math.pow(x,2))*math.cos(math.pow(x,3)) - math.sin(x) + 5.2 * (math.fabs(x)) < 10:
            print("Результат fi:", fi)
        elif math.sin(math.pow(x,2))*math.cos(math.pow(x,3)) - math.sin(x) + 5.2 * (math.fabs(x)) >= 10:
            print("Результат wi = {:.1f}".format(wi))
        else:
            print("None")
    calc_y()

math_f()
