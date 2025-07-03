import random

n = 10000

bothsame = 0
sumgreaterthan9 = 0

for i in range(n):
	a1 = random.randint(1, 6)
	a2 = random.randint(1, 6)

	if(a1 == a2): bothsame+=1
	if((a1 + a2) > 9): sumgreaterthan9+=1

probsame = bothsame/n

probgreaterthan9 = sumgreaterthan9/n

print("Probability of both being equal: ", probsame, "\nProbability of the sum being greater than 9: ", probgreaterthan9)


# cases of equal : 6/36 = 0.16666666

# cases of sum being greater than 9 : 
#	(4, 6)
#   (5, 5) (5, 6)
# 	(6, 4) (6, 5) (6, 6)
#   ans = 6/36 = 0.1666666666666
  