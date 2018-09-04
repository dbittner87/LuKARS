def sink_n_source(precipitation_ts, et_model = None, snow_model = None, \
                  interception_losses = None, interception_threshold = None, \
                  temperature_ts = None, t_threshold = None):
        
    if et_model is None and snow_model is None and interception_losses is None:
        x = list(precipitation_ts)
    
    elif et_model is None and snow_model is None:
        precipitation = list(precipitation_ts)
        x = precipitation_ts * interception_losses
        
        if interception_threshold is None:
                    x = precipitation - x
        else:
                    x[x > interception_threshold] = interception_threshold
                    x = precipitation - x
                    
    elif snow_model is None and interception_losses is None:
        x = precipitation_ts - et_model
        x = list(x)
        
    elif et_model is None and interception_losses is None:
        temp = temperature_ts
        precipitation = precipitation_ts
        melt_x = [0] * len(precipitation_ts)
        x = [0] * len(precipitation_ts)
        x[0] = 0
        for i in range(len(precipitation_ts)-1):
                if(temp[i] < t_threshold):
                    melt_x[i] = 0
                    x[i+1]  = x[i] + precipitation[i+1]

                elif(x[i] >= snow_model[i]):
                    melt_x[i] = snow_model[i]
                    x[i+1]  = x[i] - snow_model[i]

                else:
                    melt_x[i] = x[i]
                    x[i+1]  = 0

        x[0] = 0
        
        for i in range(len(precipitation_ts)-1):
                if(temp[i] < t_threshold):
                    x[i] = 0

                elif(melt_x[i] > 0):
                    x[i] = melt_x[i] + precipitation[i]

                else:
                    x[i] = precipitation[i]
                    
                    
    elif interception_losses is None:
        temp = temperature_ts
        precipitation = precipitation_ts
        melt_x = [0] * len(precipitation_ts)
        x = [0] * len(precipitation_ts)
        x[0] = 0
        for i in range(len(precipitation_ts)-1):
                if(temp[i] < t_threshold):
                    melt_x[i] = 0
                    x[i+1]  = x[i] + precipitation[i+1]

                elif(x[i] >= snow_model[i]):
                    melt_x[i] = snow_model[i]
                    x[i+1]  = x[i] - snow_model[i]

                else:
                    melt_x[i] = x[i]
                    x[i+1]  = 0
        
        for i in range(len(precipitation_ts)-1):
                if(temp[i] < t_threshold):
                    x[i] = 0

                elif(melt_x[i] > 0):
                    x[i] = melt_x[i] + precipitation[i]

                else:
                    x[i] = precipitation[i]
                     
        x = [a - b for a, b in zip(x,et_model)]
                    
    elif et_model is None:
        temp = temperature_ts
        precipitation = list(precipitation_ts)
        x = precipitation_ts * interception_losses
        
        if interception_threshold is None:
                    x = precipitation - x
        else:
                    x[x > interception_threshold] = interception_threshold
                    x = precipitation - x
                    
        precipitation = list(x)        
        melt_x = [0] * len(precipitation_ts)
        x = [0] * len(precipitation_ts)
        x[0] = 0
        
        for i in range(len(precipitation_ts)-1):
                if(temp[i] < t_threshold):
                    melt_x[i] = 0
                    x[i+1]  = x[i] + precipitation[i+1]

                elif(x[i] >= snow_model[i]):
                    melt_x[i] = snow_model[i]
                    x[i+1]  = x[i] - snow_model[i]

                else:
                    melt_x[i] = x[i]
                    x[i+1]  = 0
        
        for i in range(len(precipitation_ts)-1):
                if(temp[i] < t_threshold):
                    x[i] = 0

                elif(melt_x[i] > 0):
                    x[i] = melt_x[i] + precipitation[i]

                else:
                    x[i] = precipitation[i]
                    
                    
    else:
        temp = temperature_ts
        precipitation = list(precipitation_ts)
        x = precipitation_ts * interception_losses
        
        if interception_threshold is None:
                    x = precipitation - x
        else:
                    x[x > interception_threshold] = interception_threshold
                    x = precipitation - x
                    
        precipitation = list(x)        
        melt_x = [0] * len(precipitation_ts)
        x = [0] * len(precipitation_ts)
        x[0] = 0
        
        for i in range(len(precipitation_ts)-1):
                if(temp[i] < t_threshold):
                    melt_x[i] = 0
                    x[i+1]  = x[i] + precipitation[i+1]

                elif(x[i] >= snow_model[i]):
                    melt_x[i] = snow_model[i]
                    x[i+1]  = x[i] - snow_model[i]

                else:
                    melt_x[i] = x[i]
                    x[i+1]  = 0
        
        for i in range(len(precipitation_ts)-1):
                if(temp[i] < t_threshold):
                    x[i] = 0

                elif(melt_x[i] > 0):
                    x[i] = melt_x[i] + precipitation[i]

                else:
                    x[i] = precipitation[i]
        
        x = [a - b for a, b in zip(x,et_model)]
        
    return(x);
