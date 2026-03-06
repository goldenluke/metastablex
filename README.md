# MetastableX  
### Ultra-Deep Health Complexity Monitoring

**MetastableX** é uma plataforma experimental de **vigilância epidemiológica baseada em física estatística**, teoria da informação e dinâmica não linear.  

O sistema utiliza dados reais do **SIH/SUS** e aplica métodos de **análise de criticidade**, **complexidade estrutural** e **dinâmica de regimes** para detectar **sinais precoces de instabilidade em sistemas de saúde**.

A plataforma integra:

- Física de sistemas complexos  
- Termodinâmica fora do equilíbrio  
- Teoria da informação  
- Dinâmica de séries temporais  
- Inferência de regimes  
- Controle adaptativo  

---

# Arquitetura do Projeto

```
.
├── app.py
│
├── metastablex
│   ├── core
│   │   ├── signals.py
│   │   ├── potential.py
│   │   └── instability.py
│   │
│   ├── regimes
│   │   ├── bayesian.py
│   │   └── hmm.py
│   │
│   ├── control
│   │   └── rl.py
│   │
│   ├── dynamics
│   │   └── neural_ode.py
│   │
│   └── utils
│       └── preprocessing.py
│
└── plots
```

---

# Conceito Fundamental

Sistemas complexos apresentam mudanças abruptas quando se aproximam de **transições críticas**.

Em sistemas dinâmicos estocásticos, a evolução pode ser descrita por:

$$
\frac{dx}{dt} =
- \nabla \Phi(x)
+
\eta(t)
$$

onde:

- $x$ representa o estado do sistema
- $\Phi(x)$ é um **potencial efetivo**
- $\eta(t)$ representa ruído estocástico

Essa formulação corresponde a uma **equação de Langevin**.

---

# Reconstrução de Potencial

A paisagem de energia é reconstruída a partir da distribuição empírica das variações da série temporal.

Se $p(x)$ é a densidade de probabilidade:

$$
U(x) =
- \frac{\sigma^2}{2} \ln p(x)
$$

onde:

- $U(x)$ é o **potencial estocástico**
- $\sigma^2$ é a variância do processo

Vales profundos indicam **estabilidade estrutural**, enquanto vales rasos indicam **metaestabilidade**.

---

# Sensores de Complexidade

O sistema calcula múltiplos indicadores derivados de física estatística e teoria da informação.

## Memória Fractal

A memória de longo alcance é estimada via **Detrended Fluctuation Analysis**:

$$
F(n) \sim n^{\alpha}
$$

onde:

- $\alpha < 0.5$ → antipersistência  
- $\alpha = 0.5$ → ruído branco  
- $\alpha > 0.5$ → persistência estrutural  

---

## Informação de Fisher

A informação estrutural é definida como:

$$
I =
4 \sum_i
\left(
\nabla \sqrt{p_i}
\right)^2
$$

Valores elevados indicam **ordem estrutural elevada**.

---

## Complexidade Lempel–Ziv

A complexidade algorítmica é estimada pela compressibilidade da série:

$$
C_{LZ} =
\frac{c(n)\log_2 n}{n}
$$

onde $c(n)$ representa o número de padrões distintos detectados.

---

## Entropia por Permutação

A entropia ordinal mede complexidade dinâmica:

$$
H =
-\sum p_i \log(p_i)
$$

normalizada por:

$$
H_{norm} =
\frac{H}{\log(d!)}
$$

---

# Detecção de Critical Slowing Down

Antes de colapsos sistêmicos, sistemas complexos exibem **lentidão crítica**.

Esse fenômeno é detectado via aumento da autocorrelação:

$$
AC_1 =
\text{corr}(x_t, x_{t-1})
$$

Quando:

$$
AC_1 \rightarrow 1
$$

o sistema aproxima-se de uma **bifurcação dinâmica**.

---

# Índice de Resiliência Sistêmica

A plataforma sintetiza múltiplos indicadores em um índice composto:

$$
R =
1 -
\frac{
AC_1 +
\alpha +
\log_{10}(\sigma^2)
}{3}
$$

onde:

- $AC_1$ → autocorrelação  
- $\alpha$ → memória fractal  
- $\sigma^2$ → volatilidade  

Valores baixos de $R$ indicam **perda de resiliência sistêmica**.

---

# Pipeline Analítico

```
Dados SIH/SUS
     │
     ▼
Série temporal de internações
     │
     ▼
Transformação log-retornos
     │
     ▼
Sensores de complexidade
     │
     ▼
Reconstrução de potencial
     │
     ▼
Detecção de regimes
     │
     ▼
Diagnóstico estrutural
```

---

# Diagnóstico de 16 Sensores

O dashboard produz um **mosaico analítico completo**:

1. Série temporal bruta  
2. Índice de resiliência  
3. Autocorrelação (critical slowing down)  
4. Memória fractal (DFA)  
5. Informação de Fisher  
6. Complexidade Lempel-Ziv  
7. Potencial estocástico  
8. Atrator de fase  
9. Espectro de potência  
10. Distribuição de retornos  
11. Assimetria  
12. Curtose  
13. Entropia multiescala  
14. Volatilidade  
15. Plano complexidade-ordem  
16. Diagnóstico sistêmico  

---

# Inferência de Regimes

A biblioteca inclui métodos para detecção de regimes dinâmicos.

### Hidden Markov Models

$$
P(S_t|X_t)
$$

onde $S_t$ representa estados latentes.

Implementação:

```
metastablex/regimes/hmm.py
```

---

### Filtro Bayesiano

A atualização da crença segue:

$$
P(S_t|X_t) =
\frac{
P(X_t|S_t) P(S_t)
}{
\sum_i P(X_t|S_i)P(S_i)
}
$$

Implementado em:

```
metastablex/regimes/bayesian.py
```

---

# Controle Adaptativo

O sistema inclui um controlador de **aprendizado por reforço**.

Função de atualização Q-Learning:

$$
Q(s,a)
\leftarrow
Q(s,a)
+
\alpha
\left[
r +
\gamma
\max_a Q(s',a)
-
Q(s,a)
\right]
$$

Implementado em:

```
metastablex/control/rl.py
```

---

# Interface Interativa

A aplicação é construída com **Streamlit**.

```
streamlit run app.py
```

A interface permite:

- seleção de estado (UF)
- filtragem por capítulo CID
- agregação temporal
- controle da janela de análise

---

# Fonte de Dados

Dados hospitalares são obtidos via:

```
PySUS
```

Fonte:

**SIH/SUS — Sistema de Informações Hospitalares**

---

# Instalação

```
pip install streamlit numpy pandas scipy matplotlib pysus hmmlearn
```

---

# Execução

```
streamlit run app.py
```

---

# Motivação Científica

A plataforma investiga a hipótese:

> Sistemas complexos de saúde apresentam sinais detectáveis de instabilidade antes de colapsos epidemiológicos.

Inspirada em:

- Critical Transitions in Nature and Society  
- Statistical Physics of Complex Systems  
- Early Warning Signals for Critical Transitions  

---

# Status do Projeto

```
Research Prototype
Active Development
Experimental Methods
```

---

# Licença

MIT License

@ Autor
Lucas Amaral Dourado

```
MetastableX
Computational Epidemiology Lab
```
