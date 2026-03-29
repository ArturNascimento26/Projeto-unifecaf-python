
def cadastrar_peca(pecas, caixas, caixa_atual):
    id_peca = input("Digite o ID da peca: ")
    peso = float(input("Digite o peso da peca (g): "))
    cor = input("Digite a cor da peca: ")
    comprimento = float(input("Digite o comprimento da peca (cm): "))

    motivos = []
    if not (95 <= peso <= 105):
        motivos.append("peso fora do intervalo (95g a 105g)")
    if cor.lower() not in ["azul", "verde"]:
        motivos.append("cor invalida (aceitas: azul ou verde)")
    if not (10 <= comprimento <= 20):
        motivos.append("comprimento fora do intervalo (10cm a 20cm)")

    aprovada = len(motivos) == 0

    peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento, "aprovada": aprovada, "motivos": motivos}
    pecas.append(peca)

    if aprovada:
        caixa_atual.append(peca)
        print(f"Peca {id_peca} aprovada e adicionada a caixa atual ({len(caixa_atual)}/10).")
        if len(caixa_atual) == 10:
            caixas.append(caixa_atual.copy())
            print(f"Caixa {len(caixas)} fechada com 10 pecas!")
            caixa_atual.clear()
    else:
        print(f"Peca {id_peca} reprovada pelos seguintes motivos:")
        for motivo in motivos:
            print(f"  - {motivo}")


def listar_pecas(pecas):
    print("\nLista de pecas:")
    for indice, peca in enumerate(pecas, start=1):
        status = "aprovada" if peca["aprovada"] else "reprovada"
        print(f"{indice}. ID: {peca['id']} | {status} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
        if not peca["aprovada"]:
            for motivo in peca["motivos"]:
                print(f" - {motivo}")



def remover_peca(pecas, caixa_atual):



def listar_caixas(caixas, caixa_atual):



def gerar_relatorio(pecas, caixas, caixa_atual):


print("\nGestão de Peças, Qaulidade e Armazenamento")
print("1. Cadastrar nova peça")
print("2. Listar peças aprovadas/reprovadas")
print("3. Remover peça cadastrada")
print("4. Listar caixas fechadas")
print("5. Gerar relatório final")
print("6. Sair")

opcao = input("Digite a opção desejada: ")

if opcao == "1":
        cadastrar_peca(pecas, caixas, caixa_atual)

elif opcao == "2":
        listar_pecas(pecas)

elif opcao == "3":
        remover_peca(pecas, caixa_atual)

elif opcao == "4":
        listar_caixas(caixas, caixa_atual)

elif opcao == "5":
        gerar_relatorio(pecas, caixas, caixa_atual)

elif opcao == "6":
    break



