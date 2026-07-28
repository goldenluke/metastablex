<h1 align="center">🧠 MetastableX</h1>
<h3 align="center">A Computational Framework for Metastability, Critical Transitions, and Emergent Structure in Complex Systems</h3>

<p align="center">
A research framework to simulate, measure, and interpret metastable dynamics across physical, epidemiological, and informational systems.
</p>

<p align="center">
⚙️ PyTorch • 📊 Time-Series • 🧠 Complex Systems • 🌊 Nonlinear Dynamics • 📐 Fractals • 🏥 Public Health • 🤖 Machine Learning
</p>

---

# 📄 Article

Full theoretical foundation:

https://goldenluke.github.io/metastablex/

---

# 📌 Abstract

Complex systems do not operate in equilibrium — they evolve through **metastable regimes**, where transient structures emerge, persist, and dissolve.

**MetastableX** is a computational framework designed to:

- simulate metastable field dynamics (QWAN)
- detect critical transitions
- quantify emergent structure
- measure instability and complexity
- forecast systemic behavior

The framework integrates:

- statistical physics (free energy, entropy, criticality)
- nonlinear dynamics (Lyapunov spectrum, bifurcation, chaos, renormalization group)
- information theory (Shannon entropy, permutation entropy, mutual information)
- geometry (correlation dimension, multifractal spectrum, phase-space reconstruction)
- machine learning (GRU regime classification, HMM, clustering, neural ODEs)
- epidemiology (DATASUS / SIH-SUS, SIR dynamics)

---

# 🧠 1. Conceptual Foundation

MetastableX treats systems as:

> **fields evolving under competing forces of order and instability**

Instead of static states, the framework models:

- continuous transformation
- transient organization
- regime transitions

---

# ⚙️ 2. Core Mathematical Model (QWAN)

QWAN (the field-simulation engine) evolves a scalar field under gradient descent on a discrete Ginzburg-Landau / Allen-Cahn free energy. The field free energy is:

$$
E[x] = \sum_i \left[ \tfrac{1}{2}(x_{i+1}-x_i)^2 \;-\; \tfrac{1}{2}x_i^2 \;+\; \tfrac{1}{4}x_i^4 \right]
$$

— a discrete spatial-gradient term (periodic boundary) plus a symmetric double-well potential. Its functional gradient, obtained via autograd, gives the field evolution:

## Field Evolution

$$
x_{t+1} = x + \Delta t \,(\nabla^2 x + x - x^3)
$$

- diffusion (∇²x)
- nonlinear stabilization (−x³)
- growth term (+x)

Started from small random noise, the field relaxes toward the double well's minima (x = ±1), forming metastable domains separated by diffuse interfaces — the "emergent structure" the framework is built to measure. Entropy and coherence terms (weighted by `alpha`/`beta`) can be added on top of this base equation as additional adaptive forces.

## Energy (activity)

$$
\Phi = \langle x^2 \rangle
$$

## Variance / instability

$$
I = \langle (x - \mu)^2 \rangle
$$

## Lyapunov (proxy)

$$
\lambda \approx \log(\mathrm{Var}(x))
$$

A cheap sensitivity-to-perturbation proxy — not the formal dynamical-systems Lyapunov exponent (see §3 for that).

## KPZ (interface growth)

$$
W = \sqrt{\langle (h - \bar{h})^2 \rangle}
$$

## Fractal dimension

$$
D = \frac{\log N(\epsilon)}{\log(1/\epsilon)}
$$

---

# 🌊 3. Dynamical Systems Analysis

The rigorous chaos-theory toolkit lives mainly in the interactive backend (`metastablex_app/backend/qwan/`) and has been checked against known reference values (Lorenz attractor, logistic map) rather than left as untested formulas.

## 🔥 Chaos & Stability

- **Largest Lyapunov exponent** — Benettin's algorithm (reference + perturbed trajectory, periodic renormalization).
- **Lyapunov spectrum** (multi-dimensional) — Benettin's algorithm with Gram-Schmidt reorthonormalization of the tangent vectors at every step; without it, all directions collapse onto the dominant one. Verified on independent logistic maps with known exponents (recovers all three to <1% error in float64).
- **Kaplan-Yorke dimension** — $D_{KY} = j + \dfrac{\sum_{i=1}^{j}\lambda_i}{|\lambda_{j+1}|}$, verified against the classic Lorenz attractor value (≈2.06).

## 🧭 Bifurcation Analysis

- Parameter scanning over the 2D Ginzburg-Landau field (CPU and GPU-accelerated variants)
- Phase diagrams over (coupling, noise)

## 🌀 Phase Space Reconstruction

- Takens delay embedding
- Optimal delay via first local minimum of time-delayed mutual information
- Optimal embedding dimension via false nearest neighbors
- Attractor classification (fixed point / limit cycle / strange attractor) — see §7

