import math
x = 13

salary1 = 100 * math.fabs(math.sin(math.pow(x,2))*math.cos(math.pow(x,3)) - math.sin(x) + 5.2*(13) + 50)
salary2 = 150 * math.fabs(math.sin(math.pow(x,2))*math.cos(math.pow(x,3)) - math.sin(x) + 5.2*(13) + 100)
salary3 = 200 * math.fabs(math.sin(math.pow(x,2))*math.cos(math.pow(x,3)) - math.sin(x) + 5.2*(13) + 135)

tax1 = (salary1 / 100) * 10
tax2 = (salary2 / 100) * 10
tax3 = (salary3 / 100) * 10

def funtion_tax():
    print("Податок від суми заробітної плати роботи типу А становить 10%= {:.1f}".format (tax1))
    print("Податок від суми заробітної плати роботи типу B становить 15%= {:.1f}".format (tax2))
    print("Податок від суми заробітної плати роботи типу C становить 30%= {:.1f} \n".format (tax3))

funtion_tax()

def funtion_salary():
    print("Вся сума заробітної плати роботи типу А становить={:.1f}".format (salary1 - tax1))
    print("Вся сума заробітної плати роботи типу B становить={:.1f}".format (salary2 - tax2))
    print("Вся сума заробітної плати роботи типу C становить={:.1f}".format (salary3 - tax3))

funtion_salary()
