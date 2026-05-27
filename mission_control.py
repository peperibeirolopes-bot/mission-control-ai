# MISSION CONTROL AI

nome_missao = "Project SILENT SKY"
nome_equipe = "The Stellar Initiative"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [24, 95, 89, 96, 90],
    [25, 88, 74, 94, 85],
    [29, 65, 58, 91, 72],
    [31, 42, 38, 87, 56],
    [38, 28, 19, 78, 35],
    [29, 55, 34, 82, 50]
]

# FUNÇÕES DE ANÁLISE

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO"
    elif 18 <= valor <= 30:
        return "NORMAL"
    elif 31 <= valor <= 35:
        return "ATENÇÃO"
    else:
        return "CRÍTICO"

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO"
    elif valor < 60:
        return "ATENÇÃO"
    else:
        return "NORMAL"

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO"
    elif 20 <= valor <= 49:
        return "ATENÇÃO"
    else:
        return "NORMAL"

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO"
    elif 80 <= valor <= 89:
        return "ATENÇÃO"
    else:
        return "NORMAL"

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO"
    elif 40 <= valor <= 69:
        return "ATENÇÃO"
    else:
        return "NORMAL"

def calcular_pontuacao(classificacao):
    if classificacao == "NORMAL":
        return 0
    elif classificacao == "ATENÇÃO":
        return 1
    else:
        return 2

def classificar_ciclo(pontuacao):
    if 0 <= pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif 3 <= pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(pontuacao):
    if 0 <= pontuacao <= 2:
        return "Manter operação normal e continuar monitoramento."
    elif 3 <= pontuacao <= 5:
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

def analisar_tendencia(riscos):
    primeiro = riscos[0]
    ultimo = riscos[-1]
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável."

def identificar_area_mais_afetada(pontuacoes_por_area):
    indice = pontuacoes_por_area.index(max(pontuacoes_por_area))
    return indice

# LOOP PRINCIPAL

riscos = []
pontuacoes_por_area = [0, 0, 0, 0, 0]

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missão: {nome_missao}")
print(f"Equipe: {nome_equipe}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

for i, ciclo in enumerate(dados_missao):
    temperatura  = ciclo[0]
    comunicacao  = ciclo[1]
    bateria      = ciclo[2]
    oxigenio     = ciclo[3]
    estabilidade = ciclo[4]

    # Classificar cada sensor
    class_temp  = analisar_temperatura(temperatura)
    class_comu  = analisar_comunicacao(comunicacao)
    class_bat   = analisar_bateria(bateria)
    class_oxi   = analisar_oxigenio(oxigenio)
    class_estab = analisar_estabilidade(estabilidade)

    # Calcular pontuação dos sensores
    pont_temp  = calcular_pontuacao(class_temp)
    pont_comu  = calcular_pontuacao(class_comu)
    pont_bat   = calcular_pontuacao(class_bat)
    pont_oxi   = calcular_pontuacao(class_oxi)
    pont_estab = calcular_pontuacao(class_estab)

    # Pontuação total do ciclo
    total = pont_temp + pont_comu + pont_bat + pont_oxi + pont_estab

    # Guardar risco e acumular por área
    riscos.append(total)
    pontuacoes_por_area[0] += pont_temp
    pontuacoes_por_area[1] += pont_comu
    pontuacoes_por_area[2] += pont_bat
    pontuacoes_por_area[3] += pont_oxi
    pontuacoes_por_area[4] += pont_estab


    classificacao = classificar_ciclo(total)
    recomendacao  = gerar_recomendacao(total)

    # Exibir ciclo
    print(f"\nCICLO {i + 1}")
    print("-" * 60)
    print(f"Temperatura:  {temperatura}°C  | {class_temp}")
    print(f"Comunicação:  {comunicacao}%   | {class_comu}")
    print(f"Bateria:      {bateria}%       | {class_bat}")
    print(f"Oxigênio:     {oxigenio}%      | {class_oxi}")
    print(f"Estabilidade: {estabilidade}%  | {class_estab}")
    print(f"Pontuação de risco do ciclo: {total}")
    print(f"Classificação do ciclo: {classificacao}")
    print(f"Recomendação: {recomendacao}")

# RELATÓRIO

def gerar_relatorio_final():
    # Médias
    media_temp  = sum(ciclo[0] for ciclo in dados_missao) / len(dados_missao)
    media_comu  = sum(ciclo[1] for ciclo in dados_missao) / len(dados_missao)
    media_bat   = sum(ciclo[2] for ciclo in dados_missao) / len(dados_missao)
    media_oxi   = sum(ciclo[3] for ciclo in dados_missao) / len(dados_missao)
    media_estab = sum(ciclo[4] for ciclo in dados_missao) / len(dados_missao)

    # Estatísticas dos ciclos
    ciclo_critico   = riscos.index(max(riscos)) + 1
    maior_risco     = max(riscos)
    risco_medio     = sum(riscos) / len(riscos)
    ciclos_criticos = sum(1 for r in riscos if r >= 6)

    # Tendência e área mais afetada
    tendencia = analisar_tendencia(riscos)
    indice_area = identificar_area_mais_afetada(pontuacoes_por_area)
    area_afetada = areas_monitoradas[indice_area]

    # Classificação final baseada no risco médio
    classificacao_final = classificar_ciclo(round(risco_medio))

    print("\n" + "=" * 60)
    print("RELATÓRIO FINAL DA MISSÃO")
    print("=" * 60)
    print(f"Missão: {nome_missao}")
    print(f"Equipe: {nome_equipe}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print(f"\nMédia de temperatura:   {media_temp:.2f}°C")
    print(f"Média de comunicação:   {media_comu:.2f}%")
    print(f"Média de bateria:       {media_bat:.2f}%")
    print(f"Média de oxigênio:      {media_oxi:.2f}%")
    print(f"Média de estabilidade:  {media_estab:.2f}%")
    print(f"\nCiclo mais crítico:     Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão:  {risco_medio:.2f}")
    print(f"Ciclos críticos:        {ciclos_criticos}")
    print(f"\nTendência da missão:")
    print(f"{tendencia}")
    print(f"\nPontuação acumulada por área:")
    for i, area in enumerate(areas_monitoradas):
        print(f"  {area}: {pontuacoes_por_area[i]} pontos")
    print(f"\nÁrea mais afetada:")
    print(f"  {area_afetada}")
    print(f"\nClassificação final da missão:")
    print(f"  {classificacao_final}")
    print("=" * 60)

gerar_relatorio_final()
