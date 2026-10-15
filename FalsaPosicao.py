import time
from utils import obter_intervalo_valido
from graficos import plotar_grafico

def FalsaPosicao(f, df, erro, max_iteracoes):
    a, b, fa, fb, raiz_exata = obter_intervalo_valido(f, df, "Falsa Posição")

    if raiz_exata:
        plotar_grafico(f, a, a, b, "Método da Falsa Posição")
        return a, 0, 0.0, 0.0

    print("\nExecutando falsa posição...")
    inicio = time.perf_counter()

    n = 0
    denominador = fb - fa

    if abs(denominador) < 1e-15:
        print("\n[Erro]: f(b) - f(a) é zero ou próximo de zero. Não é possível iniciar o método.")
        return None, n, 0.0, 0.0

    aux = (a * fb - b * fa) / denominador
    faux = f(aux)
    ultima_aux = aux

    while (abs(faux) > erro) and (n < max_iteracoes):
        n += 1
        if (fa * faux) < 0:
            b = aux
            fb = faux
        else:
            a = aux
            fa = faux

        denominador = fb - fa

        if abs(denominador) < 1e-15:
            print(f"\n[Aviso]: Divisão por zero detectada na iteração {n} (estagnação do método).")
            print(f"Interrupção antecipada. Última aproximação válida: {ultima_aux:.8f}")
            aux = ultima_aux
            break

        ultima_aux = aux
        aux = (a * fb - b * fa) / denominador
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

    plotar_grafico(f, aux, a, b, "Método da Falsa Posição")
    return aux, n, tempo_ms, residuo
