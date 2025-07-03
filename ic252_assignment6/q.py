import math
import random
import matplotlib.pyplot as plt

class Santa: 
    def __init__(self, trials):
        self.trials = trials
        self.mu = 0.75
        self.n = 15
        self.p = 0.25

    def binomial_inverse_transform(self):
        samples = []  
        for _ in range(self.trials):  
            U = random.uniform(0, 1)
            cumulative_prob = 0
            k = 0  
            while U > cumulative_prob:  
                cumulative_prob += (math.comb(self.n, k) * (self.p ** k) * ((1 - self.p) ** (self.n - k)))
                k += 1  
            samples.append(k - 1)  
        mean_value = sum(samples) / len(samples)  
        return samples, mean_value  

    def poisson_knuth(self):
        samples = []
        for _ in range(self.trials):
            L = math.exp(-self.mu)
            k = 0
            p = 1
            while p > L:
                p *= random.uniform(0, 1)
                k += 1
            samples.append(k - 1)  
        mean_value = sum(samples) / len(samples)  
        return samples, mean_value  

    def plot_graphs(self):
        binomial_samples, binomial_mean = self.binomial_inverse_transform()
        poisson_samples, poisson_mean = self.poisson_knuth()

        print("Mean of Binomial(15, 0.25):", binomial_mean)
        print("Mean of Poisson(0.75):", poisson_mean)

        # Binomial Histogram
        plt.subplot(1, 2, 1)
        plt.hist(binomial_samples, bins=range(min(binomial_samples), max(binomial_samples) + 1), color='Green', edgecolor='White')
        plt.title(f"Binomial(15, 0.25) Distribution\nMean: {binomial_mean:.4f}")
        plt.xlabel("Value")
        plt.ylabel("Probability")

        # Poisson Histogram
        plt.subplot(1, 2, 2)
        plt.hist(poisson_samples, bins=range(min(poisson_samples), max(poisson_samples) + 1), color='Green', edgecolor='White')
        plt.title(f"Poisson(μ=0.75) Distribution\nMean: {poisson_mean:.4f}")
        plt.xlabel("Value")
        plt.ylabel("Probability")

        plt.tight_layout()
        plt.show()

exp = Santa(10000)
exp.plot_graphs()
