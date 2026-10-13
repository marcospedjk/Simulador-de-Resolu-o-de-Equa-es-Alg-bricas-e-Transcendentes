import time
import numpy as np
import sympy as sp
from sympy import symbols, pretty_print, diff
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor
)

transformacoes = standard_transformations + (implicit_multiplication_application, convert_xor)
x = symbols("x")
contexto_local = {"e": sp.E, "E": sp.E}


def ler_funcao():
    while True:
        try:
            texto = input("\nInsira a função f(x): ")
            expr = parse_expr(texto, local_dict=contexto_local, transformations=transformacoes)

            f_num = sp.lambdify(x, expr, modules="numpy")
            df_num = sp.lambdify(x, diff(expr, x), modules="numpy")

            print("\nFunção interpretada:")
            pretty_print(expr)
            return expr, f_num, df_num
        except Exception as erro:
            print(f"[Erro ao interpretar a função]: {erro}. Tente novamente.")


def derivada_tem_sinal_constante(df, a, b, num_pontos=100):
    try:
        pontos = np.linspace(a, b, num_pontos)
        valores_df = df(pontos)

        if np.isscalar(valores_df):
            return valores_df != 0

        if np.any(np.isnan(valores_df)) or np.any(np.isinf(valores_df)):
            return False

        todos_positivos = np.all(valores_df > 0)
        todos_negativos = np.all(valores_df < 0)

        return todos_positivos or todos_negativos
    except Exception:
        return False


def Bisseccao(f, df, erro, max_iteracoes):
    print("\n" + "-" * 40)
    print("MÉTODO DA BISSECÇÃO: DEFINIÇÃO DE INTERVALO")
    print("-" * 40)

    while True:
        try:
            a = float(input("Digite o limite a: "))
            b = float(input("Digite o limite b: "))
            break
        except ValueError:
            print("Entrada inválida. Digite valores numéricos.")

    if a > b:
        a, b = b, a

    # Validação do intervalo e da derivada constante no intervalo
    while True:
        try:
            fa = float(f(a))
            fb = float(f(b))
        except Exception as e:
            print(f"\n[Erro ao avaliar função nos limites]: {e}. Escolha outro intervalo dentro do domínio.")
            a = float(input("Novo a: "))
            b = float(input("Novo b: "))
            if a > b: a, b = b, a
            continue

        if fa == 0.0:
            print(f"\nA raiz exata já é o limite inferior: {a}")
            return a, 0, 0.0, 0.0
        elif fb == 0.0:
            print(f"\nA raiz exata já é o limite superior: {b}")
            return b, 0, 0.0, 0.0

        if fa * fb >= 0:
            print("\n[Erro]: f(a) * f(b) >= 0. Não há mudança de sinal (Teorema de Bolzano não satisfeito).")
        elif not derivada_tem_sinal_constante(df, a, b):
            print("\n[Erro]: O sinal de f'(x) não é constante em [a, b]. O intervalo pode conter mais de uma raiz.")
        else:
            break

        a = float(input("Novo a: "))
        b = float(input("Novo b: "))
        if a > b:
            a, b = b, a

    print("\nIntervalo válido aceito! Executando bissecção...")

    # Início da medição de tempo
    inicio = time.perf_counter()

    aux = (a + b) / 2.0
    faux = f(aux)
    fa = f(a)
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
    print("       RESULTADOS - MÉTODO DA BISSECÇÃO       ")
    print("=" * 45)
    print(f"Raiz aproximada         : {aux:.8f}")
    print(f"Número de iterações     : {n}")
    print(f"Tempo de execução       : {tempo_ms:.4f} ms")
    print(f"Precisão final |f(raiz)| : {residuo:.4e}")
    print("=" * 45)

    return aux, n, tempo_ms, residuo


