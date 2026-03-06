# 🔬 QWAN Ultra-Deep Health Complexity
### Sistema Termodinâmico de Alerta Precoce para Instabilidade em Sistemas de Saúde

**Autor:** Lucas Amaral Dourado  
**Licença:** MIT  

---

# Visão Geral

**QWAN Ultra-Deep Health Complexity** é uma plataforma científica experimental que aplica **física estatística, dinâmica não-linear, teoria da informação e ciência de sistemas complexos** à **vigilância em saúde pública**.

O sistema consome dados de internações hospitalares do **SIH/SUS** e executa **diagnósticos multicamadas de complexidade**, capazes de identificar **sinais precoces de instabilidade sistêmica**, incluindo:

- Lentidão crítica (critical slowing down)
- Perda de resiliência
- Persistência fractal
- Transições entrópicas
- Deformação da paisagem de potencial

O projeto integra:

- **Dashboards interativos em Streamlit**
- **Métricas de teoria da complexidade**
- **Reconstrução de potenciais termodinâmicos**
- **Processamento de sinais**
- **Detecção de regimes com aprendizado de máquina**

O resultado é um **sistema de diagnóstico estrutural em 16 pontos** projetado para monitorar **metastabilidade em sistemas de saúde**.

---

# Motivação Científica

Sistemas complexos próximos de **transições críticas** frequentemente exibem **assinaturas estatísticas universais** antes de colapsos.

Se representarmos o estado do sistema por uma série temporal:

$$
x_t
$$

À medida que o sistema se aproxima de uma transição crítica, vários indicadores mudam sistematicamente.

---

### Lentidão Crítica

A autocorrelação cresce:

$$
AC(1) \rightarrow 1
$$

porque o sistema demora mais para retornar ao equilíbrio após perturbações.

---

### Aumento da Variância

A variância aumenta porque o sistema passa a explorar uma região maior do espaço de estados:

$$
\sigma^2 = Var(x_t)
$$

---

### Memória Fractal

Correlação de longo alcance emerge:

$$
F(s) \sim s^\alpha
$$

onde:

- \( \alpha > 0.5 \) indica persistência
- \( \alpha < 0.5 \) indica antipersistência

---

### Colapso Entrópico

Métricas de complexidade como entropia podem diminuir à medida que o sistema se aproxima de estados altamente estruturados ou colapsos organizacionais.

---

O projeto operacionaliza esses princípios em um **motor de sensores de complexidade**.

---

# Arquitetura

```
project/
│
├── app.py
│
├── metastablex/
│   ├── core/
│   │   ├── signals.py
│   │   ├── potential.py
│   │   └── instability.py
│   │
│   ├── regimes/
│   │   ├── hmm.py
│   │   └── bayesian.py
│   │
│   ├── dynamics/
│   │   └── neural_ode.py
│   │
│   ├── control/
│   │   └── rl.py
│   │
│   └── utils/
│       └── preprocessing.py
```

O sistema é estruturado em camadas científicas modulares:

| Camada | Função |
|------|------|
| Camada de Dados | Ingestão de dados do SIH/SUS |
| Camada de Sinais | Métricas estatísticas |
| Camada de Complexidade | Entropia e análise fractal |
| Camada Dinâmica | Reconstrução de potenciais |
| Camada de Regimes | Detecção de estados com Bayesian/HMM |
| Camada de Controle | Políticas com reinforcement learning |
| Camada de Visualização | Dashboard Streamlit |

---

# Estrutura Matemática

## Retornos Logarítmicos

A principal transformação utilizada é o **retorno logarítmico**:

$$
r_t = \log(x_t + \epsilon) - \log(x_{t-1} + \epsilon)
$$

onde \( \epsilon \) evita singularidades numéricas.

---

# Métricas de Complexidade

## 1. Detrended Fluctuation Analysis (DFA)

Utilizada para estimar persistência fractal.

Passos:

1. Integração do sinal

$$
Y(k) = \sum_{i=1}^{k} (x_i - \bar{x})
$$

2. Divisão em janelas de tamanho \( n \)

3. Cálculo da flutuação RMS

$$
F(n) = \sqrt{\frac{1}{N}\sum (Y - Y_{trend})^2}
$$

Lei de escala:

$$
F(n) \sim n^\alpha
$$

Interpretação:

| Alpha | Interpretação |
|------|------|
| 0.5 | Aleatório |
| >0.5 | Persistente |
| <0.5 | Antipersistente |

---

## 2. Complexidade de Lempel-Ziv

Mede complexidade algorítmica.

Para uma sequência binária \( S \):

$$
C_{LZ} = \frac{c(n)\log_2 n}{n}
$$

onde:

- \( c(n) \) = número de subsequências únicas.

Valores altos indicam **maior novidade estrutural**.

---

## 3. Informação de Fisher

Mede **ordem versus desordem** no sistema.

Aproximação discreta:

$$
I = 4 \sum (\sqrt{p_{i+1}} - \sqrt{p_i})^2
$$

Interpretação:

| Fisher | Significado |
|------|------|
| Alto | Sistema ordenado |
| Baixo | Sistema desordenado |

---

## 4. Entropia de Permutação

Captura a estrutura temporal da série.

$$
H = - \sum p_i \log_2(p_i)
$$

Entropia normalizada:

$$
H_{norm} = \frac{H}{\log_2(d!)}
$$

onde:

- \( d \) é a dimensão de embedding.

---

## 5. Entropia Multiescala

