#Analytical Approach
import math
#P(atleast 3 people sharing the same birthday) = 1 - P(0 people sharing the same birthday) - P(2 people sharing the same birthday)
# P(0) = (365 choose 25)*(25 factorial)/(365^25)
# P(2) --> there can be any number of pairs of people sharing the same birthday from 1 to 12.
# P(2) is the summation of all the possible cases of all the pairs divided by 365^25. Number of pairs can range from 1 to 12.
# ans = 1 - P(0) - P(2);

P_0 = (math.comb(365, 25)*(math.factorial(25)))/(365**25)
P_2 = 0
def group_of_2(n):
        return math.factorial(n)/((2**(n//2))*math.factorial(n//2))

i = 2
ways = 0
totalways = 365**25
while(i<=24):
    ways += math.comb(25, i)*group_of_2(i)*math.comb(365, i//2 + 25 - i)*math.factorial(25 - i + i//2)
    i+=2
P_2 = ways / totalways

ans = 1 - P_0 - P_2

print(f"The probability by mathematical analysis is {ans}")
    

#Monte Carlo Simulation
import random
from collections import Counter
testcases = 100000
atleast3 = 0
for _ in range(testcases):
    random_numbers = random.choices(range(1, 365), k=25)
    freq_table = Counter(random_numbers)
    maxi = 0
    for i, j in freq_table.items():
        if(j>maxi): maxi = j
    if(maxi>=3): atleast3 += 1
prob = atleast3/testcases
print(f"The probability by Monte Carlo Simulation is {prob}")
