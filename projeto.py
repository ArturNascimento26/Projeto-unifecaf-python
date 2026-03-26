
def cadastrar_peca():
  print("Preencha os dados da peça que deseja cadastrar")
  id_peca = input("Qual o id da peça? ")
  peso_peca = int(input("Qual o peso da peça? "))
  cor_peca = input("Qual a cor da peça? [azul/verde] ")
  comprimento_peca = int(input("Qual o comprimento da peça? "))

  criterios = []
  if not (95 <= peso_peca <= 105):  
      criterios.append("peso não se encaixa nos critérios de qualidade")

  if cor_peca not in ["azul", "verde"]:
      criterios.append("cor invalida (cores válidas: azul ou verde)")

  if not (10 <= comprimento_peca <= 20):
      criterios.append("comprimento não se encaixa nos critérios de qualidade")

  peca_aprovada = len(criterios) == 0

  peca = {"id": id_peca, "peso": peso_peca, "cor": cor_peca, "comprimento": comprimento_peca, "aprovada": peca_aprovada, "criterios": criterios}
  pecas.append(peca)

  if peca_aprovada:
      caixa_atual.append(peca)
      print(f"Peça {id_peca} aprovada e adicionada a caixa atual ({len(caixa_atual)}/10)")
      if len(caixa_atual) == 10:
        caixas.append(caixa_atual.copy())
        print(f"Caixa {len(caixas)} chegou ao limite com 10 peças!")
        caixa_atual.clear()

  else:
      print(f"Peça {id_peca} não atende aos seguintes requisitos: ")
      for criterio in criterios:
          print(f" - {criterio}")

print("\nGestão de Peças, Qaulidade e Armazenamento")
print("1. Cadastrar nova peça")
print("2. Listar peças aprovadas/reprovadas")
print("3. Remover peça cadastrada")
print("4. Listar caixas fechadas")
print("5. Gerar relatório final")
print("6. Sair")

opcao = input("Digite a opção desejada: ")



