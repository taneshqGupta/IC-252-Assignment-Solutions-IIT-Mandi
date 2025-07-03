import random

n = int(input("Enter the number of trials: "))

success = 0

#let 0 denote red and 1 denote blue
for _ in range(n):
	balls = [0]*50 + [1]*50
	fiveBalls = random.sample(balls, 5)

	red_balls = fiveBalls.count(0)
	blue_balls = fiveBalls.count(1)

	if (red_balls == 2) and (blue_balls == 3):
		success += 1

print("Required probability (3 blue_balls and 2 red_balls) :  ", success/n)


# probability = (50 choose 2)*(50 choose 3)/(100 choose 5)
# i.e; 1225 * 19600 / 75287520 = 0.318910757055087