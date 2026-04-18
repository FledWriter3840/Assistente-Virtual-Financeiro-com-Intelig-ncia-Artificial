# Base de Conhecimento

## Dados Utilizados


| Arquivo | Formato | Utilidade |
|---------|---------|---------------------|
| `perfil_do_usuario.json` | JSON | Permitir personalizar decisões com base na realidade e características do usuário |
| `transacoes.csv` | CSV | Registrar entradas e saídas financeiras, permitindo análise completa do comportamento do usuário |
| `Metas.json` | JSON | Definir objetivos financeiros e orientar as recomendações do agente |
| `dados_derivados.json` | JSON | Gerar insights automáticos (médias, tendências e alertas) a partir dos dados brutos |
| `interações.json` | JSON | Registrar conversas para melhorar respostas e adaptar o comportamento da IA. |
| `receitas.csv` | CSV | Representar entradas de dinheiro que são base para cálculo de orçamento e saldo |
| `regras_financeiras.json` | JSON | Fornecer lógica e boas práticas para guiar as recomendações do agente |


## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os arquivos perfil_do_usuario.json, transacoes.csv, metas.json, dados_derivados.json, interacoes.json, receitas.csv e regras_financeiras.json foram adicionados à pasta data, pois os dados anteriormente presentes não eram relevantes para o funcionamento do agente financeiro.

O arquivo transacoes.csv foi modificado para melhorar a análise financeira, incluindo:

- Padronização das categorias
- Inclusão de novos campos (como subcategoria, recorrência e método de pagamento)
- Separação clara entre entradas e saídas
- Estrutura mais organizada para facilitar o processamento

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```python
Import pandas as pd

import json

CSVS

historico pd.read_csv('data/receitas.csv')

transacoes pd.read_csv('data/transacoes.csv')

#JS0Ns

with open('data/perfil_do_usuario.json', 'r', encoding-'utf-8') as f:
perfil = json.load(f)

with open('data/Metas.json', 'r', encoding-'utf-8') as f:
metas = json.load(f)

with open('data/dados_derivados.json', 'r', encoding-'utf-8') as f:
dados_derivados = json.load(f)

with open('data/interacoes.json', 'r', encoding-'utf-8') as f:
interações = json.load(f)

with open('data/regras_financeiras.json', 'r', encoding-'utf-8') as f:
regras_financeiras = json.load(f)

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```

Contexto do Agente

Dados do Cliente:

- Nome: João Silva
- Perfil: Moderado
- Renda mensal: R$ 5.000
- Saldo disponível: R$ 1.800
- Reserva de emergência: R$ 10.000
- Objetivo principal: Construir reserva de emergência

---

Resumo Financeiro:

- Gasto médio mensal: R$ 3.200
- Tendência de gastos: Aumento
- Categoria mais impactante: Alimentação

---

Metas:

Completar reserva de emergência (Meta: R$ 15.000 até 06/2026)

---

Últimas transações:

- 01/10: Supermercado - R$ 450
- 05/10: Netflix - R$ 55,90
- 10/10: Restaurante - R$ 120
- 12/10: Uber - R$ 45
- 25/10: Combustível - R$ 250

---

Regras Financeiras Aplicáveis:

- Priorizar a construção da reserva de emergência
- Evitar gastos acima de 30% da renda em alimentação

---

Interação do Usuário:

- Pergunta: “Posso sair esse fim de semana?”

```
