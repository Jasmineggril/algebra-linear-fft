import numpy as np
import time
import matplotlib.pyplot as plt

# 1. DFT puramente Matricial: X = F_N * x  (Complexidade O(N^2))
def dft_matrix(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    omega = np.exp(-2j * np.pi / N)
    F_N = omega ** (k * n)
    return F_N @ x

# 2. FFT de Cooley-Tukey Recursiva (Complexidade O(N log N))
# Decompõe a matriz em blocos par e ímpar via álgebra linear
def fft_cooley_tukey(x):
    N = len(x)
    if N <= 1:
        return x
    if N % 2 != 0:
        raise ValueError("O tamanho do vetor deve ser potência de 2")
        
    X_even = fft_cooley_tukey(x[::2])
    X_odd = fft_cooley_tukey(x[1::2])
    
    twiddle = np.exp(-2j * np.pi * np.arange(N // 2) / N)
    return np.concatenate([
        X_even + twiddle * X_odd,
        X_even - twiddle * X_odd
    ])

# 3. Benchmark de Desempenho
tamanhos = [2**k for k in range(4, 12)] # de 16 a 2048 elementos
tempos_dft = []
tempos_fft = []

for N in tamanhos:
    x = np.random.random(N)
    
    # Tempo DFT
    t0 = time.perf_counter()
    dft_matrix(x)
    tempos_dft.append(time.perf_counter() - t0)
    
    # Tempo FFT
    t0 = time.perf_counter()
    fft_cooley_tukey(x)
    tempos_fft.append(time.perf_counter() - t0)

# 4. Gerar o gráfico para os slides
plt.figure(figsize=(9, 5))
plt.plot(tamanhos, tempos_dft, 'o-', label='DFT Matricial $\\mathcal{O}(N^2)$')
plt.plot(tamanhos, tempos_fft, 's-', label='FFT Cooley-Tukey $\\mathcal{O}(N \\log N)$')
plt.xlabel('Tamanho do Sinal (N)')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Impacto da Fatoração Matricial: DFT vs FFT')
plt.grid(True)
plt.legend()
plt.savefig('benchmark_dft_vs_fft.png')
plt.show()
