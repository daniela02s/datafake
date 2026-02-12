# %% 
# Configuração do Ambiente e Importações
import pandas as pd
import numpy as np
import streamlit as st
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializa o gerador de dados
# Garante a regionalização dos dados, permitindo análises geográficas realistas do mercado brasileiro
fake = Faker("pt_BR")

st.set_page_config(page_title="Gerador de Dados Fakes", layout="wide")
st.title("📊 Gerador de Dados Fakes")
st.write("Crie bases de dados personalizadas para testes e estudos de Ciência de Dados.")

# %% 
# Barra lateral para configurações
st.sidebar.header("Configurações")
area = st.sidebar.selectbox(
    "Escolha a área:", 
    ['Vendas', 'Saúde', 'RH', 'Recuperação de Crédito', 'Bancário (Crédito)']
)
qtd = st.sidebar.slider("Quantas linhas deseja gerar?", min_value=10, max_value=1000, step=10)

# %% 
# Funções de Geração de Dados
def gerar_dados_simples(area, qtd):
    """Gera datasets de tabela única para áreas genéricas"""
    dados = []
    for _ in range(qtd):
        if area == "Vendas":
            dados.append({
                "Data": fake.date_this_year(),
                "Cliente": fake.name(),
                "Produto": random.choice(["Camisa","Calça","Tênis","Boné"]),
                "Valor": round(random.uniform(50,500),2),
                "Pagamento": random.choice(["Cartão","Dinheiro","Pix"])
            })
        elif area == "Saúde":
            dados.append({
                "Data Consulta": fake.date_this_year(),
                "Paciente": fake.name(),
                "Especialidade": random.choice(["Clínico Geral", "Cardiologia", "Ortopedia"]),
                "Convênio": random.choice(["Particular", "Plano A", "Plano B","SUS"]),
                "Valor": round(random.uniform(100, 500), 2)
            })
        elif area == "RH":
            dados.append({
                "Funcionário": fake.name(),
                "Cargo": random.choice(["Analista", "Coordenador", "Gerente","Técnico"]),
                "Data Admissão": fake.date_between(start_date="-5y", end_date="today"),
                "Salário": round(random.uniform(2000, 10000), 2)
            })
        elif area == "Recuperação de Crédito":
            dados.append({
                "Cliente": fake.name(),
                "Valor em Aberto": round(random.uniform(500, 15000), 2),
                "Dias de Atraso": random.randint(1, 360),
                "Status": random.choice(["Pendente", "Negociado", "Ajuizado"]),
                "Último Contato": fake.date_this_year()
            })
    return pd.DataFrame(dados)

def generate_banking_data(n_clients):
    """Gera o ecossistema bancário com tabelas relacionadas"""
    # Tabela de Clientes
    clients = []
    for _ in range(n_clients):
        renda = round(random.uniform(2000, 25000), 2)
        # Lógica de negócio: Renda influencia o Score de crédito
        # Demonstra domínio de lógica de negócio ao criar correlação estatística entre renda e pontuação de crédito
        score_base = int((renda / 25000) * 400 + random.randint(300, 600))
        clients.append({
            # Utiliza identificadores únicos universais (UUID) para garantir a integridade referencial entre tabelas,
            # simulando um ambiente de produção real
            "id_cliente": fake.uuid4(),
            "nome": fake.name(),
            "idade": random.randint(18, 80),
            "renda_mensal": renda,
            "score_serasa_base": min(score_base, 1000),
            "data_adesao": fake.date_between(start_date='-5y', end_date='today'),
            "regiao_geografica": random.choice(['SP', 'RJ', 'MG', 'RS', 'BA', 'PR'])
        })
    df_clientes = pd.DataFrame(clients)

    # Tabela de Transações (Relacionada por id_cliente)
    transactions = []
    # Itera sobre o cadastro base para gerar um histórico transacional condicional,
    # simulando o comportamento real de clientes ao longo do tempo
    for _, row in df_clientes.iterrows():
        for _ in range(random.randint(5, 15)):
            transactions.append({
                "id_transacao": fake.uuid4(),
                "id_cliente": row['id_cliente'],
                "data_transacao": fake.date_time_between(start_date='-1y', end_date='now'),
                "valor": round(random.uniform(10, 5000), 2),
                "categoria": random.choice(['Saque', 'Cartão', 'PIX']),
                "tipo_dispositivo": random.choice(['Android', 'iOS', 'Web'])
            })
    df_transacoes = pd.DataFrame(transactions)

    # Tabela de Crédito (Status e Variável Alvo/Target)
    credit_status = []
    for _, row in df_clientes.iterrows():
        # Probabilidade de inadimplência baseada no score
        prob_default = 0.8 if row['score_serasa_base'] < 500 else 0.1
        target = 1 if random.random() < prob_default else 0
        divida_ativa = target == 1 or random.random() < 0.2
        
        credit_status.append({
            "id_cliente": row['id_cliente'],
            "tem_divida_ativa": divida_ativa,
            "dias_atraso": random.randint(1, 90) if divida_ativa else 0,
            "valor_devido": round(random.uniform(500, 10000), 2) if divida_ativa else 0.0,
            "target_inadimplente": target
        })
    df_credito = pd.DataFrame(credit_status)
    
    return df_clientes, df_transacoes, df_credito

# %% 
# Processamento e Interface

if area == "Bancário (Crédito)":
    st.subheader("🏦 Ecossistema Bancário Relacional")
    st.info("Este módulo gera dados integrados. O ID do cliente conecta as três tabelas.")
    
    # Geração dos dados
    df_c, df_t, df_s = generate_banking_data(qtd)
    
    # Organização em abas para melhor UX
    # Foca na experiência do usuário (UX) e na organização de dados complexos,
    # facilitando o consumo da informação por áreas não técnicas
    tab1, tab2, tab3 = st.tabs(["👥 Clientes", "💳 Transações", "⚠️ Status de Crédito"])
    
    # Aplica boas práticas de engenharia de dados ao garantir a codificação correta 
    # e a limpeza de índices desnecessários para exportação
    with tab1:
        st.dataframe(df_c, use_container_width=True)
        st.download_button("📥 Baixar Clientes (CSV)", df_c.to_csv(index=False).encode("utf-8"), "clientes.csv", "text/csv")
        
    with tab2:
        st.dataframe(df_t, use_container_width=True)
        st.download_button("📥 Baixar Transações (CSV)", df_t.to_csv(index=False).encode("utf-8"), "transacoes.csv", "text/csv")
        
    with tab3:
        st.dataframe(df_s, use_container_width=True)
        st.download_button("📥 Baixar Status Crédito (CSV)", df_s.to_csv(index=False).encode("utf-8"), "status_credito.csv", "text/csv")

else:
    # Geração simples para as outras áreas
    df = gerar_dados_simples(area, qtd)
    st.subheader(f"Dataset de {area}")
    st.dataframe(df, use_container_width=True)
    
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label=f"📥 Baixar CSV de {area}",
        data=csv,
        file_name=f'dados_{area.lower().replace(" ", "_")}.csv',
        mime="text/csv"
    )