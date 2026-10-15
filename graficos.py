import numpy as np
import matplotlib.pyplot as plt


def plotar_grafico(f, raiz, a=None, b=None, nome_metodo=""):
    """Plota a função f(x), destaca a raiz encontrada e opcionalmente o intervalo [a, b]."""
    try:
        if a is not None and b is not None:
            margem = (b - a) * 0.2 if b != a else 1.0
            x_vals = np.linspace(min(a, raiz) - margem, max(b, raiz) + margem, 400)
        else:
            x_vals = np.linspace(raiz - 3, raiz + 3, 400)

        y_vals = f(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label="f(x)", color="royalblue", linewidth=2)
        plt.axhline(0, color="black", linewidth=1, linestyle="--")

        y_raiz = f(raiz)
        plt.scatter([raiz], [y_raiz], color="red", zorder=5, s=80, label=f"Raiz: {raiz:.5f}")

        if a is not None and b is not None:
            plt.axvline(a, color="green", linestyle=":", alpha=0.7, label=f"a ({a})")
            plt.axvline(b, color="orange", linestyle=":", alpha=0.7, label=f"b ({b})")

        plt.title(f"Gráfico da Função - {nome_metodo}", fontsize=12, fontweight='bold')
        plt.xlabel("x", fontsize=10)
        plt.ylabel("f(x)", fontsize=10)
        plt.axvline(0, color="gray", linewidth=0.8, alpha=0.5)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"\n[Aviso]: Não foi possível gerar o gráfico automaticamente: {e}")
