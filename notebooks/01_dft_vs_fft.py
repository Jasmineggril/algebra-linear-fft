import numpy as np
import time
import matplotlib.pyplot as plt
from pathlib import Path

RESULTADOS = Path(__file__).resolve().parent.parent / 'resultados'
RESULTADOS.mkdir(exist_ok=True)

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
    x = np.asarray(x, dtype=complex)
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

# 3. Validação numérica contra a implementação do NumPy
rng = np.random.default_rng(42)
teste = rng.normal(size=32) + 1j * rng.normal(size=32)
resultado_cooley_tukey = fft_cooley_tukey(teste)
resultado_numpy = np.fft.fft(teste)
if not np.allclose(resultado_cooley_tukey, resultado_numpy):
    raise AssertionError('A implementação Cooley-Tukey diverge de numpy.fft.fft')
print('Validação Cooley-Tukey vs numpy.fft.fft: np.allclose=True')

# 4. Benchmark de Desempenho
tamanhos = [2**k for k in range(4, 12)] # de 16 a 2048 elementos
tempos_dft = []
tempos_fft = []

for N in tamanhos:
    x = rng.random(N)
    
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
plt.savefig(RESULTADOS / 'benchmark_dft_vs_fft.png', dpi=150)
plt.close()
