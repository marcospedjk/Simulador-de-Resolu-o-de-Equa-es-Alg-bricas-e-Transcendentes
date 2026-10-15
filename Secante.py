import time
import numpy as np
from graficos import plotar_grafico
def Secante(f, df, erro, max_iteracoes):
    print("\n" + "-" * 40)
    print("MÉTODO DA SECANTE: ESTIMATIVAS INICIAIS")
    print("-" * 40)

    while True:
        try:
            x0 = float(input("Digite a primeira estimativa inicial (x0): "))
            x1 = float(input("Digite a segunda estimativa inicial (x1): "))
            break
        except ValueError:
            print("Entrada inválida. Digite valores numéricos.")

    print("\nExecutando o método da secante...")
    inicio = time.perf_counter()

    n = 0
    fx0 = f(x0)
    fx1 = f(x1)

    # Variável para guardar a última aproximação segura caso ocorra divisão por zero
    ultima_x = x1

    while n < max_iteracoes:
        denominador = fx1 - fx0

        # Proteção contra divisão por zero
        if abs(denominador) < 1e-15:
            print(f"\n[Aviso]: Divisão por zero detectada na iteração {n+1} (f(x1) - f(x0) é zero).")
            print(f"Interrupção antecipada. Última aproximação válida: {ultima_x:.8f}")
            x1 = ultima_x
            break

        # Fórmula do Método da Secante
        x2 = x1 - (fx1 * (x1 - x0)) / denominador
        fx2 = f(x2)

        n += 1
        ultima_x = x2

        # Critério de parada (baseado na tolerância do erro ou na diferença entre aproximações)
        if abs(fx2) < erro or abs(x2 - x1) < erro:
            x1 = x2
            break

        # Atualiza os pontos para a próxima iteração
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = fx2import time
import numpy as np

def Secante(f, df, erro, max_iteracoes):
    print("\n" + "-" * 40)
    print("MÉTODO DA SECANTE: ESTIMATIVAS INICIAIS")
    print("-" * 40)

    while True:
        try:
            x0 = float(input("Digite a primeira estimativa inicial (x0): "))
            x1 = float(input("Digite a segunda estimativa inicial (x1): "))
            break
        except ValueError:
            print("Entrada inválida. Digite valores numéricos.")

    print("\nExecutando o método da secante...")
    inicio = time.perf_counter()

    n = 0
    fx0 = f(x0)
    fx1 = f(x1)

    # Variável para guardar a última aproximação segura caso ocorra divisão por zero
    ultima_x = x1

    while n < max_iteracoes:
        denominador = fx1 - fx0

        # Proteção contra divisão por zero
        if abs(denominador) < 1e-15:
            print(f"\n[Aviso]: Divisão por zero detectada na iteração {n+1} (f(x1) - f(x0) é zero).")
            print(f"Interrupção antecipada. Última aproximação válida: {ultima_x:.8f}")
            x1 = ultima_x
            break

        # Fórmula do Método da Secante
        x2 = x1 - (fx1 * (x1 - x0)) / denominador
        fx2 = f(x2)

        n += 1
        ultima_x = x2

        # Critério de parada (baseado na tolerância do erro ou na diferença entre aproximações)
        if abs(fx2) < erro or abs(x2 - x1) < erro:
            x1 = x2
            break

        # Atualiza os pontos para a próxima iteração
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = fx2

    fim = time.perf_counter()
    tempo_ms = (fim - inicio) * 1000
    residuo = abs(f(x1))

    print("\n" + "=" * 45)
    print("         RESULTADOS - MÉTODO DA SECANTE         ")
    print("=" * 45)
    print(f"Raiz aproximada         : {x1:.8f}")
    print(f"Número de iterações     : {n}")
    print(f"Tempo de execução       : {tempo_ms:.4f} ms")
    print(f"Precisão final |f(raiz)| : {residuo:.4e}")
    print("=" * 45)

    return x1, n, tempo_ms, residuo

    fim = time.perf_counter()
    tempo_ms = (fim - inicio) * 1000
    residuo = abs(f(x1))

    print("\n" + "=" * 45)
    print("         RESULTADOS - MÉTODO DA SECANTE         ")
    print("=" * 45)
    print(f"Raiz aproximada         : {x1:.8f}")
    print(f"Número de iterações     : {n}")
    print(f"Tempo de execução       : {tempo_ms:.4f} ms")
    print(f"Precisão final |f(raiz)| : {residuo:.4e}")
    print("=" * 45)
plotar_grafico(f, x1, nome_metodo="Método da Secante")
    return x1, n, tempo_ms, residuo
