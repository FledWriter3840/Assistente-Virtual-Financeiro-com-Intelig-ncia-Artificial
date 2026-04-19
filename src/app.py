import json
import pandas as pd
import requests
import streamlit as st

# =========== CONFIGURAÇÃO =============

OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'gpt-oss' 

# =========== CARREGAR DADOS =============

perfil = json.load(open('data/perfil_do_usuario.json'))
regras_financeiras = json.load(open('data/regras_financeiras.json'))
interacoes = json.load(open('data/interações.json'))
dados_derivados = json.load(open('data/dados_derivados.json'))
metas = json.load(open('data/Metas.json'))
transacoes = pd.read_csv('data/transacoes.csv')
receitas = pd.read_csv('data/receitas.csv')

# ============= MONTAR CONTEXTO =============

contexto = f"""
CLIENTE: {perfil['nome']}
IDADE: {perfil['idade']}
PERFIL: {perfil['perfil']}
RENDA MENSAL: {perfil['renda_mensal']}
OBJETIVO: {perfil['objetivo']}
TOLERANCIA RISCO: {perfil['tolerancia_risco']}
REGRAS FINANCEIRAS: {regras_financeiras}
INTERACOES: {interacoes}
DADOS DERIVADOS: {dados_derivados}
METAS: {metas}
TRANSACOES: {transacoes}
RECEITAS: {receitas}
"""

# ============= SYSTEM PROMPT =============

system_prompt = f"""
Você é Avici, um agente financeiro inteligente especializado em controle financeiro pessoal, análise de gastos e orientação consultiva.

OBJETIVO:
Seu objetivo é ajudar o usuário a entender sua situação financeira, tomar decisões mais conscientes e alcançar suas metas, utilizando os dados fornecidos no contexto.

Você deve se comportar como um parceiro financeiro, com comunicação informal, acessível e levemente descontraída, mas mantendo seriedade em situações críticas.

REGRAS:

1. Baseie todas as respostas apenas nos dados fornecidos no contexto
2. Nunca invente informações financeiras ou valores
3. Se não houver dados suficientes, informe claramente a limitação
4. Não faça suposições fora do contexto
5. Não substitua um especialista financeiro profissional
6. Não tome decisões pelo usuário, apenas sugira
7. Não recomende investimentos de alto risco
8. Mantenha coerência com o perfil do usuário (ex: perfil moderado, conservador)
9. Priorize sempre as metas do usuário nas recomendações
10. Evite respostas genéricas — seja específico com base nos dados
11. Linguagem simples, como se fosse um amigo
12. Se a resposta for claramente uma regra, use-a

"""

# ============= CHAMAR OLLAMA =============

def perguntar (msg):
    prompt = f"""
    {system_prompt}
    
    CONTEXTO DO CLIENTE : {contexto}

    PERGUNTA: {msg}"""

    r = requests.post(OLLAMA_URL, json={'prompt': prompt, 'model': MODELO, "stream": False})
    return r.json()['response']

# ============= INTERFACE ================

st.title ('Avici, seu Assistente Financeiro Pessoal')

if pergunta := st.text_input ('Digite sua pergunta'):
    st.chat_message('user').write(pergunta)
    with st.spinner("Pensando..."):
        st.chat_message('assistant').write(perguntar(pergunta))
    


