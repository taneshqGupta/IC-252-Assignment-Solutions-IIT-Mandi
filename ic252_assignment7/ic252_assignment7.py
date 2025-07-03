import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

class Santa:
    def __init__(self, lmbda, mu):
        self.lmbda = lmbda
        self.mu = mu
    
    def pdf(self, x):
        if x <= self.mu:
            return 0  
        return 2 * self.lmbda * (x - self.mu) * np.exp(-self.lmbda * ((x - self.mu) ** 2))
    
    def cdf(self, x):
        if x <= self.mu:
            return 0  
        result, _ = quad(self.pdf, self.mu, x)
        return result

    def integrand(self,x):
        return  x * self.pdf(x)

    def inverseTransform(self, num_samples=5000):
        samples = []
        for _ in range(num_samples):
            u = np.random.uniform(0, 1)  
            left = self.mu
            right = 10
              
            while right - left > 1e-6:  
                mid = (left + right) / 2
                if self.cdf(mid) < u:
                    left = mid
                else:
                    right = mid
            samples.append((left + right) / 2)
        return np.array(samples)

    def plot(self):
        x_values = np.arange(self.mu + 0.1,10,0.03) 
        pdf_values = [self.pdf(x) for x in x_values]
        cdf_values = [self.cdf(x) for x in x_values]

        plt.plot(x_values, pdf_values, label=f'PDF (λ={self.lmbda})', color='green')
        plt.plot(x_values, cdf_values, label=f'CDF (λ={self.lmbda})', color='black', linestyle='dashed')
        plt.legend()
        plt.title('PDF and CDF')
        plt.xlabel('x')
        plt.ylabel('Probability')
        plt.show()

lmbda = 0.25
mu = 1.5
deer = Santa(lmbda, mu)

deer.plot()
samples = deer.inverseTransform()
sample_mean = np.mean(samples)
population_mean, _ = quad(deer.integrand, mu, 10)

print(sample_mean)
print(population_mean)


