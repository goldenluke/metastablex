import matplotlib.pyplot as plt


def plot_rg_flow(trajectory):
    """
    Desenha o diagrama de fluxo do grupo de renormalização: a
    trajetória das constantes de acoplamento efetivas (rho, g) no
    espaço de acoplamentos, à medida que a série é sucessivamente
    renormalizada (coarse-grained). O ponto fixo, se atingido, é
    destacado.

    `trajectory` é a lista de dicts retornada por
    metastablex.rg.flow.rg_flow / RegimeRG.flow.
    """

    rho = [point["rho"] for point in trajectory]
    g = [point["g"] for point in trajectory]
    scales = [point["scale"] for point in trajectory]

    fig, ax = plt.subplots(figsize=(7, 6))

    ax.plot(rho, g, marker="o", linestyle="-", color="steelblue")

    for r, gg, scale in zip(rho, g, scales):
        ax.annotate(f"b={scale}", (r, gg), textcoords="offset points", xytext=(6, 6))

    if trajectory[-1].get("fixed_point"):
        ax.scatter([rho[-1]], [g[-1]], color="crimson", zorder=5, label="ponto fixo")
        ax.legend()

    ax.set_xlabel("rho (acoplamento de correlação)")
    ax.set_ylabel("g (energia residual)")
    ax.set_title("Regime RG Flow")

    plt.show()
