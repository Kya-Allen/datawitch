import numpy as np
import Distributions as dist

stuff = [10, 20, 30]

def mean(data):
    return sum(data[i] for i in range(len(data))) / len(data)
    

def test(x):
    return 3.0 * x**2 + 1
       
def trapezoidial_quadrature(a, b, n):
    Subinterval = (b - a) / n
    term_a = (Subinterval / 2) * test(a)
    term_b = Subinterval * sum(test(a + i * Subinterval) + (Subinterval / 2) * test(b) for i in range(1, n - 1))
    return term_a + term_b

def z_probability(a, b, n):
    Subinterval = (b - a) / n
    term_a = (Subinterval / 2) * dist.standard_normal(a)
    term_b = Subinterval * sum(dist.standard_normal(a + i * Subinterval) + (Subinterval / 2) * dist.standard_normal(b) for i in range(1, n - 1))
    return term_a + term_b

def t_probability(a, b, n, df):
    Subinterval = (b - a) / n
    term_a = (Subinterval / 2) * dist.students_t(a, df)
    term_b = Subinterval * sum(dist.students_t(a + i * Subinterval, df) + (Subinterval / 2) * dist.students_t(b, df) for i in range(1, n - 1))
    return term_a + term_b

print(trapezoidial_quadrature(0, 2, 10000))
print(z_probability(1.96, 50, 10000))
print(t_probability(1.96, 50, 10000, 500))