def space_acquaintance(space_from, space_to ):
  min_Acquaintance_sum = None
  for i in range(len(space_from)):
    acquaintances = []
    Astronuat3= None
    Astronuat2 = space_from[i]
    Astronuat1 = space_to[i]
    Trio_acquaintances = []
    if Astronuat2 == Astronuat1:
      pass
    else:
      for j in range(len(space_from)):
        if j == i:
          pass
        elif space_to[j] == Astronuat1:
          acquaintances.append(space_from[j])
        elif space_from[j] == Astronuat2:
          acquaintances.append(space_to[j])
      print(acquaintances)
      for k in acquaintances:
        if Astronuat3 == k:
          pass
        elif acquaintances.count(k) >1:
          Astronuat3 = k
          for j in range(len(space_from)):
            if Trio_acquaintances.count(j) > 0 :
              pass
            elif space_to[j] == Astronuat1:
              Trio_acquaintances.append(space_to[j])
            elif space_to[j] == Astronuat2:
              Trio_acquaintances.append(space_to[j])
            elif space_to[j] == Astronuat3:
              Trio_acquaintances.append(space_to[j])
            elif space_from[j] == Astronuat1:
              Trio_acquaintances.append(space_to[j])
            elif space_from[j] == Astronuat2:
              Trio_acquaintances.append(space_to[j])
            elif space_from[j] == Astronuat3:
              Trio_acquaintances.append(space_to[j])
      if min_Acquaintance_sum == None: 
        min_Acquaintance_sum = len(Trio_acquaintances)
      elif min_Acquaintance_sum > len(Trio_acquaintances);
        min_Acquaintance_sum = len(Trio_acquaintances)
              
  return min_Acquaintance_sum
