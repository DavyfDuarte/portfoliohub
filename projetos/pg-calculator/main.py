def calcular_termos_pg(primeiro_termo, razao, quantidade):
    termos = []
    for i in range(quantidade):
        termo = primeiro_termo * (razao ** i)
        termos.append(round(termo, 2))
    return termos

def calcular_soma_pg(primeiro_termo, razao, quantidade):
    if razao == 1:
        return primeiro_termo * quantidade
    soma = primeiro_termo * (1 - razao ** quantidade) / (1 - razao)
    return round(soma, 2)

def calcular_razao(primeiro_termo, segundo_termo):
    if primeiro_termo == 0:
        print("Erro: o primeiro termo nao pode ser zero.")
        return None
    return round(segundo_termo / primeiro_termo, 4)

def exibir_menu():
    print("\n" + "="*45)
    print("     CALCULADORA DE PROGRESSAO GEOMETRICA")
    print("="*45)
    print("1. Calcular termos da PG")
    print("2. Calcular soma dos termos")
    print("3. Descobrir a razao entre dois termos")
    print("4. Sair")
    print("="*45)

def main():
    print("\nBem-vindo ao calculador de Progressao Geometrica!")
    print("Projeto - Matematica para Computacao | CEUB 2026")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            try:
                a1 = float(input("Digite o primeiro termo (a1): "))
                q  = float(input("Digite a razao (q): "))
                n  = int(input("Quantos termos deseja calcular? "))
                if n <= 0:
                    print("A quantidade deve ser maior que zero.")
                    continue
                termos = calcular_termos_pg(a1, q, n)
                print(f"\nTermos da PG: {termos}")
            except ValueError:
                print("Entrada invalida. Digite apenas numeros.")

        elif opcao == "2":
            try:
                a1 = float(input("Digite o primeiro termo (a1): "))
                q  = float(input("Digite a razao (q): "))
                n  = int(input("Quantos termos deseja somar? "))
                if n <= 0:
                    print("A quantidade deve ser maior que zero.")
                    continue
                soma = calcular_soma_pg(a1, q, n)
                termos = calcular_termos_pg(a1, q, n)
                print(f"\nTermos: {termos}")
                print(f"Soma dos {n} termos: {soma}")
            except ValueError:
                print("Entrada invalida. Digite apenas numeros.")

        elif opcao == "3":
            try:
                a1 = float(input("Digite o primeiro termo: "))
                a2 = float(input("Digite o segundo termo: "))
                razao = calcular_razao(a1, a2)
                if razao is not None:
                    print(f"\nA razao da PG e: {razao}")
            except ValueError:
                print("Entrada invalida. Digite apenas numeros.")

        elif opcao == "4":
            print("\nEncerrando o programa. Ate logo!")
            break

        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()
