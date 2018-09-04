import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\danie\\Documents\\university\\research\\case_studies\\Waidhofen\\LuKARS\\input_data')

### import data
precip      = np.loadtxt('kerschbaum_py.csv', skiprows = 1, usecols = 1, delimiter = ';')
Q_obs       = np.loadtxt('kerschbaum_py.csv', skiprows = 1, usecols = 2, delimiter = ';')
temp        = np.loadtxt('kerschbaum_py.csv', skiprows = 1, usecols = 3, delimiter = ';')

### model application Kerschbaum spring
period      = model_period('01/01/2001', '31/12/2016', 'D')
melt        = t_index_model(temp, 4, 0.5)
et          = et_model(period, temp)
intercep    = interception_losses(period)
sns_term    = sink_n_source(precip, et_model = et, snow_model = melt, \
                            interception_losses = intercep, interception_threshold = 5, \
                            temperature_ts = temp, t_threshold = 0.5)
sns_term_Q  = sink_n_source(precip, et_model = et, snow_model = melt, temperature_ts = temp,\
                            t_threshold = 0.5)
input_param = np.loadtxt('kerschbaum_input.txt', skiprows = 0, usecols = 1, delimiter = ';')
model_run   = lukars(sns_term_Q, sns_term, sns_term, sns_term, input_param)

### plot observed and simulated discharge time series
plt.figure()
plt.plot(period[1827:2556], model_run[1827:2556], color = 'blue')
plt.plot(period[1827:2556], Q_obs[1827:2556], color = 'red')