## 📐 Fractal & Multifractal Analysis

- Correlation dimension (Grassberger-Procaccia), with the scaling range derived from the data's own pairwise-distance distribution rather than a fixed absolute range
- MFDFA (multifractal detrended fluctuation analysis) — singularity spectrum α, f(α)

## 🔗 Correlation Dimension

$$
C(r) \sim r^D
$$

## 🧠 Entropy Measures

- Shannon entropy
- Permutation entropy (Bandt-Pompe)
- Mutual information

## 🔁 Renormalization Group Flow

Real-space RG: iterated coarse-graining of the series, extracting effective couplings at each scale — a correlation coupling ρ (fit as an AR(1) coefficient) and a residual noise coupling g — and tracking their flow to a fixed point. White noise flows to the trivial fixed point (ρ*≈0); a random walk sits near the non-trivial fixed point (ρ*≈1, g growing) — the two textbook universality classes.

---

# 🧬 4. Structure & Emergence

## 🔷 Cluster Detection

- connected components
- metastable domains

## 🧭 Cluster Tracking

- persistent IDs
- trajectory tracking
- merging (coalescence)
- splitting (fission)

## 📏 Geometry

- perimeter
- roughness
- interface analysis

## 📈 Growth Dynamics

- domain growth velocity
- KPZ scaling behavior

## 🔥 Nucleation Detection

- automatic emergence of structure
- early phase transitions

---

# 📊 5. Time-Series Intelligence

## 📉 Early Warning Signals

- variance increase
- autocorrelation increase (critical slowing down)
- entropy peaks
- a composite instability index (`metastablex.core.instability`)

## 🤖 Machine Learning

- GRU-based regime classification and forecasting (`MetastableXModel`)
- Gaussian HMM regime detection
- Q-learning control
- Neural ODE (learns the field's own vector field dx/dt)

## 🧠 Clustering

- temporal clustering of regimes (K-means over rolling windows)
- automatic segmentation

---

# 🏥 6. Epidemiological Layer

## DATASUS Integration

- SIH/SUS ingestion
- multi-state, multi-year analysis
- municipality-level resolution

## 🦠 COVID Detection

- CID filtering (U07, B34)
- detection as phase transition

## 📊 Indicators

- hospitalization dynamics
- chronic disease burden
- regional clustering

## ⚙️ SIR + ML

$$
\frac{dS}{dt} = -\beta\frac{SI}{N}, \qquad
\frac{dI}{dt} = \beta\frac{SI}{N} - \gamma I, \qquad
\frac{dR}{dt} = \gamma I
$$

Frequency-dependent transmission (normalized by population N) — combined with ML for prediction and anomaly detection.

## Interpretation & reporting

- natural-language interpretation of metrics (medical / scientific-paper modes)
- local LLM integration (Ollama / Llama 3) for narrative explanation, no external API
- PDF report generation

Pipeline: `data → physics → dynamics → structure → metrics → interpretation`

---

# 🧪 7. Simulation Engine

## QWAN (Quantum Wave Adaptive Network)

- metastable field dynamics
- emergent structure formation
- continuous evolution

## Features

- real-time simulation
- GPU acceleration (PyTorch)
- multi-instance QWAN
- scenario comparison

## Regime & attractor classification

Rather than fixed magnitude thresholds, the streaming detectors use statistically grounded criteria: the sign of the Lyapunov exponent plus a one-sample t-test for `RegimeAlert`; distance to the field's own theoretical fixed point (Φ*=1, I*=0) for `RegimeDetector`; and, for `AttractorDetector`, an F-test (level variance vs. a noise floor estimated by differencing) for fixed points plus a local-peak autocorrelation test (not just "any value above the confidence band," which would misclassify a smooth random walk as periodic) for limit cycles.

---

# 🎛 8. Interactive System

- real-time WebSocket simulation (Django Channels)
- dashboard interface (React)
- glassmorphism UI
- live metrics visualization

## Visual Capabilities

- field rendering
- cluster visualization
- trajectories
- energy heatmaps
- bifurcation heatmaps

---

# 📦 Installation

```bash
pip install metastablex
```

---

# 🚀 Quick Example

```python
from metastablex import MetastableModel
import numpy as np

series = np.sin(np.linspace(0, 20, 200)) + np.random.randn(200) * 0.05

model = MetastableModel().fit(series)
score = model.predict(series)

print(score, model.classify(score))
```

Simulating the QWAN field directly:

```python
import torch
from metastablex.qwan.dynamics import evolve

x0 = 0.1 * torch.randn(64)
x_final, history = evolve(x0, steps=300, dt=0.01, alpha=0.0, beta=0.0, k=0.0, sigma=0.0)

print(history[-1])   # {"H": ..., "I": ..., "Phi": ...}
print(x_final.min().item(), x_final.max().item())  # relaxes toward the double-well minima, ~±1
```
