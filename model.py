def lukars(sink_n_source_hyd_1, sink_n_source_hyd_2, sink_n_source_hyd_3,\
           sink_n_source_hyd_4, input_parameters, time_step = 1):
        
    sns1        = list(sink_n_source_hyd_1)
    sns2        = list(sink_n_source_hyd_2)
    sns3        = list(sink_n_source_hyd_3)
    sns4        = list(sink_n_source_hyd_4)
    
    a_hyd1      = input_parameters[0] * input_parameters[3]  
    a_hyd2      = input_parameters[0] * input_parameters[13]
    a_hyd3      = input_parameters[0] * input_parameters[23]
    a_hyd4      = input_parameters[0] * input_parameters[33]
    
    Q_tot       = [0] * (len(sns1) + 1)
    Q_tot[0]    = 1
    Q_is        = [0] * (len(sns1) + 1)
    Q_is[0]     = 1
    Q_b         = [0] * (len(sns1) + 1)
    Q_b[0]      = 1
    Q_e         = [0] * (len(sns1) + 1)
    Q_e[0]      = 1
    Q_sec       = [0] * (len(sns1) + 1)
    Q_sec[0]    = 1
    
    # Linear storage
    E_b         = [0] * (len(sns1) + 1)
    E_b[0]      = input_parameters[1]
    k_b         = input_parameters[2]       
    
    ### Hydrotope 1 #####
    # Non-Linear storage
    l_hyd_1     = input_parameters[4]
    k_e_1       = input_parameters[5] / l_hyd_1  
    E_1         = [0] * (len(sns1) + 1)
    E_1[0]      = input_parameters[6]    
    e_min_1     = input_parameters[7]    
    e_max_1     = input_parameters[8]    
    alpha_1     = input_parameters[9]
    Q_e_1       = [0] * (len(sns1) + 1)
    Q_e_1[0]    = 1

    # to Baseflow storage
    k_is_1      = input_parameters[10]   
    Q_is_1      = [0] * (len(sns1) + 1)
    Q_is[0]     = 1

    # secondary springs
    k_sec_1     = input_parameters[11]
    e_sec_1     = input_parameters[12]       
    Q_sec_1     = [0] * (len(sns1) + 1)
    Q_sec_1[0]  = 1


    ### Hydrotope 2 #####
    l_hyd_2     = input_parameters[14]
    k_e_2       = input_parameters[15] / l_hyd_2   
    E_2         = [0] * (len(sns1) + 1)
    E_2[0]      = input_parameters[16]
    e_min_2     = input_parameters[17]
    e_max_2     = input_parameters[18]
    alpha_2     = input_parameters[19]
    Q_e_2       = [0] * (len(sns1) + 1)
    Q_e_2[0]    = 1

    # to Baseflow storage
    k_is_2      = input_parameters[20]
    Q_is_2      = [0] * (len(sns1) + 1)
    Q_is_2[0]   = 1

    # secondary springs
    k_sec_2     = input_parameters[21]
    e_sec_2     = input_parameters[22]
    Q_sec_2     = [0] * (len(sns1) + 1)
    Q_sec_2[0]  = 1


    ### Hydrotope 3 ##### 
    l_hyd_3     = input_parameters[24]
    k_e_3       = input_parameters[25] / l_hyd_3   
    E_3         = [0] * (len(sns1) + 1)
    E_3[0]      = input_parameters[26]
    e_min_3     = input_parameters[27]    
    e_max_3     = input_parameters[28]    
    alpha_3     = input_parameters[29]
    Q_e_3       = [0] * (len(sns1) + 1)
    Q_e_3[0]    = 1

    # to Baseflow storage
    k_is_3      = input_parameters[30]
    Q_is_3      = [0] * (len(sns1) + 1)
    Q_is_3[0]   = 1

    # secondary springs
    k_sec_3     = input_parameters[31]
    e_sec_3     = input_parameters[32]
    Q_sec_3     = [0] * (len(sns1) + 1)
    Q_sec_3[0]  = 1


    ### Hydrotope 4 #####
    l_hyd_4     = input_parameters[34]
    k_e_4       = input_parameters[35] / l_hyd_4   
    E_4         = [0] * (len(sns1) + 1)
    E_4[0]      = input_parameters[36]
    e_min_4     = input_parameters[37]
    e_max_4     = input_parameters[38]
    alpha_4     = input_parameters[39]
    Q_e_4       = [0] * (len(sns1) + 1)
    Q_e_4[0]    = 1

    # to Baseflow storage
    k_is_4      = input_parameters[40]    
    Q_is_4      = [0] * (len(sns1) + 1)
    Q_is_4[0]   = 1

    # secondary springs
    k_sec_4     = input_parameters[41]
    e_sec_4     = input_parameters[42]
    Q_sec_4     = [0] * (len(sns1) + 1)
    Q_sec_4[0]  = 1

    #############################################
    ### Model ###################################
    #############################################
    
    for i in range(len(sns1)):
      
      #############################################
      ### Storages ################################
      #############################################
      
      # non-linear, Hydrotop 1
      if((E_1[i] + (sns1[i] - ((Q_sec_1[i] + Q_is_1[i] + Q_e_1[i]) / a_hyd1)) * time_step) >= 0):
        E_1[i+1] = E_1[i] + (sns1[i] - ((Q_sec_1[i] + Q_is_1[i] + Q_e_1[i]) / a_hyd1)) * time_step
    
      else:
        E_1[i+1] = 0
        sns1[i]    = sns1[i] - (E_1[i] + (sns1[i] - ((Q_sec_1[i] + Q_is_1[i] + Q_e_1[i]) / 
                                                              a_hyd1)) * time_step)
      
      
      # non-linear, Hydrotop 2
      if((E_2[i] + (sns2[i] - ((Q_sec_2[i] + Q_is_2[i] + Q_e_2[i]) / a_hyd2)) * time_step) >= 0):
        E_2[i+1] = E_2[i] + (sns2[i] - ((Q_sec_2[i] + Q_is_2[i] + Q_e_2[i]) / a_hyd2)) * time_step
    
      else:
        E_2[i+1] = 0
        sns2[i]    = sns2[i] - (E_2[i] + (sns2[i] - ((Q_sec_2[i] + Q_is_2[i] + Q_e_2[i]) / 
                                                              a_hyd2)) * time_step)
      
      # non-linear, Hydrotop 3
      if((E_3[i] + (sns3[i] - ((Q_sec_3[i] + Q_is_3[i] + Q_e_3[i]) / a_hyd3)) * time_step) >= 0):
        E_3[i+1] = E_3[i] + (sns3[i] - ((Q_sec_3[i] + Q_is_3[i] + Q_e_3[i]) / a_hyd3)) * time_step
    
      else:
        E_3[i+1] = 0
        sns3[i]    = sns3[i] - (E_3[i] + (sns3[i] - ((Q_sec_3[i] + Q_is_3[i] + Q_e_3[i]) / 
                                                              a_hyd3)) * time_step)
      
      # non-linear, Hydrotop 4
      if((E_4[i] + (sns4[i] - ((Q_sec_4[i] + Q_is_4[i] + Q_e_4[i]) / a_hyd4)) * time_step) >= 0):   
        E_4[i+1] = E_4[i] + (sns4[i] - ((Q_sec_4[i] + Q_is_4[i] + Q_e_4[i]) / a_hyd4)) * time_step
      
      else:
        E_4[i+1] = 0
        sns4[i]    = sns4[i] - (E_4[i] + (sns4[i] - ((Q_sec_4[i] + Q_is_4[i] + Q_e_4[i]) / 
                                                              a_hyd4)) * time_step)
      
      # linear (baseflow storage)
      E_b[i+1] = E_b[i] + ((Q_is[i] - Q_b[i]) / input_parameters[0]) * time_step
      
      #############################################
      ### Flows ###################################
      #############################################
      
      # Q secondary springs, Hydrotop 1
      if(E_1[i+1] >= e_sec_1):
        Q_sec_1[i+1] = k_sec_1 * a_hyd1 * (E_1[i+1] - e_sec_1)
      
      else:
        Q_sec_1[i+1] = 0 
      
      # Q secondary springs, Hydrotop 2
      if(E_2[i+1] >= e_sec_2):
        Q_sec_2[i+1] = k_sec_2 * a_hyd2 * (E_2[i+1] - e_sec_2)
    
      else:
        Q_sec_2[i+1] = 0 
      
      # Q secondary springs, Hydrotop 3
      if(E_3[i+1] >= e_sec_3):
        Q_sec_3[i+1] = k_sec_3 * a_hyd3 * (E_3[i+1] - e_sec_3)
      
      else:
        Q_sec_3[i+1] = 0 
      
      # Q secondary springs, Hydrotop 4
      if(E_4[i+1] >= e_sec_4):
        Q_sec_4[i+1] = k_sec_4 * a_hyd4 * (E_4[i+1] - e_sec_4)
      
      else:
        Q_sec_4[i+1] = 0 
      
      Q_sec[i+1] = Q_sec_1[i+1] + Q_sec_2[i+1] + Q_sec_3[i+1] + Q_sec_4[i+1]
      
      # Q inter-storage, Hydrotop 1
      Q_is_1[i+1] = a_hyd1 * k_is_1 * E_1[i+1]
      
      # Q inter-storage, Hydrotop 2
      Q_is_2[i+1] = a_hyd2 * k_is_2 * E_2[i+1]
      
      # Q inter-storage, Hydrotop 3
      Q_is_3[i+1] = a_hyd3 * k_is_3 * E_3[i+1]
      
      # Q inter-storage, Hydrotop 4
      Q_is_4[i+1] = a_hyd4 * k_is_4 * E_4[i+1]
      
      # total
      Q_is[i+1]   = Q_is_1[i+1] + Q_is_2[i+1] + Q_is_3[i+1] + Q_is_4[i+1]
      
      
      # Q baseflow
      Q_b[i+1] = input_parameters[0] * k_b * E_b[i+1]
      
      
      # Hysteresis function, Hydrotop 1
      if(E_1[i+1] >= e_min_1 and Q_e_1[i] > 0):
        Q_e_1[i+1] = (((E_1[i+1] - e_min_1)/(e_max_1 - e_min_1))**alpha_1) * k_e_1 * a_hyd1
        
      elif(E_1[i+1] >= e_max_1 and Q_e_1[i] <= 0):
        Q_e_1[i+1] = (((E_1[i+1] - e_min_1)/(e_max_1 - e_min_1))**alpha_1) * k_e_1 * a_hyd1
        
      else:
        Q_e_1[i+1] = 0 
      
      
      # Hysteresis function, Hydrotop 2
      if(E_2[i+1] >= e_min_2 and Q_e_2[i] > 0):
        Q_e_2[i+1] = (((E_2[i+1] - e_min_2)/(e_max_2 - e_min_2))**alpha_2) * k_e_2 * a_hyd2
      
      elif(E_2[i+1] >= e_max_2 and Q_e_2[i] <= 0):
        Q_e_2[i+1] = (((E_2[i+1] - e_min_2)/(e_max_2 - e_min_2))**alpha_2) * k_e_2 * a_hyd2
      
      else:
        Q_e_2[i+1] = 0 
      
      
      # Hysteresis function, Hydrotop 3
      if(E_3[i+1] >= e_min_3 and Q_e_3[i] > 0):
        Q_e_3[i+1] = (((E_3[i+1] - e_min_3)/(e_max_3 - e_min_3))**alpha_3) * k_e_3 * a_hyd3
      
      elif(E_3[i+1] >= e_max_3 and Q_e_3[i] <= 0): 
        Q_e_3[i+1] = (((E_3[i+1] - e_min_3)/(e_max_3 - e_min_3))**alpha_3) * k_e_3 * a_hyd3
      
      else:
        Q_e_3[i+1] = 0 
       
      
      # Hysteresis function, Hydrotop 4
      if(E_4[i+1] >= e_min_4 and Q_e_4[i] > 0):
        Q_e_4[i+1] = (((E_4[i+1] - e_min_4)/(e_max_4 - e_min_4))**alpha_4) * k_e_4 * a_hyd4
      
      elif(E_4[i+1] >= e_max_4 and Q_e_4[i] <= 0):
        Q_e_4[i+1] = (((E_4[i+1] - e_min_4)/(e_max_4 - e_min_4))**alpha_4) * k_e_4 * a_hyd4
      
      else:
        Q_e_4[i+1] = 0 
      
        
      Q_e[i+1]   = Q_e_1[i+1] + Q_e_2[i+1] + Q_e_3[i+1] + Q_e_4[i+1]
      
      Q_tot[i+1] = Q_e[i+1] + Q_b[i+1]
      
    Q_tot[:]     = [x / 86400 for x in Q_tot]
    Q_tot        = Q_tot[0:len(sns1)]
    return(Q_tot);
