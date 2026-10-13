import time
from utils import obter_intervalo_valido


def FalsaPosicao(f, df, erro, max_iteracoes):
    a, b, fa, fb, raiz_exata = obter_intervalo_valido(f, df, "Falsa Posição")

    if raiz_exata:
        return a, 0, 0.0, 0.0

    print("Executando falsa posição...")
    inicio = time.perf_counter()

    n = 0
    aux = (a * fb - b * fa) / (fb - fa)
    faux = f(aux)

    while (abs(faux) > erro) and (n < max_iteracoes):
        n += 1
        if (fa * faux) < 0:
            b = aux
            fb = faux
        else:
            a = aux
            fa = faux

        aux = (a * fb - b * fa) / (fb - fa)
        faux = f(aux)

    fim = time.perf_counter()
    tempo_ms = (fim - inicio) * 1000
    residuo = abs(faux)

    print("\n" + "=" * 45)
    print("         RESULTADOS - MÉTODO DA FALSA POSIÇÃO        ")
    print("=" * 45)
    print(f"Raiz aproximada         : {aux:.8f}")
    print(f"Número de iterações     : {n}")
    print(f"Tempo de execução       : {tempo_ms:.4f} ms")
    print(f"Precisão final |f(raiz)| : {residuo:.4e}")
    print("=" * 45)

    return aux, n, tempo_ms, residuo
