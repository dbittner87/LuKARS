def t_index_model(temperature_ts, melt_factor, t_threshold):

    temp   = temperature_ts
    mf     = melt_factor
    t      = t_threshold
    m_rate = [0] * len(temp)

    for i in range(len(temp)):
        if(temp[i] <= t):
            m_rate[i] = 0
        else:
            m_rate[i] = mf * (temp[i] - t)
            
    return(m_rate);
