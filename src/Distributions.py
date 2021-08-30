import numpy as np

def stirling_gamma(n):
    return np.sqrt(2 * np.pi * n) * (n / np.exp(1)) ** n

def beta_integrand(t, a, b):
    return (t ** (a-1)) * (1-t) ** (b-1) 
    
def beta_function(a, b):
    Subinterval = (1 - 0.01) / 100
    term_a = (Subinterval / 2) * beta_integrand(0.01, a, b)
    term_b = Subinterval * sum(beta_integrand(0.01 + i * Subinterval, a, b) + (Subinterval / 2) * beta_integrand(1, a, b) for i in range(1, 100 - 1))
    return term_a + term_b

#The Students-t distribution, where v is the degrees of freedom
def students_t(t, v):
    return (1 / (np.sqrt(v) * beta_function(0.5, v / 2))) * ((1 + ((t ** 2) / v)) ** np.negative(((v + 1) / 2)))
    
#the Z or Standard Normal distribution
def standard_normal(x):
    return (1/(1 * np.sqrt(2 * np.pi)) * np.exp(-(1/2) * (((x - 0) / 1) ** 2)))

def chi_square(x, k):
    if x > 0:
        result = 5
    else:
        result = 0
        
    return result
        
