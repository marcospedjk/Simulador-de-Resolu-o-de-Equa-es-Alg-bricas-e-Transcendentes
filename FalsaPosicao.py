import time
from Bisseccao import derivada_tem_sinal_constante


def FalsaPosicao(f, df, erro, max_iteracoes):
    print("\n" + "-" * 40)
    print("MÉTODO DA FALSA POSIÇÃO: DEFINIÇÃO DE INTERVALO")
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

    print("\nIntervalo válido aceito! Executando falsa posição...")


    inicio = time.perf_counter()

    n = 0
    # formula da falsa posição
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
    print("        RESULTADOS - MÉTODO DA FALSA POSIÇÃO        ")
    print("=" * 45)
    print(f"Raiz aproximada         : {aux:.8f}")
    print(f"Número de iterações     : {n}")
    print(f"Tempo de execução       : {tempo_ms:.4f} ms")
    print(f"Precisão final |f(raiz)| : {residuo:.4e}")
    print("=" * 45)
    return aux, n, tempo_ms, residuo

