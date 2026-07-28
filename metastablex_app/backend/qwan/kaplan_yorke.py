def kaplan_yorke_dimension(lyap):
    """
    D_KY = j + (Σ_{i=1}^{j} λ_i) / |λ_{j+1}|, onde j é o maior número
    de expoentes (em ordem decrescente) cuja soma acumulada
    permanece não-negativa.
    """

    lyap = sorted(lyap, reverse=True)

    total = 0.0
    count = 0

    for val in lyap:
        if total + val < 0:
            break
        total += val
        count += 1

    if count == len(lyap):
        # soma de todos os expoentes ainda não-negativa: não há
        # λ_{j+1} para o termo fracionário
        return float(count)

    next_exp = lyap[count]

    if next_exp == 0:
        return float(count)

    return count + total / abs(next_exp)
