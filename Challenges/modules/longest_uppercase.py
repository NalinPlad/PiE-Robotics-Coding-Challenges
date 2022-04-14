def longest_uppercase(input,k):
  final_out = 0
  for i in input:
    test_letters = i
    for j in input:
      if  len(test_letters) == k :
        break
      if test_letters.find(j) >= 0:
        pass
      else:
        test_letters += j
    max = 0
    count = 0
    for m in input :
      if test_letters.find(m) == -1:
        if count > max:
          max = count
        count = 0
      else:
        count += 1 
    if len(input) <= k:
      return len(input)
    if final_out < max:
      final_out = max
  return final_out
