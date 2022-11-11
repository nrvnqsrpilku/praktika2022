import math


def cycle_fun():
    k = 1
    i = 0
    a = []
    b = []
    for i in range(0, 13):
        k += 1
        x = round((math.sin(math.fabs(k))/ 0.1 + 9.4 * math.sin((3 * k- 2.5)) ) * k )  
        a.append(x)
        print("{:.2f}".format(a[i]))
    print("Відсутність шуканих даних")
cycle_fun()
        
    

