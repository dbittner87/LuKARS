def model_period(start_date, end_date, time_steps):
    
    import pandas as pd
    date_range = pd.date_range(start = start_date, end = end_date, freq = time_steps)
    return(date_range);