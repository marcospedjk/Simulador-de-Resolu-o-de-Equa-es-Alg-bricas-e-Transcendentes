import time
import numpy as np
from graficos import plotar_grafico

def NewtonRaphson(f, df, erro, max_iteracoes):
    print("\n" + "-" * 40)
    print("MÉTODO DE NEWTON-RAPHSON: PONTO INICIAL")
    print("-" * 40)

    #Obtenção e validação do x0
    while True:
        try:
            x0 = float(input("Digite o ponto inicial (x0): "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    #Obtendo f(x0) e validando se ele é matematicamente possível
    try:
        fx0 = float(f(x0))
    except Exception as e:
        print(f"[Erro ao avaliar f(x0)]: {e}")
        return x0, 0, 0.0, 0.0

    #Caso em que x0 é uma raiz aceitável (com precisão suficiente)
    if abs(fx0) <= erro:
        print(f"\nO ponto inicial já satisfaz a tolerância: x0 = {x0:.8f}")
        plotar_grafico(f, x0, nome_metodo="Método de Newton-Raphson")
        return x0, 0, 0.0, abs(fx0)

    print("\nA executar o método de Newton-Raphson...")

    #Inicio do contador de performance
    inicio = time.perf_counter()

    k = 0
    xk = x0
    sucesso = False #Variavel auxiliar para definir êxito ou não

    #Laço enquanto não atingir o máximo de iterações definidas (que é definido por padrão como 100)
    while k < max_iteracoes:
        k += 1

        #Obtenção e validação de df(xk)
        try:
            dfxk = float(df(xk))
        except Exception as e:
            print(f"\n[Erro ao avaliar f'({xk})]: {e}")
            break

        #Verificação se df(xk) ~ 0, para não haver overflow nem indeterminação
        if abs(dfxk) < 1e-15:
            print(f"\n[Erro]: f'({xk:.8f}) é aproximadamente zero (tangente horizontal).")
            print("O método de Newton-Raphson não pode prosseguir sem divisão por zero.")
            break

        #Aplicação do método de Newton-Raphson
        fxk = float(f(xk))
        x_proximo = xk - (fxk / dfxk)

        # Verificação dos critérios de parada: resíduo da função (|f(x)| <= erro) ou variação relativa (|dx/x| <= erro)
        try:
            fx_proximo = float(f(x_proximo))
        except Exception as e:
            print(f"\n[Erro ao avaliar f({x_proximo})]: {e}")
            break

        criterio_f = abs(fx_proximo) <= erro

        if abs(x_proximo) > 1e-15:
            criterio_x = abs((x_proximo - xk) / x_proximo) <= erro
        else:
            criterio_x = abs(x_proximo - xk) <= erro

        xk = x_proximo

        if criterio_f or criterio_x:
            sucesso = True
            break
    #Fim do contador
    fim = time.perf_counter()
    tempo_ms = (fim - inicio) * 1000
    residuo = abs(float(f(xk)))

    print("\n" + "=" * 45)
    print("     RESULTADOS - MÉTODO DE NEWTON-RAPHSON    ")
    print("=" * 45)
    print(f"Raiz aproximada         : {xk:.8f}")
    print(f"Número de iterações (k) : {k}")
    print(f"Tempo de execução       : {tempo_ms:.4f} ms")
    print(f"Precisão final |f(raiz)| : {residuo:.4e}")
    if not sucesso and k >= max_iteracoes:
        print("[Aviso]: O limite máximo de iterações foi atingido sem atingir a precisão.")
    print("=" * 45)
    #Plotagem do gráfico da função
    plotar_grafico(f, xk, nome_metodo="Método de Newton-Raphson")
    return xk, k, tempo_ms, residuo
