def interception_losses(model_period):
    
    import pandas as pd
    
    I_loss = pd.Series([0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.16, 0.15, 0.14, 0.13, 0.12])
    daily_losses = pd.Series(index = model_period)
    monthly_losses = daily_losses.groupby(pd.Grouper(freq = 'M')).mean()
    monthly_losses = pd.Series(pd.np.tile(I_loss, round(len(model_period)/365)), index = monthly_losses.index)
    days = pd.Series(monthly_losses.index.daysinmonth)
    x = pd.Series(0.11)
    monthly_losses = monthly_losses.append(x)
    x = pd.Series(1)
    days = x.append(days)
    days = days.cumsum()
    day_seq = pd.Series(range(1, len(model_period) + 2))
    monthly_losses.index = days
    x = pd.Series(monthly_losses, index = day_seq)
    x = x.interpolate()
    daily_losses = list(x[0:len(model_period)])
    return(daily_losses);
