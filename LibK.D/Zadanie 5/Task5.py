import math

def cycle():
    sum1 = 8.81
    sum2 =  0.07929
    print("1 Пик = {:.3f}".format (sum1), "Л = {:.3f}".format (sum2), "Сака") 
    for i in range(int(input("Введить кількість операцій:"))):
        sum1 += 8.81
        sum2 += 0.07929
        print(1+i+1,"Пик = {:.3f}".format (sum1), "Л = {:.3f}".format (sum2), "Сака") 

cycle()
