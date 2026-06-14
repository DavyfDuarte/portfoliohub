alunos = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ").strip()
    if nome == "":
        print("Nome nao pode ser vazio.")
        return
    curso = input("Digite o curso: ").strip()
    nota  = float(input("Digite a nota do aluno (0 a 10): "))

    if nota < 0 or nota > 10:
        print("Nota invalida. Deve ser entre 0 e 10.")
        return

    if nota >= 5:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    aluno = {
        "nome": nome,
        "curso": curso,
        "nota": nota,
        "situacao": situacao
    }
    alunos.append(aluno)
    print(f"\nAluno '{nome}' cadastrado com sucesso! Situacao: {situacao}")

def listar_alunos():
    if len(alunos) == 0:
        print("\nNenhum aluno cadastrado ainda.")
        return
    print("\n" + "="*45)
    print(f"{'NOME':<20} {'CURSO':<15} {'NOTA':<6} {'SITUACAO'}")
    print("="*45)
    for aluno in alunos:
        print(f"{aluno['nome']:<20} {aluno['curso']:<15} {aluno['nota']:<6} {aluno['situacao']}")
    print("="*45)
    print(f"Total de alunos cadastrados: {len(alunos)}")

def buscar_aluno():
    nome_busca = input("Digite o nome do aluno: ").strip().lower()
    encontrados = []
    for aluno in alunos:
        if nome_busca in aluno["nome"].lower():
            encontrados.append(aluno)

    if len(encontrados) == 0:
        print("Nenhum aluno encontrado com esse nome.")
    else:
        print(f"\n{len(encontrados)} aluno(s) encontrado(s):")
        for aluno in encontrados:
            print(f"  Nome: {aluno['nome']}")
            print(f"  Curso: {aluno['curso']}")
            print(f"  Nota: {aluno['nota']}")
            print(f"  Situacao: {aluno['situacao']}")
            print()

def remover_aluno():
    nome_remover = input("Digite o nome do aluno para remover: ").strip().lower()
    for i, aluno in enumerate(alunos):
        if aluno["nome"].lower() == nome_remover:
            alunos.pop(i)
            print(f"Aluno '{aluno['nome']}' removido com sucesso.")
            return
    print("Aluno nao encontrado.")

def calcular_media():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    soma = 0
    for aluno in alunos:
        soma += aluno["nota"]
    media = soma / len(alunos)
    aprovados   = sum(1 for a in alunos if a["situacao"] == "Aprovado")
    reprovados  = sum(1 for a in alunos if a["situacao"] == "Reprovado")
    print(f"\nMedia da turma: {media:.2f}")
    print(f"Aprovados:  {aprovados}")
    print(f"Reprovados: {reprovados}")

def exibir_menu():
    print("\n" + "="*45)
    print("       SISTEMA DE CADASTRO DE ALUNOS")
    print("="*45)
    print("1. Cadastrar aluno")
    print("2. Listar todos os alunos")
    print("3. Buscar aluno pelo nome")
    print("4. Remover aluno")
    print("5. Ver media e estatisticas da turma")
    print("6. Sair")
    print("="*45)

def main():
    print("\nSistema de Cadastro de Alunos")
    print("Logica de Programacao — CEUB 2026")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            buscar_aluno()
        elif opcao == "4":
            remover_aluno()
        elif opcao == "5":
            calcular_media()
        elif opcao == "6":
            print("\nEncerrando o sistema. Ate logo!")
            break
        else:
            print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()
