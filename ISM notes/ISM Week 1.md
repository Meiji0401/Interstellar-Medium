x-ray: hot gas

radio: coldest gas clouds (SF)

75% H 24% He 1%Metal

dust abundance is limit by metallicity

## Statistical Mechanics
假設粒子 identical, distinguishable
### Ways of Combination
$$\begin{align}

W &=\frac{N!}{N_1!(N-N_1)!}\frac{(N-N_1)!}{N_2!(N_1-N_2)!}...\frac{N_k!}{N_k!0!}
\\
&=\frac{N !}{\prod^k_{i=1}N_i!}

\end{align}$$
### Entropy
$$\begin{align}
S&=\ln W = \ln N! - \sum^k_{i=1}\ln N_i!
\\
&\approx N\ln N - N -\sum^k_{i=1}\left(N_i\ln N_i-N_i\right)
\end{align}$$
> Using Sterling's approximation: 
> 	if $N$ is large, then 
> 	$$\ln N! \approx N\ln N- N$$

In L.T.D., $W$ is maximized. (if global T.D., everything is uniformed)
### Find maxima $W$
Under 2 conditions:
1. $N=\sum_i N_i$
2. $E=\sum_iN_iE_i$

Using Lagrangian multipliers = $\alpha,\ \beta$
$$\begin{align}
F(N_i) &= \ln W + \alpha (N\sum_iN)+\beta(E-\sum_iN_iE_i)
\\
&= N\ln N-N +\alpha N+\beta E-\sum^k_{i=1}\left[N_i(1-\alpha-\beta E_i)-N_i\ln N_i\right]
\end{align}$$
where $N\ln N-N + \alpha N + \beta E$ is constant and $\frac{\partial F(N_i)}{\partial N_i}=0$, then
$$1-\alpha -\beta E-\ln N_i-1=0$$
$$N_i=e^{-\alpha}e^{-\beta E_i}=e^{-\alpha}e^{-E_i/kT}$$
> by define 
> $\beta=\frac{1}{kT}$ using Maxwell Boltzmann distribution
> $\alpha \equiv \frac{\mu}{kT}$ where $\mu$ is the chemical potential

### Partition Function
Temperature of $\ce{He}$ for given energy
$$Z(T)=\sum_ie^{-\frac{E_i}{kT}}$$
$$E^{\alpha}=\frac{Z(T)}{N}$$
1. translation partition $\to$ motion
2. internal energy level

$$E_i=E_{i,tr}+E_{i,rot}+E_{i,vib}+E_{i,e}$$
$$\begin{align}
Z&=Z_{tr}+Z_{rot}+Z_{vib}+Z_{e}
\\
&=\left(\sum_ie^{-\frac{E_{i,tr}}{kT}}\right)\left(\sum_ie^{-\frac{E_{i,rot}}{k^T}} \right)
\end{align}$$
> $E_{i,rot}$: rotation, observed in lower radio
> $E_{i,vib}$: vibration, observed in near infrared, low energy
> $E_{i,e}$: electronic level, high energy

### Recall Particle in a box in Q.M.
