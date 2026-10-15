import time
from utils import obter_intervalo_valido
from graficos import plotar_grafico

def Bisseccao(f, df, erro, max_iteracoes):
    #Obtenção e validação do intervalo [a,b]
    a, b, fa, fb, raiz_exata = obter_intervalo_valido(f, df, "Bissecção")

    #Se houver raiz exata quer dizer que um dos valores (a ou b) já é raiz daquela função.
    if raiz_exata:
        plotar_grafico(f, a, a, b, "Método da Bissecção")
        return a, 0, 0.0, 0.0

    print("Executando bissecção...")

    a_orig = a
    b_orig = b
    #Início contador do tempo de execução
    inicio = time.perf_counter()

    #Aplicação do método da bissecção
    aux = (a + b) / 2.0
    faux = f(aux)
    n = 0

    #Laço para permanecer em loop enquanto não estiver em precisão aceitável e for menor que o limite de iterações
    while (abs(faux) > erro) and (n < max_iteracoes):
        n += 1
        if (faux * fa) < 0:
            b = aux
        else:
            a = aux
            fa = faux
        aux = (a + b) / 2.0
        faux = f(aux)

    #Final do contador
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

    #Plotagem do gráfico
    plotar_grafico(f, aux, a=a_orig, b=b_orig, nome_metodo="Método da Bissecção")
    return aux, n, tempo_ms, residuo
