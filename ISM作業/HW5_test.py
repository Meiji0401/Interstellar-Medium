import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import brentq
import scienceplots
plot.style.use(['science', 'no-latex'])

k_b = 1.380649e-16
m_h= 1.6726219e-24
n_h = 100.0
T = 30.0
Z_prime = 1.0
I_UV = 1.0
D_prime = Z_prime
x_C_total = 3.2e-4 * D_prime
H2_photodiss_0 = 5.68e-11
AV_NH_conversion = 1.87e21
b5_H2_shielding = 2.0
k0_CHx_formation = 5.0e-16
CO_photodiss_0 = 2.0e-10
k1_CO_formation = 5.0e-10
CHx_photodiss_0 = 5.0e-10

def H2_self_shielding(N_H2_column, b5):
    if N_H2_column < 0:
        return 1.0 
    x = N_H2_column / 5.0e14 # normalization
    f = 0.965/((1+x/b5)**2) + (0.035/np.sqrt(1+x)) * np.exp(-8.5e-4 * np.sqrt(1+x))
    return f

def H2_equilibrium(x_h2_frac, N_H_column, n_H, R_dust, gamma_H2_0, I_UV, D_p, AV_conv, b5):
    if x_h2_frac <=1e-15:
        return 2 * R_dust * n_H * (1.0/1e-15)
    if x_h2_frac >= 1 - 1e-15:
        x_h2_frac = 1 - 1e-15
    A_V = D_p * N_H_column / AV_conv
    f_H2
    