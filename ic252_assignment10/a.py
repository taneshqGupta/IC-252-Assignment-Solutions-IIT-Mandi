import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import quad

class PDFAnalyzer:
    def __init__(self, data_file, lam, k):
        self.data = pd.read_csv(data_file, skiprows=1, header=None).values.flatten().astype(float)
        self.lam = lam
        self.k = k

    def pdf1(self, x):
        return (self.k / self.lam) * (x / self.lam)**(self.k - 1) * np.exp(-(x / self.lam)**self.k)

    def pdf2(self, x):
        return (self.lam * self.k * x**(self.k - 1)) / (1 + x**self.k)**(self.lam + 1)

    def plot_data_with_pdfs(self):
        x_vals = np.sort(self.data)

        plt.hist(self.data, bins=30, density=True, alpha=0.5)
        plt.plot(x_vals, self.pdf1(x_vals), 'r-', label='PDF-1')
        plt.plot(x_vals, self.pdf2(x_vals), 'g-', label='PDF-2')
        plt.xlabel('x')
        plt.ylabel('Density')
        plt.title('Sample Histogram with PDF Overlays')
        plt.legend()
        plt.grid(True)
        plt.show()

    def stat(self):
        self.sample_mean = np.mean(self.data)
        self.sample_var = np.var(self.data, ddof=1)

        self.pop_mean1, _ = quad(lambda x: x * self.pdf1(x), 0, np.inf)
        self.pop_var1, _ = quad(lambda x: (x - self.pop_mean1)**2 * self.pdf1(x), 0, np.inf)

        self.pop_mean2, _ = quad(lambda x: x * self.pdf2(x), 0, np.inf)
        self.pop_var2, _ = quad(lambda x: (x - self.pop_mean2)**2 * self.pdf2(x), 0, np.inf)

        print(f"Sample Mean: {self.sample_mean:.4f}")
        print(f"Sample Variance: {self.sample_var:.4f}")
        print(f"Population Mean (PDF-1): {self.pop_mean1:.4f}")
        print(f"Population Variance (PDF-1): {self.pop_var1:.4f}")
        print(f"Population Mean (PDF-2): {self.pop_mean2:.4f}")
        print(f"Population Variance (PDF-2): {self.pop_var2:.4f}")



analyzer = PDFAnalyzer('simulated_data.csv', lam=1.5, k=2)
analyzer.stat()
analyzer.plot_data_with_pdfs()