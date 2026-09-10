# Seminário: Álgebra Linear da Transformada Rápida de Fourier (FFT) e Aplicações

**Disciplina:** Álgebra Linear  
**Integrantes:** Estevão, Francisco e Jasmine  
**Data:** 01/12/2026  

---

## 1. Introdução e Motivação

O processamento digital de sinais baseia-se na capacidade de representar dados discretos sob diferentes perspectivas. No domínio temporal ou espacial, um sinal é expresso como amplitudes em instantes específicos. No entanto, muitas propriedades fundamentais tornam-se evidentes apenas quando o sinal é decomposto em suas frequências constitutivas.

A Transformada Discreta de Fourier (DFT) realiza essa transição entre domínios. Contudo, sua computação matricial ingênua exige complexidade de tempo O(N²). Para sinais longos de áudio (44.100 amostras/segundo) ou matrizes de imagem de alta resolução, o custo inviabiliza o processamento em tempo real. A Transformada Rápida de Fourier (FFT), introduzida por Cooley e Tukey em 1965, reduz esse custo para O(N log₂ N) por meio de uma fatoração em blocos esparsos da matriz de Fourier.

---

## 2. Fundamentação Matemática: A DFT como Mudança de Base

Considere um sinal discreto como um vetor coluna x em C^N:

x = [x₀, x₁, x₂, ..., x_{N-1}]ᵀ

A DFT mapeia x em um vetor de frequências X em C^N. Definindo a raiz N-ésima primitiva da unidade por:

ω_N = e^(-i * 2π / N) = cos(2π/N) - i * sin(2π/N)

A transformação é descrita pelo produto matriz-vetor:

X = F_N * x

Onde a matriz de Fourier F_N é uma matriz simétrica de Vandermonde constituída pelas potências da raiz da unidade.

### Ortogonalidade e Unitariedade
As colunas de F_N formam uma base ortogonal do espaço C^N. O produto hermitiano satisfaz:

F_N* * F_N = N * I_N

Portanto, a matriz normalizada (1/√N) * F_N é unitária. A transformação inversa (IDFT) é imediata e computacionalmente equivalente:

x = F_N⁻¹ * X = (1/N) * F_N* * X

---

## 3. O Algoritmo de Cooley-Tukey e Fatoração Matricial

Para N par (N = 2M), o algoritmo particiona o vetor x em suas componentes de índices pares e ímpares. Matematicamente, essa reorganização corresponde à aplicação de uma matriz de permutação P_N.

A matriz F_N fatora-se exatamente em matrizes em blocos esparsos:

F_N = [I_{N/2} ,  Ω_{N/2} ; I_{N/2} , -Ω_{N/2}] * [F_{N/2} , 0 ; 0 , F_{N/2}] * P_N

Onde:
* I_{N/2} é a matriz identidade de dimensão N/2.
* Ω_{N/2} contém os fatores de rotação (twiddle factors) em uma matriz diagonal.
* O bloco central aplica recursivamente duas transformadas de metade do tamanho.

Essa decomposição reduz o número de operações de N² para (N/2) * log₂ N.

---

## 4. Aplicações Práticas Desenvolvidas

### 4.1 Processamento e Filtragem de Áudio (1D)
Um sinal temporal acústico composto por harmônicos e ruído aditivo de alta frequência é transformado ao domínio espectral via FFT. Cria-se uma matriz diagonal de filtragem H, onde frequências acima do limiar são zeradas. O sinal limpo é obtido por IFFT.

### 4.2 Processamento e Compressão de Imagens (2D-FFT)
Uma imagem digital é tratada como uma matriz A. A transformada bidimensional aplica a DFT nas linhas e nas colunas consecutivamente: Â = F_M * A * F_Nᵀ. A compressão e atenuação de ruído são obtidas mantendo-se apenas o raio central de baixas frequências.

### 4.3 Compressão de Vídeo
Fluxos de vídeo exploram a redundância espacial interquadros por meio da Transformada Discreta de Cosseno (DCT) combinada com vetores de movimento calculados via correlação cruzada acelerada no domínio da frequência.

---

## 5. Estrutura dos Módulos Práticos

1. `01_dft_vs_fft.py`: Construção da matriz F_N, implementação Cooley-Tukey e medição de tempo comparando O(N²) contra O(N log N).
2. `02_audio_filtering.py`: Geração de sinal senoidal com ruído em 4 kHz, identificação espectral e atenuação por máscara passa-baixa.
3. `03_image_2dfft.py`: Decomposição espectral bidimensional, mascaramento radial e reconstrução inversa de imagem.
