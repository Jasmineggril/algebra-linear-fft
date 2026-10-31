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
3. Aplicações práticas em processamento de áudio e imagens, além da contextualização do uso de transformadas e correlação no processamento de vídeo.

O vídeo será abordado conceitualmente; este repositório não implementa um codec completo.

## 📂 Estrutura do Repositório
* `notebooks/01_dft_vs_fft.py`: Formulação matricial, implementação Cooley-Tukey e benchmark de complexidade.
* `notebooks/02_audio_filtering.py`: Filtragem espectral e remoção de ruídos em áudio.
* `notebooks/03_image_2dfft.py`: Filtragem e redução de coeficientes em imagens via FFT bidimensional.
* `notebooks/relatorio.md`: Relatório técnico com as deduções algébricas e fundamentação teórica.
* `resultados/`: Gráficos e arquivos WAV gerados pelos scripts.

## Requisitos

Python 3.9 ou superior e as dependências listadas em `requirements.txt`.

## Como Executar
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/jasmineggril/algebra-linear-fft.git
cd algebra-linear-fft
python -m pip install -r requirements.txt
```

Execute cada demonstração com Python 3:
```bash
python notebooks/01_dft_vs_fft.py
python notebooks/02_audio_filtering.py
python notebooks/03_image_2dfft.py
```

O primeiro script compara a DFT matricial e a FFT Cooley-Tukey, valida os resultados com `np.allclose` e grava `resultados/benchmark_dft_vs_fft.png`. O benchmark mede o ambiente local e usa uma semente fixa para gerar os mesmos dados a cada execução.

O segundo gera `resultados/audio_com_ruido.wav`, `resultados/audio_filtrado.wav` e `resultados/audio_filtering_demo.png`. O terceiro compara filtragem passa-baixa e uma demonstração de redução de coeficientes por limiar de magnitude; informa o percentual preservado e o erro relativo de reconstrução em `resultados/image_filtering_2dfft.png`.

## Resultados gerados

Os links abaixo apontam para os arquivos atualmente presentes em `resultados/`:

* [Benchmark DFT versus FFT](resultados/benchmark_dft_vs_fft.png)
* [Demonstração de filtragem de áudio](resultados/audio_filtering_demo.png)
* [Demonstração da FFT 2D em imagem](resultados/image_filtering_2dfft.png)
* [Áudio com ruído](resultados/audio_com_ruido.wav)
* [Áudio filtrado](resultados/audio_filtrado.wav)
