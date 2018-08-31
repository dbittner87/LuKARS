def t_index_model(model_period, temperature_ts, melt_factor, t_threshold):

    import pandas as pd
    temp = temperature_ts
    mf = melt_factor
    t = t_threshold
    m_rate = {}

    for i in range(len(temp)):
        if(temp[i] <= t):
            m_rate[i] = 0
        else:
            m_rate[i] = mf * (temp[i] - t)
            
    m_rate = pd.Series(m_rate)
    m_rate.index = range(len(model_period))
    return(m_rate);