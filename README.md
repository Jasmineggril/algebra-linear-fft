# Álgebra Linear da Transformada Rápida de Fourier (FFT)

Seminário e repositório de implementações práticas para a disciplina de Álgebra Linear.

## 👥 Integrantes
* Jasmine
* Estevão
* Francisco

## 🎯 Objetivo
Apresentar os fundamentos de álgebra linear por trás da Transformada Discreta de Fourier (DFT) e da Transformada Rápida de Fourier (FFT), abordando:
1. Formulação matricial e bases ortogonais.
2. Fatoração de matrizes esparsas no algoritmo de Cooley-Tukey.
3. Aplicações práticas em processamento de áudio, imagem (2D-FFT) e vídeo.

## 📂 Estrutura do Repositório
* `notebooks/01_dft_vs_fft.py`: Formulação matricial, implementação Cooley-Tukey e benchmark de complexidade.
* `notebooks/02_audio_filtering.py`: Filtragem espectral e remoção de ruídos em áudio.
* `notebooks/03_image_2dfft.py`: Filtros passa-alta/baixa e compressão de imagens via FFT bidimensional.
* `relatorio.md`: Relatório técnico completo com as deduções algébricas e fundamentação teórica.

## 🚀 Como Executar os Scripts
Clone o repositório e execute com Python 3:
```bash
git clone [https://github.com/jasmineggril/algebra-linear-fft.git](https://github.com/jasmineggril/algebra-linear-fft.git)
cd algebra-linear-fft
pip install numpy matplotlib
python notebooks/01_dft_vs_fft.py
