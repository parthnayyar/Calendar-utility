import calendar as cal

def year(year):
    all_dates=[]
    def dates(number_of_days, month):
        values=[]
        for date in range(1, number_of_days+1):
            if len(str(month))==1:
                if len(str(date))==1:
                    values.append(tuple([str(year)+'_0'+str(month)+'_0'+str(date)]))
                else:
                    values.append(tuple([str(year)+'_0'+str(month)+'_'+str(date)]))
            else:
                if len(str(date))==1:
                    values.append(tuple([str(year)+'_'+str(month)+'_0'+str(date)]))
                else:
                    values.append(tuple([str(year)+'_'+str(month)+'_'+str(date)]))
        return(values)
    
    all_dates.extend(dates(31,1))
    if cal.isleap(year):
        all_dates.extend(dates(29,2))
    else:
        all_dates.extend(dates(28,2))
    all_dates.extend(dates(31,3))
    all_dates.extend(dates(30,4))
    all_dates.extend(dates(31,5))
    all_dates.extend(dates(30,6))
    all_dates.extend(dates(31,7))
    all_dates.extend(dates(31,8))
    all_dates.extend(dates(30,9))
    all_dates.extend(dates(31,10))
    all_dates.extend(dates(30,11))
    all_dates.extend(dates(31,12))
    return(all_dates)
