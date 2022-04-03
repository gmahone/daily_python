def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    i = 0
    savedThisMonth = 0
    while (startPriceOld + savedThisMonth) < startPriceNew:
        i += 1
        if i % 2 == 0:
            percentLossByMonth += 0.5
        startPriceOld *= 1-(percentLossByMonth/100)
        startPriceNew *= 1-(percentLossByMonth/100)
        savedThisMonth += savingperMonth
    return [i, round(startPriceOld + savedThisMonth - startPriceNew)]


# other solutions

def nbMonths(oldCarPrice, newCarPrice, saving, loss):
    months = 0
    budget = oldCarPrice
    
    while budget < newCarPrice:
        months += 1
        if months % 2 == 0:
            loss += 0.5
        
        oldCarPrice *= (100 - loss) / 100
        newCarPrice *= (100 - loss) / 100
        budget = saving * months + oldCarPrice
    
    return [months, round(budget - newCarPrice)]

def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    i = 0
    while savingperMonth * i + startPriceOld < startPriceNew:
        if i % 2:
            percentLossByMonth += 0.5
        startPriceOld -= startPriceOld * 0.01 * percentLossByMonth
        startPriceNew -= startPriceNew * 0.01 * percentLossByMonth
        i += 1
    return [i, round(savingperMonth * i + startPriceOld - startPriceNew)]

x=nbMonths=lambda o,n,s,l,m=0,c=0:x(o-o*l/100,n-n*l/100,s,l+~c%2/2,m+s,c+1)if o-n+m<0else[c,round(o-n+m)]

def nbMonths(fltp1, fltp2, flts, fltl, i = 0):
    return [i, round(fltp1 + flts * i - fltp2, 0)] if fltp1 + flts * i - fltp2 >= 0 else nbMonths(fltp1 * (1 - fltl / 100 - 0.005 * int((i+1)/2)), fltp2 * (1 - fltl / 100 - 0.005 * int((i+1)/2)), flts, fltl, i+1)
