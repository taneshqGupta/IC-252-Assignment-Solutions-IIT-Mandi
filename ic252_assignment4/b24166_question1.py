import random
import matplotlib.pyplot as plt
from collections import Counter
from math import comb

class UrnSimulation:
    def __init__(self, whitex=4, blackx=6, draws=5, trials=1000):
        self.whitex = whitex
        self.blackx = blackx
        self.total = whitex + blackx
        self.draws = draws
        self.trials = trials
        self.results = []

    def simulate(self):
        for _ in range(self.trials):
            sample = random.sample(["W"] * self.whitex + ["B"] * self.blackx, self.draws)
            self.results.append(sample.count("W"))

    def estimate_distribution(self):
        counter = Counter(self.results)
        estimated_probs = {x: count / self.trials for x, count in sorted(counter.items())}
        return estimated_probs

    def theoretical_probability(self, k):
        return (comb(self.whitex, k) * comb(self.blackx, self.draws - k)) / comb(self.total, self.draws)

    def plot_distribution(self):
        estimated_probs = self.estimate_distribution()
        theoretical_probs = [self.theoretical_probability(k) for k in range(self.draws + 1)]
        
        plt.bar(estimated_probs.keys(), estimated_probs.values(), label="Estimated")
        plt.plot(theoretical_probs, marker="X", color="pink", label="Theoretical")
        plt.xlabel("Number of Whitex Balls Drawn (X)")
        plt.ylabel("Probability")
        plt.legend()
        plt.title("Estimated vs. Theoretical Probability Distribution of X")
        plt.show()

simulation = UrnSimulation()
simulation.simulate()
print(simulation.estimate_distribution())
for _ in range(simulation.draws+1): print(simulation.theoretical_probability(_))
simulation.plot_distribution()

