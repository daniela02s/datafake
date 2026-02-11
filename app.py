# %%
# Configuração do Ambiente e Importações

import pandas as pd
import streamlit as st
from faker import Faker
import random

# %%
# Inicializa o gerador de dados 

fake = Faker("pt_BR")

st.title("📊 Gerador de Dados Fakes")
st.write("Crie bases de dados personalizadas para testes e estudos de Ciência de Dados.")

# %%
# Barra lateral para configurações

st.sidebar.header("Configurações")
area = st.sidebar.selectbox("Escolha a área:", ['Vendas', 'Saúde', 'RH', 'Recuperação de Crédito'])
qtd = st.sidebar.slider("Quantas linhas deseja gerar?", min_value=10, max_value=1000, step=10)

# %%
# Lógica de Geração de Dados

def gerar_dados(area, qtd):
    dados = []
    if area == "Vendas":
        for _ in range(qtd):
            dados.append({
                "Data": fake.date_this_year(),
                "Cliente": fake.name(),
                "Produto": random.choice(["Camisa","Calça","Tênis","Boné"]),
                "Valor": round(random.uniform(50,500),2),
                "Pagamento": random.choice(["Cartão","Dinheiro","Pix"])
            })
    elif area == "Saúde":
        for _ in range(qtd):
            dados.append({
                "Data Consulta": fake.date_this_year(),
                "Paciente": fake.name(),
                "Especialidade": random.choice(["Clínico Geral", "Cardiologia", "Ortopedia"]),
                "Convênio": random.choice(["Particular", "Plano A", "Plano B","SUS"]),
                "Valor": round(random.uniform(100, 500), 2)
            })
    elif area == "RH":
        for _ in range(qtd):
            dados.append({
                "Funcionário": fake.name(),
                "Cargo": random.choice(["Analista", "Coordenador", "Gerente","Técnico"]),
                "Data Admissão": fake.date_between(start_date="-5y", end_date="today"),
                "Salário": round(random.uniform(2000, 10000), 2)
            })
    elif area == "Recuperação de Crédito":
        for _ in range(qtd):
            dados.append({
                "Cliente": fake.name(),
                "Valor em Aberto": round(random.uniform(500, 15000), 2),
                "Dias de Atraso": random.randint(1, 360),
                "Status": random.choice(["Pendente", "Negociado", "Ajuizado"]),
                "Último Contato": fake.date_this_year()
            })
    return pd.DataFrame(dados)

# %%
# Processamento e Exportação

df = gerar_dados(area,qtd)
st.dataframe(df)

def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")

csv = convert_df(df)

st.download_button(
    label="📥 Baixar CSV",
    data=csv,
    file_name=f'dados_{area.lower()}.csv',
    mime="text/csv"

)

# %%
