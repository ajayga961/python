from itertools import combinations
list=[-1,7,-9,4,-6]
print("positive combinations")
for r in range(1,len(list)+1):
    for combo in combinations(list,r):
        if all (num>0 for num in combo):
            print(combo)
    
    
