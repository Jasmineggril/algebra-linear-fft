# Seminário: Álgebra Linear da FFT e Aplicações Práticas

Este repositório apresenta um seminário introdutório sobre a relação entre
Álgebra Linear e a Transformada Rápida de Fourier (FFT), com foco em aplicações
reais em processamento de áudio, imagem e vídeo.

## Objetivos

- Entender a FFT como fatoração eficiente da Transformada Discreta de Fourier (DFT).
- Conectar conceitos de Álgebra Linear (bases, matrizes e mudança de base) ao domínio da frequência.
- Demonstrar aplicações práticas com interpretação técnica e intuitiva.

## Conteúdo do Seminário

1. **Fundamentos Matemáticos**
   - Números complexos e raízes da unidade
   - DFT em forma matricial
   - Interpretação geométrica como mudança de base

2. **Da DFT à FFT**
   - Custo computacional: de \(O(n^2)\) para \(O(n \log n)\)
   - Estratégia de divisão e conquista (Cooley-Tukey)
   - Estrutura em borboleta (butterfly)

3. **Aplicações em Áudio**
   - Análise espectral de sinais sonoros
   - Filtragem de ruído em frequência
   - Extração de características (pitch e timbre)

4. **Aplicações em Imagem**
   - Filtragem passa-baixa e passa-alta no domínio da frequência
   - Compressão baseada em componentes frequenciais
   - Remoção de padrões periódicos e ruídos estruturados

5. **Aplicações em Vídeo**
   - Análise temporal de quadros
   - Compressão com representação frequencial
   - Redução de ruído e melhoria de qualidade visual

## Público-Alvo

Estudantes e profissionais de Computação, Engenharia e áreas afins com noções
básicas de Álgebra Linear, sinais e programação.