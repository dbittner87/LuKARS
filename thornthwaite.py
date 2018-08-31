def et_model(model_period, temperature_ts):
    
    import pandas as pd
    temp = pd.Series(temperature_ts, index = model_period)
    temp = temp.groupby(pd.Grouper(freq = 'M')).mean()
    heat_index = (temp/5)**1.514
    heat_index = heat_index.fillna(0)
    heat_index = heat_index.groupby(pd.Grouper(freq = 'Y')).sum()
    heat_index = heat_index.repeat(12)
    
    a = (0.000000675 * heat_index**3) - (0.000071 * heat_index**2) + (0.01792 * heat_index) + 0.49239
    pe = {}
    for i in range(len(temp)):
        if(temp[i] <= 0):
            pe[i] = 0
        else:
            pe[i] = 16 * ((10 * temp[i]) / heat_index[i])**a[i]

    pe = pd.Series(pe)
    pe = pe.fillna(0)
    
    days = pd.Series(temp.index.daysinmonth)
    pe_daily = {}
    
    for i in range(len(temp)):
        pe_daily[i] = pe[i] / days[i]
    
    x = pd.Series(15)
    days = x.append(days)
    days = days.cumsum()
    days = days[0:192]
    x = pd.Series(pe_daily)
    x.index = days
    day_seq = pd.Series(range(1, 5845))
    x = pd.Series(x, index = day_seq)
    x = x.interpolate()
    x = x.fillna(0)
    x.index = range(len(model_period))
    return(x);