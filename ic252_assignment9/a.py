import numpy as np
import random

class Santa:
    def __init__(self, n, N):
        self.n = n
        self.N = N
        self.T_vals = []

        self.theorE = (2 * n) / (2 * n - 1)


    def shufflex(self):
        people = [(i, 0) for i in range(self.n)] + [(i, 1) for i in range(self.n)]
        random.shuffle(people)
        return people

    def countx(self, seating):
        count = 0
        for i in range(len(seating)):
            if seating[i][0] == seating[(i + 1) % len(seating)][0]:
                count += 1
        return count

    def sim(self):
        for _ in range(self.N):
            seats = self.shufflex()
            T = self.countx(seats)
            self.T_vals.append(T)

        self.simulated_E = np.mean(self.T_vals)
        self.simulated_Var = np.var(self.T_vals)

    def results(self):
        print(f"Simulated E(T):     {self.simulated_E:.4f}")
        print(f"Theoretical E(T):   {self.theorE:.4f}")
        print(f"Simulated Var(T):   {self.simulated_Var:.4f}")

exp = Santa(n=50, N=10000)
exp.sim()
exp.results()
