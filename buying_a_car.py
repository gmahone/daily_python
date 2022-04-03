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
