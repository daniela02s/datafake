# Gerador de Dados Sintéticos (Data Fake Generator)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## Descrição do Projeto
Este projeto é uma aplicação web interativa desenvolvida com **Streamlit** que permite a geração de bases de dados personalizadas para testes e estudos de Ciência de Dados. A ferramenta foi projetada para apoiar desenvolvedores e analistas que precisam de massas de dados realistas (mas fictícias) para validar sistemas ou treinar modelos preditivos.

O diferencial deste gerador é a segmentação por áreas estratégicas, incluindo um módulo focado em **Recuperação de Crédito**, essencial para análises de inadimplência e comportamento financeiro.

## Funcionalidades
- **Segmentação por Áreas:** Vendas, Saúde, RH e Recuperação de Crédito.
- **Configuração Flexível:** Controle da quantidade de registros (10 a 1000) via slider.
- **Dados Localizados:** Geração de nomes e documentos (CPF) seguindo o padrão brasileiro (pt-BR) através da biblioteca **Faker**.
- **Exportação:** Download imediato da base gerada em formato `.csv`.
- **Visualização:** Prévia dinâmica dos dados diretamente na interface.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Interface Web:** Streamlit
- **Manipulação de Dados:** Pandas
- **Geração de Dados Sintéticos:** Faker
- **Gerenciamento de Dependências:** pip / requirements.txt

## Estrutura do Repositório
- `app.py`: Código principal da aplicação.
- `requirements.txt`: Lista de dependências para reprodução do ambiente.

