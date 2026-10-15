import numpy as np
from graficos import plotar_grafico

def validar_condicoes_newton(f, df, d2f, a, b, num_pontos=100):
    pontos = np.linspace(a, b, num_pontos)

    try:
        valores_f = f(pontos)
        valores_df = df(pontos)
        valores_d2f = d2f(pontos)

        if (
            np.any(np.isnan(valores_f))
            or np.any(np.isinf(valores_f))
            or np.any(np.isnan(valores_df))
            or np.any(np.isinf(valores_df))
        ):
            print(
                "[Erro]: A função ou sua derivada possui descontinuidade/assíntota no intervalo."
            )
            return False, None

        if f(a) * f(b) >= 0:
            print("[Erro]: f(a) * f(b) >= 0. Não há garantia de raiz.")
            return False, None

        df_pos = np.all(valores_df > 0)
        df_neg = np.all(valores_df < 0)
        if not (df_pos or df_neg):
            print(
                "[Erro]: f'(x) troca de sinal ou se anula. Não há garantia de raiz única ou tangente horizontal."
            )
            return False, None

        d2f_a = d2f(a)
        d2f_b = d2f(b)

        if f(a) * d2f_a > 0:
            x0 = a
        elif f(b) * d2f_b > 0:
            x0 = b
        else:
            x0 = (a + b) / 2.0

        return True, x0

    except Exception as e:
        print(f"[Erro numérico]: {e}")
        return False, None


import time
import numpy as np


def NewtonRaphson(f, df, erro, max_iteracoes):
    print("\n" + "-" * 40)
    print("MÉTODO DE NEWTON-RAPHSON: PONTO INICIAL")
    print("-" * 40)

    while True:
        try:
            x0 = float(input("Digite o ponto inicial (x0): "))
            break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    try:
        fx0 = float(f(x0))
    except Exception as e:
        print(f"[Erro ao avaliar f(x0)]: {e}")
        return x0, 0, 0.0, 0.0

    if abs(fx0) <= erro:
        print(f"\nO ponto inicial já satisfaz a tolerância: x0 = {x0:.8f}")
        return x0, 0, 0.0, abs(fx0)

    print("\nA executar o método de Newton-Raphson...")

    inicio = time.perf_counter()

    k = 0
    xk = x0
    sucesso = False

    while k < max_iteracoes:
        k += 1

        try:
            dfxk = float(df(xk))
        except Exception as e:
            print(f"\n[Erro ao avaliar f'({xk})]: {e}")
            break

        if abs(dfxk) < 1e-15:
            print(f"\n[Erro]: f'({xk:.8f}) é aproximadamente zero (tangente horizontal).")
            print("O método de Newton-Raphson não pode prosseguir sem divisão por zero.")
            break

        fxk = float(f(xk))
        x_proximo = xk - (fxk / dfxk)

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
    plotar_grafico(f, xk, nome_metodo="Método de Newton-Raphson")
    return xk, k, tempo_ms, residuo
