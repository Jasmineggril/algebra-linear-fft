import numpy as np
import matplotlib.pyplot as plt

# 1. Simulação de um sinal sonoro com ruído
taxa_amostragem = 44100  # 44.1 kHz (taxa padrão de áudio)
duracao = 0.5           # 0.5 segundos
t = np.linspace(0, duracao, int(taxa_amostragem * duracao), endpoint=False)

# Nota musical pura (Lá central = 440 Hz) + Ruído agudo (apito de 4000 Hz)
sinal_puro = np.sin(2 * np.pi * 440 * t)
ruido = 0.6 * np.sin(2 * np.pi * 4000 * t)
sinal_poluido = sinal_puro + ruido

# 2. Mudança de Base para o Domínio da Frequência via FFT
N = len(t)
espectro = np.fft.fft(sinal_poluido)
frequencias = np.fft.fftfreq(N, 1 / taxa_amostragem)

# 3. Filtragem Espectral (Filtro Passa-Baixa)
# Zeramos amplitudes associadas a frequências acima de 1000 Hz
espectro_filtrado = espectro.copy()
mascara_filtro = np.abs(frequencias) > 1000
espectro_filtrado[mascara_filtro] = 0

# 4. Reconstrução do sinal no tempo via IFFT (Transformada Inversa)
sinal_recuperado = np.fft.ifft(espectro_filtrado).real

# 5. Visualização dos resultados para a apresentação
fig, axs = plt.subplots(3, 1, figsize=(10, 8))

# Sinal no Tempo (Antes e Depois)
axs[0].plot(t[:500], sinal_poluido[:500], color='r', alpha=0.7, label='Sinal com Ruído')
axs[0].plot(t[:500], sinal_puro[:500], color='k', linestyle='--', label='Sinal Limpo Original')
axs[0].set_title('Domínio do Tempo: Sinal Original vs Contaminado')
axs[0].set_ylabel('Amplitude')
axs[0].legend()
axs[0].grid(True)

# Domínio da Frequência (Espectro)
frequencias_positivas = frequencias[:N // 2]
potencia = np.abs(espectro[:N // 2])
axs[1].plot(frequencias_positivas, potencia, color='purple')
axs[1].set_title('Domínio da Frequência (FFT): Picos em 440 Hz (sinal) e 4000 Hz (ruído)')
axs[1].set_xlim(0, 5000)
axs[1].set_ylabel('Magnitude')
axs[1].grid(True)

# Sinal Recuperado
axs[2].plot(t[:500], sinal_recuperado[:500], color='g', label='Sinal Reconstruído (Pós-IFFT)')
axs[2].plot(t[:500], sinal_puro[:500], color='k', linestyle='--', alpha=0.5, label='Original')
axs[2].set_title('Domínio do Tempo: Sinal Restaurado por Filtragem Espectral')
axs[2].set_xlabel('Tempo (s)')
axs[2].set_ylabel('Amplitude')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.savefig('audio_filtering_demo.png')
plt.show()
