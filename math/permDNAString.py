def genSet(set, k):   
    n = len(set)  
    printAllKLengthRec(set, "", n, k) 
  
def printAllKLengthRec(set, prefix, n, k): 
    if (k == 0) : 
        ls.append(prefix) 
        return

    for i in range(n): 
        newPrefix = prefix + set[i] 
        printAllKLengthRec(set, newPrefix, n, k - 1) 


bank = ['A','T','C','G'] 
for i in range(10):
	ls = []
	genSet(bank, i) 
	count = 0
	for dna in ls:
		if "AA" not in dna:
			count += 1
	compliment = 4**(i)-count
	ratio = compliment / (4**i)
	print(i, "->", count, "compliment = ", compliment, "ratio=", ratio)
