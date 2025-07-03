import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

week = int(input("enter week of case_study ::>> "))

class week1:

    def __init__(self, filename):

        self.df = pd.read_csv(filename)
        self.data = self.df['failure_times']
        self.length_of_dataset = len(self.data)
        self.mean = None
        self.median = None
        self.mode = None
        self.min_val = None
        self.max_val = None
        self.skewness = None
        self.kurtosis = None
        self.stderr = None
        self.n = None
        self.linear_freq_table = None
        self.log_freq_table = None
        self.linear_bins = None
        self.log_bins = None

    def descriptive_stats(self):

        self.mean = self.data.mean()
        self.median = self.data.median()
        self.mode = self.data.mode()[0]
        self.min_val = self.data.min()
        self.max_val = self.data.max()
        print("Mean:", self.mean)
        print("Median:", self.median)
        print("Mode:", self.mode)
        print("Min:", self.min_val)
        print("Max:", self.max_val)

    def get_frequency(self):

        sd = np.sqrt(np.mean((self.data - self.mean) ** 2))
        u3 = np.mean((self.data - self.mean) ** 3) # third_central_moment
        u4 = np.mean((self.data - self.mean) ** 4) # fourth_central_moment
        self.skewness = u3 / (sd ** 3)
        self.kurtosis = u4 / (sd ** 4) - 3
        self.stderr = np.sqrt((6 * self.length_of_dataset * (self.length_of_dataset - 1)) / ((self.length_of_dataset - 2) * (self.length_of_dataset + 1) * (self.length_of_dataset + 3)))
        print("Second Central Moment(Variance): ", sd**2)
        print("Third Central Moment: ", u3)
        print("Fourth Central Moment: ", u4)
        print("Skewness:", self.skewness)
        print("Kurtosis: ", self.kurtosis)
        print("Standard Error of Skewness:", self.stderr)
        self.n = int(round(1 + np.log2(self.length_of_dataset) + np.log2(1 + abs(self.skewness) / self.stderr)))
        print("Number of bins (Doane's formula):", self.n)

        linear_freq, self.linear_bins = np.histogram(self.data, bins=self.n)
        linear_bin_ranges = [f"{round(self.linear_bins[i], 4)} - {round(self.linear_bins[i+1], 4)}" for i in range(len(self.linear_bins)-1)]
        self.linear_freq_table = pd.DataFrame({'Bin Range': linear_bin_ranges, 'Frequency': linear_freq})
        print("\nLinear Frequency Table:\n")
        print(self.linear_freq_table)

        self.log_bins = np.logspace(np.log10(self.data.min()), np.log10(self.data.max()), self.n)
        log_freq, _ = np.histogram(self.data, bins=self.log_bins)
        log_bin_ranges = [f"{round(self.log_bins[i], 4)} - {round(self.log_bins[i+1], 4)}" for i in range(len(self.log_bins)-1)]
        self.log_freq_table = pd.DataFrame({'Bin Range': log_bin_ranges, 'Frequency': log_freq})
        print("\nLog Frequency Table:\n")
        print(self.log_freq_table)



    def plot_freq(self):

        plt.figure(figsize=(12, 6))

        # Plot linear histogram
        plt.subplot(1, 2, 1)
        plt.hist(self.data, bins=self.linear_bins, edgecolor='black')
        plt.title('Histogram (Linear Scale)')
        plt.xlabel('Failure Time')
        plt.ylabel('Frequency')
        plt.grid(True)

        # Plot log histogram
        plt.subplot(1, 2, 2)
        plt.hist(self.data, bins=self.log_bins, edgecolor='black')
        plt.xscale('log')  # Log scale on x-axis
        plt.title('Histogram (Log X-Scale)')
        plt.xlabel('Failure Time (log scale)')
        plt.ylabel('Frequency')
        plt.grid(True, which='both', linestyle='--', linewidth=0.5)

        plt.tight_layout()
        plt.show()

if(week == 1):
    # week1 impl --start
        analysis = week1("dataset8.csv")
        analysis.descriptive_stats()
        analysis.get_frequency()
        analysis.plot_freq()
    # week1 impl --end

    




