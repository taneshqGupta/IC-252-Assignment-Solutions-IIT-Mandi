import numpy as np
import pandas as pd
import scipy.optimize as opt
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("dataset8.csv")
x = data.iloc[:, 0].dropna().values

# Define given CDFs and PDFs
def cdf1(x, alpha, lam):
    return (1 - np.exp(-lam * x)) ** alpha

def pdf1(x, alpha, lam):
    return alpha * lam * np.exp(-lam * x) * (1 - np.exp(-lam * x)) ** (alpha - 1)

def cdf2(x, alpha, lam):
    return 1 - (1 - np.exp(-lam / x)) ** alpha

def pdf2(x, alpha, lam):
    return alpha * lam * np.exp(-lam / x) / (x**2) * (1 - np.exp(-lam / x)) ** (alpha - 1)

# Negative log-likelihood
def nll1(params):
    alpha, lam = params
    if alpha <= 0 or lam <= 0:
        return np.inf
    return -np.sum(np.log(pdf1(x, alpha, lam) + 1e-10))

def nll2(params):
    alpha, lam = params
    if alpha <= 0 or lam <= 0:
        return np.inf
    return -np.sum(np.log(pdf2(x, alpha, lam) + 1e-10))

# Fit CDF1
res1 = opt.minimize(nll1, [1, 0.1], method='L-BFGS-B', bounds=[(1e-5, None), (1e-5, None)])
alpha1_hat, lambda1_hat = res1.x
print(f"CDF1 - alpha: {alpha1_hat:.4f}, lambda: {lambda1_hat:.4f}")

# Fit CDF2
res2 = opt.minimize(nll2, [1, 0.1], method='L-BFGS-B', bounds=[(1e-5, None), (1e-5, None)])
alpha2_hat, lambda2_hat = res2.x
print(f"CDF2 - alpha: {alpha2_hat:.4f}, lambda: {lambda2_hat:.4f}")

# Confidence Intervals (Symmetrical, 95%)
def calc_ci(result):
    hess_inv = result.hess_inv.todense()
    var = np.diag(hess_inv)
    se = np.sqrt(var)
    lower = result.x - 1.96 * se
    upper = result.x + 1.96 * se
    return lower, upper

# CI for CDF1
ci1_lower, ci1_upper = calc_ci(res1)
print("CDF1 95% symmetric CI (alpha):", f"{ci1_lower[0]:.4f} to {ci1_upper[0]:.4f}")
print("CDF1 95% symmetric CI (lambda):", f"{ci1_lower[1]:.4f} to {ci1_upper[1]:.4f}")

# CI for CDF2
ci2_lower, ci2_upper = calc_ci(res2)
print("CDF2 95% symmetric CI (alpha):", f"{ci2_lower[0]:.4f} to {ci2_upper[0]:.4f}")
print("CDF2 95% symmetric CI (lambda):", f"{ci2_lower[1]:.4f} to {ci2_upper[1]:.4f}")

# Plot the fit
sorted_x = np.sort(x)
x_vals = sorted_x
cdf1_vals = cdf1(x_vals, alpha1_hat, lambda1_hat)
cdf2_vals = cdf2(x_vals, alpha2_hat, lambda2_hat)

# Empirical CDF
empirical_cdf = np.arange(1, len(sorted_x)+1) / len(sorted_x)

plt.figure(figsize=(10,6))
plt.plot(sorted_x, empirical_cdf, 'k.', label='Empirical CDF (data)')
plt.plot(x_vals, cdf1_vals, 'r-', label='Fitted CDF1')
plt.plot(x_vals, cdf2_vals, 'b-', label='Fitted CDF2')
plt.xlabel('Failure Time')
plt.ylabel('Cumulative Probability')
plt.title('Fit Comparison (CDF)')
plt.legend()
plt.grid(True)
plt.show()
