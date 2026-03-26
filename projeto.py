def cadastrar_peca():
  print("Preencha os dados da peça que deseja cadastrar")
  id_peca = input("Qual o id da peça? ")
  peso_peca = int(input("Qual o peso da peça? "))
  cor_peca = input("Qual a cor da peça? [azul/verde] ")
  comprimento_peca = int(input("Qual o comprimento da peça? "))

print("\nGestão de Peças, Qaulidade e Armazenamento")
print("1. Cadastrar nova peça")
print("2. Listar peças aprovadas/reprovadas")
print("3. Remover peça cadastrada")
print("4. Listar caixas fechadas")
print("5. Gerar relatório final")
print("6. Sair")

opcao = input("Digite a opção desejada: ")