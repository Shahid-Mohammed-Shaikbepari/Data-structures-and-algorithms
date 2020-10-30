def getTotalDays_Years(startYear, endYear):
    totalDays = 0
    if endYear - startYear <= 0:
        return 0
    for y in range(startYear, endYear):
        if NumDaysInMonth(2, y) == 29:
            totalDays += 366
        else:
            totalDays += 365
    return totalDays

def getTotalDays_Months(startYear, startMonth, endMonth):
    totalDays = 0
    if startMonth <= endMonth:
        startMonth += 12
    for m in range(startMonth, endMonth):
        month = m % 12
        if month == 0:
            startYear += 1
            month = 12
        totalDays += NumDaysInMonth(month, startYear)
    return totalDays

def getToatalDays_Days(startYear, startMonth, startDate, endDate ):
    totalDays = 0
    if startDate <= endDate:
        return endDate - startDate
    else:
        return (NumDaysInMonth(startMonth, startYear) - startDate) + endDate



def NumDaysBetween(y1,m1,d1,y2,m2,d2):
    result = 0
    EndYear = EndMonth = None
    if m1 < m2:
        EndYear = y2
    else:
        if m1 == m2 and d1 <= d2:
            EndYear = y2
        else:
            EndYear = y2-1
    if d1 <= d2:
        EndMonth = m2
    else:
        EndMonth = m2-1

    result += getTotalDays_Years(y1, EndYear)
    result += getTotalDays_Months(y1, m1, EndMonth)
    result += getToatalDays_Days(y1, m1, d1, d2)
    return result
