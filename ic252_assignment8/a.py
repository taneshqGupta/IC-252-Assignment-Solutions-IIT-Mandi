import numpy as np
import matplotlib.pyplot as plt

class Santa:
    def __init__(self, gamma=2, n=100):
        self.gamma = gamma
        self.n = n
        self.X1 = None
        self.X2 = None
    
    def generate_samples(self):
        u = np.random.uniform(0, 1, self.n)
        x = -1/self.gamma * np.log(1 - u)
        return x
    
    def generate(self):
        self.X1 = self.generate_samples()
        self.X2 = self.generate_samples()
    
    def get_population_mean(self):
        return 1/self.gamma

    def get_sample_means(self):
        return np.mean(self.X1), np.mean(self.X2)
    
    def get_correlation(self):
        mean1, mean2 = self.get_sample_means()
        numerator = np.sum((self.X1 - mean1) * (self.X2 - mean2))
        denominator = np.sqrt(np.sum((self.X1 - mean1)**2) * np.sum((self.X2 - mean2)**2))

        return numerator/denominator
    
    def check_independence(self):
        marginal_1 = [np.sum(self.X1 <= i) / self.n for i in self.X1]
        marginal_2 = [np.sum(self.X2 <= i) / self.n for i in self.X2]
        marginal_product = marginal_1 * marginal_2
        joint = np.sum((self.X1 <= mean1) & (self.X2 <= mean2)) / self.n
        print(f"Joint Probabiity: {joint}")
        print(f"Product of Marginal Probabilities: {marginal_product}")
    
    
    def plot(self):

        #marginal histogram
        plt.subplot(1, 2, 1)
        plt.hist(self.X1, bins=20, alpha=0.3, label='X1', density=True, color='green')
        plt.hist(self.X2, bins=20, alpha=0.3, label='X2', density=True, color='black')
        plt.title("Marginal Distributions")
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.legend()

        #joint scatter plot
        plt.subplot(1, 2, 2)
        plt.scatter(self.X1, self.X2)
        plt.title("Joint Distribution: X1 vs X2")
        plt.xlabel('X1')
        plt.ylabel('X2')

        plt.show()
    
seed = np.random.randint(1, 100)
np.random.seed(seed)
Claus = Santa()
Claus.generate()
pop_mean = Claus.get_population_mean()
mean1, mean2 = Claus.get_sample_means()
correlation = Claus.get_correlation()

print(f"Population Mean: {pop_mean}")
print(f"Sample Mean 1: {mean1}")
print(f"Sample Mean 2: {mean2}")
print(f"Correlation: {correlation}")
Claus.check_independence()

Claus.plot()



