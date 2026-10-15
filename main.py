import sympy as sp
from utils import ler_funcao
from Bisseccao import Bisseccao
from FalsaPosicao import FalsaPosicao
from Secante import Secante
from NewtonRaphson import NewtonRaphson


#Esta função é somente para criar a interface, ou seja, ela é responsável pelo I/O (input e output)
def main():
    print("=" * 55)
    print(" SIMULADOR DE ZEROS DE EQUAÇÕES TRANSCENDENTES ")
    print("=" * 55)

    expr_simb, f_num, df_num = ler_funcao()
    erro = 0.000001
    max_iteracoes = 100

    while True:
        print("\n" + "=" * 40)
        print("PAINEL DE CONTROLE / MENU PRINCIPAL")
        print("=" * 40)
        print(f"Função atual       : {expr_simb}")
        print(f"Precisão (ϵ)       : {erro}")
        print(f"Máximo de iterações: {max_iteracoes}")
        print("-" * 40)
        print("[1] Bissecção")
        print("[2] Falsa-posição")
        print("[3] Newton-Raphson")
        print("[4] Secante")
        print("[R] Redefinir tolerância (ϵ) ou iterações máximas")
        print("[F] Trocar a função f(x)")
        print("[5] Sair do programa")
        print("-" * 40)

        opcao = input("Escolha uma opção: ").strip().lower()

        if opcao == "1":
            Bisseccao(f_num, df_num, erro, max_iteracoes)
        elif opcao == "2":
            FalsaPosicao(f_num, df_num, erro, max_iteracoes)
        elif opcao == "3":
            NewtonRaphson(f_num, df_num, erro, max_iteracoes)
        elif opcao == "4":
            Secante(f_num, df_num, erro, max_iteracoes)
        elif opcao == "r":
            try:
                novo_erro = float(sp.sympify(input(f"Nova tolerância ϵ (atual = {erro}): ")))
                novas_iter = int(input(f"Novo limite de iterações (atual = {max_iteracoes}): "))
                erro = novo_erro
                max_iteracoes = novas_iter
                print("\n[Sucesso]: Parâmetros atualizados com sucesso!")
            except Exception as e:
                print(f"[Erro]: Entrada inválida ({e}). Parâmetros mantidos.")
        elif opcao == "f":
            expr_simb, f_num, df_num = ler_funcao()
        elif opcao == "5":
            print("\nEncerrando o programa.")
            break
        else:
            print("\nOpção inválida! Digite 1, 2, 3, 4, R, F ou 5.")

        input("\nPressione enter para continuar...")


if __name__ == "__main__":
    main()
