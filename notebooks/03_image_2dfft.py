import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

RESULTADOS = Path(__file__).resolve().parent.parent / 'resultados'
RESULTADOS.mkdir(exist_ok=True)

# 1. Gerar uma imagem sintética (padrão xadrez com círculos concêntricos)
tamanho = 256
x = np.linspace(-10, 10, tamanho)
y = np.linspace(-10, 10, tamanho)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

# Imagem base + ruído de alta frequência (ondulações rápidas)
imagem_original = np.sin(R)
ruido_alta_freq = 0.4 * np.sin(15 * X) * np.cos(15 * Y)
imagem_contaminada = imagem_original + ruido_alta_freq

# 2. Transformada de Fourier Bidimensional (2D-FFT)
# Matematicamente equivale a aplicar F_N nas linhas e F_M nas colunas: F_M * Imagem * F_N^T
espectro_2d = np.fft.fft2(imagem_contaminada)
espectro_centralizado = np.fft.fftshift(espectro_2d) # Move baixa frequência para o centro

# 3. Filtragem passa-baixa
centro_x, centro_y = tamanho // 2, tamanho // 2
raio_corte = 35 # Raio das frequências que serão mantidas

Y_idx, X_idx = np.ogrid[:tamanho, :tamanho]
dist_do_centro = np.sqrt((X_idx - centro_x)**2 + (Y_idx - centro_y)**2)
mascara_passa_baixa = dist_do_centro <= raio_corte

# Aplica máscara e inverte o shift
espectro_filtrado = espectro_centralizado * mascara_passa_baixa
espectro_filtrado_ishift = np.fft.ifftshift(espectro_filtrado)

# 4. Reconstrução da Imagem via 2D-IFFT
imagem_filtrada = np.fft.ifft2(espectro_filtrado_ishift).real

# 4. Compressão por limiar de magnitude, separada da filtragem radial.
percentual_mantido = 10
limiar = np.percentile(np.abs(espectro_2d), 100 - percentual_mantido)
mascara_compressao = np.abs(espectro_2d) >= limiar
espectro_comprimido = espectro_2d * mascara_compressao
imagem_comprimida = np.fft.ifft2(espectro_comprimido).real
coeficientes_mantidos = 100 * np.count_nonzero(mascara_compressao) / mascara_compressao.size
erro_reconstrucao = np.linalg.norm(imagem_contaminada - imagem_comprimida) / np.linalg.norm(imagem_contaminada)
print(f'Filtragem radial: {100 * np.count_nonzero(mascara_passa_baixa) / mascara_passa_baixa.size:.2f}% dos coeficientes mantidos')
print(f'Compressão por magnitude: {coeficientes_mantidos:.2f}% dos coeficientes mantidos; erro relativo de reconstrução: {erro_reconstrucao:.6f}')

# 5. Visualização separada de espectro, filtragem e compressão.
fig, axs = plt.subplots(2, 3, figsize=(15, 9))

axs[0, 0].imshow(imagem_contaminada, cmap='gray')
axs[0, 0].set_title('Imagem de entrada')
axs[0, 0].axis('off')

# Magnitude logarítmica para visualização do espectro
magnitude_spectrum = np.log(np.abs(espectro_centralizado) + 1)
axs[0, 1].imshow(magnitude_spectrum, cmap='magma')
axs[0, 1].set_title('Espectro 2D centralizado')
axs[0, 1].axis('off')

axs[0, 2].imshow(imagem_filtrada, cmap='gray')
axs[0, 2].set_title('Filtragem passa-baixa')
axs[0, 2].axis('off')
axs[1, 0].imshow(mascara_passa_baixa, cmap='gray')
axs[1, 0].set_title('Máscara de filtragem')
axs[1, 0].axis('off')
axs[1, 1].imshow(imagem_comprimida, cmap='gray')
axs[1, 1].set_title(f'Compressão: {coeficientes_mantidos:.2f}% mantidos')
axs[1, 1].axis('off')
axs[1, 2].imshow(mascara_compressao, cmap='gray')
axs[1, 2].set_title(f'Erro relativo: {erro_reconstrucao:.6f}')
axs[1, 2].axis('off')

plt.tight_layout()
plt.savefig(RESULTADOS / 'image_filtering_2dfft.png', dpi=150)
plt.close()
