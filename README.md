# 🚢 Titanic Survival Analysis: Machine Learning & Data Storytelling

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/pandas-Data_Analysis-yellow.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Machine_Learning-orange.svg)

## 📌 Visão Geral do Projeto
Este repositório contém uma análise aprofundada ponta-a-ponta e modelagem preditiva baseada nos dados do naufrágio do Titanic. O foco deste projeto é ir além da precisão do modelo, focando em **interpretabilidade, boas práticas de código (Python/Pandas)** e **storytelling de dados**.

## 🎯 Objetivos
- Realizar Análise Exploratória de Dados (EDA) para identificar correlações sociais e demográficas com as taxas de sobrevivência.
- Aplicar técnicas de Feature Engineering para criar variáveis explicativas mais ricas (ex: *Family Size*).
- Treinar e avaliar modelos de classificação, extraindo o grau de importância de cada variável na decisão final (Feature Importance).

## 🗂️ Estrutura do Repositório
* `data/raw/`: Contém o dataset original `titanic.csv`.
* `notebooks/`: Jupyter Notebook estruturado com a linha de raciocínio, códigos e conclusões.
* `src/`: Scripts Python contendo funções auxiliares para manter o Notebook limpo e focado em negócios.

## 🚀 Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/jlfcar2/titanic-survival-analysis.git](https://github.com/SEU_USUARIO/titanic-survival-analysis.git)
   ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute o Jupyter Notebook:
    ```bash
    jupyter notebook notebooks/01_eda_and_modeling_titanic.ipynb
    ```

🛠️ Tecnologias Utilizadas
- Manipulação de Dados: Pandas, NumPy
- Visualização: Matplotlib, Seaborn
- Machine Learning: Scikit-Learn
- Ambiente de Desenvolvimento: Jupyter Notebook

Desenvolvido por Jonatha Lima Fernandes - Conecte-se comigo no LinkedIn.