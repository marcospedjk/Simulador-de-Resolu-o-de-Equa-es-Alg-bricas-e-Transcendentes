import time
from utils import obter_intervalo_valido
from graficos import plotar_grafico

def Bisseccao(f, df, erro, max_iteracoes):
    a, b, fa, fb, raiz_exata = obter_intervalo_valido(f, df, "Bissecção")

    if raiz_exata:
        plotar_grafico(f, a, a, b, "Método da Bissecção")
        return a, 0, 0.0, 0.0

    print("Executando bissecção...")
    inicio = time.perf_counter()

    aux = (a + b) / 2.0
    faux = f(aux)
    n = 0

    while (abs(faux) > erro) and (n < max_iteracoes):
        n += 1
        if (faux * fa) < 0:
            b = aux
        else:
            a = aux
            fa = faux
        aux = (a + b) / 2.0
        faux = f(aux)

    fim = time.perf_counter()
    tempo_ms = (fim - inicio) * 1000
    residuo = abs(faux)

    print("\n" + "=" * 45)
    print("        RESULTADOS - MÉTODO DA BISSECÇÃO        ")
    print("=" * 45)
    print(f"Raiz aproximada         : {aux:.8f}")
    print(f"Número de iterações     : {n}")
    print(f"Tempo de execução       : {tempo_ms:.4f} ms")
    print(f"Precisão final |f(raiz)| : {residuo:.4e}")
    print("=" * 45)

    plotar_grafico(f, aux, a, b, "Método da Bissecção")
    return aux, n, tempo_ms, residuo
