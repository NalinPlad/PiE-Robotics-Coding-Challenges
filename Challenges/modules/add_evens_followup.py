def add_evens2(nums2):
	added = 0
	numsString = str(nums2)
	for j in range(len(numsString)):
		if j % 2 == 0 :
		  added += int(numsString[j])
		
	return added
