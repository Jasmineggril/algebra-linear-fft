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

Essa decomposição reduz o custo assintótico de O(N²) para O(N log₂ N), pois cada nível realiza O(N) operações e existem log₂ N níveis.

## 4. Aplicações Práticas Desenvolvidas

### 4.1 Processamento e Filtragem de Áudio (1D)
O script gera uma senoide de 440 Hz e adiciona uma interferência tonal de 4.000 Hz. A DFT/FFT representa o sinal no domínio da frequência; uma máscara passa-baixa zera os bins acima de 1.000 Hz, e a transformada inversa reconstrói o sinal filtrado. Este exemplo sintético ilustra filtragem, não remoção universal de ruído.

### 4.2 Processamento de Imagens (2D)
Uma imagem digital em tons de cinza é uma matriz A. Sua DFT bidimensional pode ser expressa como F_M A F_Nᵀ, ou calculada aplicando transformadas unidimensionais às linhas e colunas. No script, uma máscara radial de baixas frequências realiza filtragem. Separadamente, um limiar de magnitude zera coeficientes e permite avaliar a proporção preservada e o erro relativo de reconstrução; isso ilustra esparsificação espectral, não um formato completo de arquivo comprimido.

### 4.3 Contextualização do Processamento de Vídeo
Vídeo pode ser entendido como uma sequência de quadros e, portanto, como um sinal com dimensões espaciais e temporais. DFT e DCT são transformações distintas: codecs de vídeo podem usar transformações baseadas em cossenos ou outras representações, junto a predição, quantização e codificação para representar os dados. A correlação cruzada entre quadros ou regiões pode ser calculada por convoluções no domínio da frequência e, com preenchimento adequado quando necessário, pode aproveitar a FFT para reduzir o custo em problemas de maior porte. Este repositório contextualiza essas ideias, mas não implementa um codec completo.

## 5. DFT, FFT e DCT
A DFT é a transformação linear que converte uma sequência finita em coeficientes complexos da base de Fourier. A FFT não é outra transformação: é uma família de algoritmos eficientes para calcular a mesma DFT, como a fatoração recursiva de Cooley-Tukey para tamanhos apropriados. Já a DCT (Transformada Discreta de Cosseno) usa uma base de cossenos e é uma transformação distinta; não é uma versão real da FFT. DCT e DFT podem ter algoritmos rápidos relacionados, mas não devem ser confundidas.

## 6. Estrutura dos Módulos Práticos
1. `01_dft_vs_fft.py`: DFT matricial, implementação recursiva de Cooley-Tukey, validação com `numpy.fft.fft` e benchmark local reproduzível.
2. `02_audio_filtering.py`: geração de sinal com interferência tonal, filtragem espectral e gravação dos WAVs de entrada e saída.
3. `03_image_2dfft.py`: DFT bidimensional, filtragem passa-baixa e demonstração separada de limiar por magnitude, com percentual preservado e erro de reconstrução.

## 7. Referências
- STRANG, Gilbert. *Introduction to Linear Algebra*. Seção 3.5.
- ANTON, Howard; RORRES, Chris. *Álgebra Linear com Aplicações*. Seção 6.6.
- COOLEY, J. W.; TUKEY, J. W. *An Algorithm for the Machine Calculation of Complex Fourier Series*, 1965.
