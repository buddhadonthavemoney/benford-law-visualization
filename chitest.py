def chitest(obs_value,exp_value):
    a=0
    chi=0

    for x in obs_value :
        chi= chi+  ((x-exp_value[a])*(x-exp_value[a])/exp_value[a])
      
        a+=1

    return chi
