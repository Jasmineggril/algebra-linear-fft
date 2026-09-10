import numpy as np
import matplotlib.pyplot as plt

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

# 3. Filtro Passa-Baixa (Compressão/Limpeza de Frequências Altas)
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

# 5. Visualização comparativa
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].imshow(imagem_contaminada, cmap='gray')
axs[0].set_title('Imagem Original + Ruído')
axs[0].axis('off')

# Magnitude logarítmica para visualização do espectro
magnitude_spectrum = np.log(np.abs(espectro_centralizado) + 1)
axs[1].imshow(magnitude_spectrum, cmap='magma')
axs[1].set_title('Espectro de Frequências (2D-FFT)')
axs[1].axis('off')

axs[2].imshow(imagem_filtrada, cmap='gray')
axs[2].set_title('Imagem Reconstruída (Filtro Passa-Baixa)')
axs[2].axis('off')

plt.tight_layout()
plt.savefig('image_filtering_2dfft.png')
plt.show()
