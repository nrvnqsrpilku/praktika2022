
import math
from array import array

def company_calculations():
    k = [1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001, 2002, 2003, 2004, 2005]
    sum = 0
    y = 0
    f = 0
    
    for i in range(0, 13):
        y = 100*(2 * math.sin(math.fabs(2 * k[i]))* math.cos(2 * k[i]) - 11.6 * math.sin(k[i]/ 0.41) )* k[i]
        f += y
        if y == sum:
            print("В цей рік фірма не мала прибутків та збитків:{:.0f}".format (k[i]), "," "   Фірма заробила = {:.1f}".format (y) )

        if y > sum:
            print("В цей рік фірма мала пибуток:{:.0f}".format (k[i]), "," "   Фірма заробила = {:.1f}".format (y) )

        if y < sum:
            print("В цей рік фірма мала збитки: {:.0f}".format (k[i]), "," "   Фірма заробила = {:.1f}".format (y) )
        
    
    if y < 0:
        y += y
    print("Всього збитків фірма мала:", "{:.0f}".format(y))
    if y > 0:
        y += y
    print("Всього прибутків фірма мала:", "{:.0f}".format(y))

company_calculations()









