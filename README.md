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
3. Aplicações práticas em processamento de áudio e imagem (2D-FFT).

## 📂 Estrutura do Repositório
* `notebooks/01_dft_vs_fft.py`: Formulação matricial, implementação Cooley-Tukey e benchmark de complexidade.
* `notebooks/02_audio_filtering.py`: Filtragem espectral e remoção de ruídos em áudio.
* `notebooks/03_image_2dfft.py`: Filtros passa-alta/baixa e compressão de imagens via FFT bidimensional.
* `notebooks/relatorio.md`: Relatório técnico com as deduções algébricas e fundamentação teórica.
* `resultados/`: Gráficos e arquivos WAV gerados pelos scripts.

## Requisitos

Python 3.9 ou superior e as dependências listadas em `requirements.txt`.

## 🚀 Como Executar os Scripts
Clone o repositório e execute com Python 3:
```bash
git clone https://github.com/jasmineggril/algebra-linear-fft.git
cd algebra-linear-fft
python -m pip install -r requirements.txt
python notebooks/01_dft_vs_fft.py
python notebooks/02_audio_filtering.py
python notebooks/03_image_2dfft.py
```

Os três scripts imprimem as validações e métricas calculadas e salvam seus resultados em `resultados/`.

O primeiro script compara a implementação recursiva de Cooley-Tukey com `numpy.fft.fft` usando `np.allclose`. O segundo gera `audio_com_ruido.wav` e `audio_filtrado.wav`. O terceiro exibe separadamente a filtragem passa-baixa e a compressão por limiar de magnitude, informando os coeficientes mantidos e o erro relativo de reconstrução.
