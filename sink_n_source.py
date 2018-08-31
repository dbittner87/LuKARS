def sink_n_source(model_period, precipitation_ts, et_model = None, snow_model = None, \
                  interception_losses = None, interception_threshold = None, \
                  temperature_ts = None, t_threshold = None):
    
    import pandas as pd
    
    if et_model is None and snow_model is None and interception_losses is None:
        x = pd.Series(precipitation_ts, index = model_period)
    
    elif et_model is None and snow_model is None:
        precipitation = pd.Series(precipitation_ts, index = model_period)
        x = pd.Series(precipitation_ts, index = model_period) * interception_losses
        
        if interception_threshold is None:
                    x = precipitation - x
        else:
                    x[x > interception_threshold] = interception_threshold
                    x = precipitation - x
                    
    elif snow_model is None and interception_losses is None:
        x = pd.Series(precipitation_ts, index = model_period) - et_model
        
    elif et_model is None and interception_losses is None:
        precipitation = pd.Series(precipitation_ts, index = model_period)
        melt_x = pd.Series(index = range(len(model_period)))
        x = pd.Series(index = range(len(model_period)))
        x[0] = 0
        for i in range(len(model_period)-1):
                if(temp[i] < t_threshold):
                    melt_x[i] = 0
                    x[i+1]  = x[i] + precipitation[i+1]

                elif(x[i] >= melt[i]):
                    melt_x[i] = snow_model[i]
                    x[i+1]  = x[i] - snow_model[i]

                else:
                    melt_x[i] = x[i]
                    x[i+1]  = 0

        x = pd.Series(index = range(len(model_period)))
        x[0] = 0
        
        for i in range(len(model_period)-1):
                if(temp[i] < t_threshold):
                    x[i] = 0

                elif(melt_x[i] > 0):
                    x[i] = melt_x[i] + precipitation[i]

                else:
                    x[i] = precipitation[i]
                    
        x.index = model_period 
        
    elif interception_losses is None:
        precipitation = pd.Series(precipitation_ts, index = range(len(model_period)))
        melt_x = pd.Series(index = range(len(model_period)))
        x = pd.Series(index = range(len(model_period)))
        x[0] = 0
        for i in range(len(model_period)-1):
                if(temp[i] < t_threshold):
                    melt_x[i] = 0
                    x[i+1]  = x[i] + precipitation[i+1]

                elif(x[i] >= melt[i]):
                    melt_x[i] = snow_model[i]
                    x[i+1]  = x[i] - snow_model[i]

                else:
                    melt_x[i] = x[i]
                    x[i+1]  = 0

        x = pd.Series(index = range(len(model_period)))
        x[0] = 0
        
        for i in range(len(model_period)-1):
                if(temp[i] < t_threshold):
                    x[i] = 0

                elif(melt_x[i] > 0):
                    x[i] = melt_x[i] + precipitation[i]

                else:
                    x[i] = precipitation[i]
                     
        x = x - et_model
                    
    elif et_model is None:
        precipitation = pd.Series(precipitation_ts, index = model_period)
        interception = pd.Series(precipitation_ts, index = model_period) * interception_losses
        
        if interception_threshold is None:
                    interception = precipitation - interception
        else:
                    interception[interception > interception_threshold] = interception_threshold
                    interception = precipitation - interception
                    
        precipitation = interception        
        melt_x = pd.Series(index = range(len(model_period)))
        x = pd.Series(index = range(len(model_period)))
        x[0] = 0
        
        for i in range(len(model_period)-1):
                if(temp[i] < t_threshold):
                    melt_x[i] = 0
                    x[i+1]  = x[i] + precipitation[i+1]

                elif(x[i] >= melt[i]):
                    melt_x[i] = snow_model[i]
                    x[i+1]  = x[i] - snow_model[i]

                else:
                    melt_x[i] = x[i]
                    x[i+1]  = 0

        x = pd.Series(index = range(len(model_period)))
        x[0] = 0
        
        for i in range(len(model_period)-1):
                if(temp[i] < t_threshold):
                    x[i] = 0

                elif(melt_x[i] > 0):
                    x[i] = melt_x[i] + precipitation[i]

                else:
                    x[i] = precipitation[i]
                    
        x.index = model_period 
                    
    else:
        precipitation = pd.Series(precipitation_ts, index = range(len(model_period)))
        interception = pd.Series(precipitation_ts, index = range(len(model_period))) * interception_losses
        
        if interception_threshold is None:
                    precipitation = precipitation - interception
        else:
                    interception[interception > interception_threshold] = interception_threshold
                    precipitation = precipitation - interception
                    
        melt_x = pd.Series(index = range(len(model_period)))
        x = pd.Series(index = range(len(model_period)))
        x[0] = 0
        
        for i in range(len(model_period)-1):
                if(temp[i] < t_threshold):
                    melt_x[i] = 0
                    x[i+1]  = x[i] + precipitation[i+1]

                elif(x[i] >= melt[i]):
                    melt_x[i] = snow_model[i]
                    x[i+1]  = x[i] - snow_model[i]

                else:
                    melt_x[i] = x[i]
                    x[i+1]  = 0

        x = pd.Series(index = range(len(model_period)))
        x[0] = 0
        
        for i in range(len(model_period)-1):
                if(temp[i] < t_threshold):
                    x[i] = 0

                elif(melt_x[i] > 0):
                    x[i] = melt_x[i] + precipitation[i]

                else:
                    x[i] = precipitation[i]
        
        x = x - et_model
        x.index = model_period 
      
    return(x);