A entropia é calculada em múltiplas escalas temporais:

$$
y_j^{(\tau)} = \frac{1}{\tau}\sum_{i=(j-1)\tau+1}^{j\tau} x_i
$$

Depois calcula-se a entropia de \( y^{(\tau)} \).

Isso revela **complexidade hierárquica**.

---

# Reconstrução da Paisagem de Potencial

Um dos diagnósticos mais importantes é a reconstrução do **potencial termodinâmico efetivo**.

Dada uma densidade de probabilidade \( p(x) \):

$$
U(x) = -\frac{\sigma^2}{2} \log p(x)
$$

Interpretação:

| Paisagem | Significado |
|------|------|
| Poço profundo | Sistema estável |
| Poço raso | Perda de resiliência |
| Bimodal | Transição de regime |

Isso corresponde ao sistema estocástico:

$$
\frac{dx}{dt} = -\nabla U(x) + \eta(t)
$$

onde \( \eta(t) \) representa ruído.

---

# Índice de Resiliência

Um índice composto de resiliência é definido como:

$$
R = 1 - \frac{AC_1 + \alpha + V}{3}
$$

onde:

- \( AC_1 \) = autocorrelação lag-1
- \( \alpha \) = expoente fractal
- \( V \) = transformação da volatilidade

Interpretação:

| Resiliência | Significado |
|------|------|
| >0.6 | Sistema estável |
| 0.45–0.6 | Atenção |
| <0.45 | Crítico |

---

# Reconstrução do Espaço de Fase

O sistema também visualiza **atratores de fase**.

Embedding:

$$
X_t = (x_t, x_{t+\tau})
$$

Isso revela estruturas dinâmicas ocultas.

---

# Análise Espectral

Usando o método de Welch:

$$
S(f) = \frac{1}{N}\left|\sum x_t e^{-i2\pi ft}\right|^2
$$

O espectro revela:

- periodicidades
- leis de escala
- mudanças de regime

---

# Controlador de Reinforcement Learning

O projeto inclui um controlador experimental baseado em **QLearning**.

Regra de atualização:

$$
Q(s,a) \leftarrow Q(s,a) + \alpha \left[r + \gamma \max Q(s',a') - Q(s,a)\right]
$$

Isso permite futuras pesquisas sobre **políticas adaptativas de intervenção**.

---

# Detecção Bayesiana de Regimes

Atualização de crença:

$$
P(s|D) = \frac{P(D|s)P(s)}{\sum P(D|s_i)P(s_i)}
$$

Usada para inferir **regimes ocultos do sistema**.

---

# Hidden Markov Models

Transições de regime:

$$
P(S_t | S_{t-1})
$$

com emissões gaussianas:

$$
x_t \sim N(\mu_s, \Sigma_s)
$$

---

# Dashboard Streamlit

A interface apresenta **16 painéis analíticos**:

| Painel | Métrica |
|-----|-----|
| 1 | Série temporal |
| 2 | Monitor de resiliência |
| 3 | Lentidão crítica |
| 4 | DFA |
| 5 | Informação de Fisher |
| 6 | Complexidade LZ |
| 7 | Poço de potencial |
| 8 | Atrator de fase |
| 9 | Espectro de potência |
| 10 | PDF |
| 11 | Assimetria |
| 12 | Curtose |
| 13 | Entropia multiescala |
| 14 | Volatilidade |
| 15 | Plano complexidade-ordem |
| 16 | Resumo técnico |

---

# Fonte de Dados

O sistema utiliza a biblioteca:

```
PySUS
```

para acessar dados do:

```
SIH/SUS
```

Parâmetros de consulta:

- UF
- Ano
- Mês
- Capítulo CID-10
- Agregação temporal

---

# Instalação

```
git clone https://github.com/your-repo/qwan-health-complexity
cd qwan-health-complexity
```

Instale as dependências:

```
pip install -r requirements.txt
```

Execute:

```
streamlit run app.py
```

---

# Saída do Sistema

O sistema gera um **mosaico diagnóstico** contendo:

- trajetórias de resiliência
- escalas de entropia
- diagnósticos espectrais
- paisagens de potencial
- atratores dinâmicos

Os gráficos são exportados automaticamente para:

```
/plots
```

Formatos:

- PNG
- PDF

---

# Direções Futuras de Pesquisa

Possíveis extensões incluem:

- Modelagem epidemiológica com Neural ODE
- Pipelines de vigilância em tempo real
- Políticas adaptativas com reinforcement learning
- Previsão de regimes com métodos bayesianos
- Integração com sistemas nacionais de monitoramento em saúde

---

# Licença

Licença MIT

```
Copyright (c) 2026 Lucas Amaral Dourado

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies.
```

---

# Autor

**Lucas Amaral Dourado**

Áreas de pesquisa:

- Sistemas Complexos
- Saúde Computacional
- Física Estatística
- Dinâmica de Sistemas de Saúde

---

# Citação

Caso utilize este projeto em pesquisa:

```
Dourado, Lucas Amaral.
QWAN Ultra-Deep Health Complexity:
Sinais Termodinâmicos de Alerta Precoce em Sistemas de Saúde.
2026.
```

---

# Observação Final

Sistemas de saúde são **sistemas adaptativos complexos**.

Compreendê-los exige ferramentas além da epidemiologia clássica.

Este projeto busca trazer **física estatística e ciência da complexidade** para o **monitoramento de sistemas de saúde**, abrindo caminho para **governança antecipatória baseada em dados**.

---
