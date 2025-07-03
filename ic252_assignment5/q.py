import random

# -- mathematical approach

#there are n different people with n different gifts st. each gift is associated to one person.
#to find number of ways atleast j employees recieve their own gift:
#       we must find the complement of the probability of less than j people recieving their own gifts.
#       essentially find P(i) for i ranging from 0 to j-1 where P(i) stands for probability of i people getting their own gift.
#       then answer is 1 - sum(p(i))
#   P(i) = (assign each of the i people their own gift [only one way to do so]) * (assign the rest of people the wrong gifts [derangements])
#if j>n/2 its better to calculate normally, but if j<n/2 its better to use 1 - p(complement)

# -- simulation approach

class santa:
    def __init__(self, n, j):
        self.n = n
        self.j = j

    def sim(self, trials=10000):
        #we will create a list where all values are corresponding to the respective index
        #meaning initially each gift is given to the correct person
        #then we will shuffle the list and iterate through it to see which values are correct
        #if the number of correct gifts are greater than or equal to j, then we will add to our results variable
        #answer would be results/trials
        
        self.trials = trials
        results = 0
        lst = list(range(0, self.n))
        for _ in range(self.trials):
            subres = 0
            random.shuffle(lst)
            for i in range(self.n):
                if (lst[i] == i): subres += 1
            if (subres >= self.j):  results += 1    
        return results/self.trials


complan = santa(100, 2)
ans = complan.sim()
print("probability through simulations is ", ans)


