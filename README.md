# 🚀 Mission Control AI — Project SILENT SKY

Sistema de monitoramento inteligente de missão espacial desenvolvido em Python.  
O sistema analisa ciclos de monitoramento, gera alertas automáticos e exibe um relatório final com a situação da operação.

---

## 👥 Equipe The Stellar Initiative

Pedro Ribeiro Lopes — RM: 570083

Lucas Furquim Lima — RM: 568690

Diogo Chiaradia Santos - RM: 570246

---

## 📋 Descrição

O **Mission Control AI** simula o acompanhamento de uma missão espacial experimental chamada **Project SILENT SKY**.  
A missão é dividida em 6 ciclos de monitoramento. Em cada ciclo, o sistema analisa 5 sensores, calcula o risco, classifica a situação e gera recomendações automáticas.  
Ao final, é exibido um relatório completo com tendência, área mais afetada e classificação geral da missão.

---

## ▶️ Como executar

1. Certifique-se de ter o Python 3 instalado
2. Clone ou baixe o repositório
3. Execute o arquivo principal:

```bash
python mission_control_ai.py
```

Não é necessário instalar nenhuma biblioteca externa.

---

## 🗂️ Estrutura do projeto

```
mission_control_ai.py   # Código principal
README.md               # Documentação do projeto
```

---

## ⚙️ Funções do sistema

| Função | Descrição |
|--------|-----------|
| `analisar_temperatura(valor)` | Classifica a temperatura do módulo |
| `analisar_comunicacao(valor)` | Classifica a qualidade do sinal |
| `analisar_bateria(valor)` | Classifica o nível de bateria |
| `analisar_oxigenio(valor)` | Classifica o nível de oxigênio |
| `analisar_estabilidade(valor)` | Classifica a estabilidade operacional |
| `calcular_pontuacao(classificacao)` | Converte classificação em pontos de risco |
| `classificar_ciclo(pontuacao)` | Classifica o ciclo com base na pontuação total |
| `gerar_recomendacao(pontuacao)` | Gera recomendação automática para o ciclo |
| `analisar_tendencia(riscos)` | Compara o primeiro e último ciclo para identificar tendência |
| `identificar_area_mais_afetada(pontuacoes_por_area)` | Identifica a área com maior risco acumulado |
| `gerar_relatorio_final()` | Exibe o relatório completo da missão |

---

## 🚨 Regras de alerta

### Temperatura (°C)
| Condição | Classificação |
|----------|---------------|
| Menor que 18°C | ATENÇÃO |
| De 18°C até 30°C | NORMAL |
| De 31°C até 35°C | ATENÇÃO |
| Maior que 35°C | CRÍTICO |

### Comunicação (%)
| Condição | Classificação |
|----------|---------------|
| Menor que 30% | CRÍTICO |
| De 30% até 59% | ATENÇÃO |
| 60% ou mais | NORMAL |

### Bateria (%)
| Condição | Classificação |
|----------|---------------|
| Menor que 20% | CRÍTICO |
| De 20% até 49% | ATENÇÃO |
| 50% ou mais | NORMAL |

### Oxigênio (%)
| Condição | Classificação |
|----------|---------------|
| Menor que 80% | CRÍTICO |
| De 80% até 89% | ATENÇÃO |
| 90% ou mais | NORMAL |

### Estabilidade (%)
| Condição | Classificação |
|----------|---------------|
| Menor que 40% | CRÍTICO |
| De 40% até 69% | ATENÇÃO |
| 70% ou mais | NORMAL |

---

## 📊 Pontuação de risco

| Classificação | Pontos |
|---------------|--------|
| NORMAL | 0 |
| ATENÇÃO | 1 |
| CRÍTICO | 2 |

### Classificação do ciclo
| Pontuação total | Classificação |
|-----------------|---------------|
| 0 a 2 pontos | MISSÃO ESTÁVEL |
| 3 a 5 pontos | MISSÃO EM ATENÇÃO |
| 6 a 10 pontos | MISSÃO CRÍTICA |

---

## 📡 Dados da missão simulada

```python
dados_missao = [
    [24, 95, 89, 96, 90],  # Ciclo 1 — Início estável
    [25, 88, 74, 94, 85],  # Ciclo 2 — Estabilização
    [29, 65, 58, 91, 72],  # Ciclo 3 — Leve queda
    [31, 42, 38, 87, 56],  # Ciclo 4 — Alerta geral
    [38, 28, 19, 78, 35],  # Ciclo 5 — Risco crítico
    [29, 55, 34, 82, 50]   # Ciclo 6 — Tentativa de recuperação
]
```

---

## 🛰️ Áreas monitoradas

- Temperatura interna
- Comunicação com a base
- Sistema de energia
- Suporte de oxigênio
- Estabilidade operacional
