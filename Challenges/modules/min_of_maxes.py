def min_of_maxes(nums,k):
  count = 0 
  highest = None
  lowest = None
  for i in nums:  
    count += 1
    if highest == None:
      highest = i
    if i > highest:
      highest = i 
    if count == k:
      if lowest == None:
        lowest = highest 
      if highest < lowest:
        lowest = highest 
      highest = None
      count = 0
  return lowest 
