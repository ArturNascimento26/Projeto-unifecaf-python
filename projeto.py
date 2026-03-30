def cadastrar_peca(pecas, caixas, caixa_atual):
    id_peca = input("Digite o ID da peca: ")
    peso = float(input("Digite o peso da peca: "))
    cor = input("Digite a cor da peca: ")
    comprimento = float(input("Digite o comprimento da peca: "))

    motivos = []
    if not (95 <= peso <= 105):
        motivos.append("peso fora do intervalo (95g a 105g)")
    if cor.lower() not in ["azul", "verde"]:
        motivos.append("cor invalida (cores aceitas: azul ou verde)")
    if not (10 <= comprimento <= 20):
        motivos.append("comprimento fora do intervalo (10cm a 20cm)")

    aprovada = len(motivos) == 0

    peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento, "aprovada": aprovada, "motivos": motivos}
    pecas.append(peca)

    if aprovada:
        caixa_atual.append(peca)
        print(f"Peca {id_peca} Aprovada e adicionada a caixa atual ({len(caixa_atual)}/10).")
        if len(caixa_atual) == 10:
            caixas.append(caixa_atual.copy())
            print(f"Caixa {len(caixas)} fechada com 10 pecas!")
            caixa_atual.clear()
    else:
        print(f"Peca {id_peca} Reprovada pelos seguintes motivos:")
        for motivo in motivos:
            print(f"  - {motivo}")



def listar_pecas(pecas):
    print("\nLista de pecas:")
    for indice, peca in enumerate(pecas, start=1):
        status = "Aprovada" if peca["aprovada"] else "Reprovada"
        print(f"{indice}. ID: {peca['id']} | {status} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
        if not peca["aprovada"]:
            for motivo in peca["motivos"]:
                print(f"     - {motivo}")



def remover_peca(pecas, caixa_atual):
    listar_pecas(pecas)
    indice = int(input("Digite o numero da peca que deseja remover: ")) - 1
    if 0 <= indice < len(pecas):
        peca = pecas[indice]
        if peca in caixa_atual:
            caixa_atual.remove(peca)
        pecas.pop(indice)
        print(f"Peca removida com sucesso.")
    else:
        print("Indice invalido.")



def listar_caixas(caixas, caixa_atual):
    print(f"\nCaixas fechadas: {len(caixas)}")
    for indice, caixa in enumerate(caixas, start=1):
        print(f"\nCaixa {indice}:")
        for peca in caixa:
            print(f"  - ID: {peca['id']} | Peso: {peca['peso']}g | Cor: {peca['cor']} | Comprimento: {peca['comprimento']}cm")
    print(f"\nCaixa em aberto: {len(caixa_atual)}/10 pecas")



def gerar_relatorio(pecas, caixas, caixa_atual):
    aprovadas = [p for p in pecas if p["aprovada"]]
    reprovadas = [p for p in pecas if not p["aprovada"]]

    print("\nRELATORIO FINAL")
    print(f"Total de pecas cadastradas: {len(pecas)}")
    print(f"Pecas aprovadas: {len(aprovadas)}")
    print(f"Pecas reprovadas: {len(reprovadas)}")

    if reprovadas:
        print("\nMotivos de reprovacao:")
        for peca in reprovadas:
            print(f"  Peca {peca['id']}:")
            for motivo in peca["motivos"]:
                print(f"    - {motivo}")

    print(f"\nCaixas fechadas: {len(caixas)}")
    print(f"Caixa em aberto: {len(caixa_atual)}/10 pecas")



pecas = []
caixas = []
caixa_atual = []


while True:
    print("\nMenu do Sistema de Controle de Producao:")
    print("1. Cadastrar nova peca")
    print("2. Listar pecas aprovadas/reprovadas")
    print("3. Remover peca cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatorio final")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        cadastrar_peca(pecas, caixas, caixa_atual)

    elif escolha == "2":
        listar_pecas(pecas)

    elif escolha == "3":
        remover_peca(pecas, caixa_atual)

    elif escolha == "4":
        listar_caixas(caixas, caixa_atual)

    elif escolha == "5":
        gerar_relatorio(pecas, caixas, caixa_atual)

    elif escolha == "6":
        break