import random
import math
import numpy as np

class CoupleSeatingSimulator:
    def __init__(self, n_couples=20, num_simulations=10000):
        self.n = n_couples
        self.N = num_simulations
        self.total_people = 2 * n_couples
        self.couples = [(2*i, 2*i + 1) for i in range(self.n)]
        self.sim_results = []

    def is_couple(self, a, b):
        return (a, b) in self.couples or (b, a) in self.couples

    def count_adjacent_couples(self, arrangement):
        count = 0
        for i in range(self.total_people):
            a = arrangement[i]
            b = arrangement[(i + 1) % self.total_people]
            if self.is_couple(a, b):
                count += 1
        return count // 2  # since each couple will be counted twice in the loop

    def run_simulation(self):
        for _ in range(self.N):
            people = list(range(self.total_people))
            random.shuffle(people)
            T = self.count_adjacent_couples(people)
            self.sim_results.append(T)

    def get_expectation(self):
        return np.mean(self.sim_results)

    def get_variance(self):
        return np.var(self.sim_results)

    def theoretical_expectation(self):
        return self.n * (2 / (2 * self.n - 1))

    def theoretical_variance(self):
        p = 2 / (2 * self.n - 1)
        return self.n * p * (1 - p)

    def report(self):
        print(f"Simulated E(T): {self.get_expectation():.4f}")
        print(f"Theoretical E(T): {self.theoretical_expectation():.4f}")
        print(f"Simulated Var(T): {self.get_variance():.4f}")
        print(f"Theoretical Var(T): {self.theoretical_variance():.4f}")

a = CoupleSeatingSimulator()
print(a.get_expectation())
print(a.get_variance())