# Sistema de Controle de Produção - UNIFECAF

## 📋 Descrição do Projeto

Este projeto é um **Sistema de Controle de Produção** desenvolvido em Python para gerenciar o cadastro, validação e organização de peças em caixas. O sistema foi desenvolvido para a UNIFECAF e funciona como um gestor de qualidade para peças industriais.

## 🎯 Funcionamento do Programa

O programa funciona com base em um **sistema de validação de peças** onde cada peça deve atender a critérios específicos para ser aprovada:

### Critérios de Validação:
- **Peso**: Deve estar entre **95g e 105g**
- **Cor**: Deve ser **azul** ou **verde**
- **Comprimento**: Deve estar entre **10cm e 20cm**

### Fluxo de Funcionamento:

1. **Cadastro de Peças**: Cada peça é cadastrada com ID, peso, cor e comprimento
2. **Validação Automática**: O sistema verifica se a peça atende aos critérios
3. **Armazenamento**: 
   - Peças **aprovadas** são adicionadas automaticamente à caixa atual
   - Cada caixa comporta **10 peças aprovadas**
   - Ao completar 10 peças, a caixa é fechada automaticamente
4. **Rastreamento**: Todas as peças (aprovadas e reprovadas) ficam registradas
5. **Relatório**: É possível gerar um relatório completo ao final

## 🚀 Como Executar o Programa

### Pré-requisitos:
- Python 3.x instalado em sua máquina
- Um editor de código ou terminal

### Passo a Passo:

#### 1️⃣ Abra o Terminal do Seu Editor de Código
- Se está usando **VS Code**, pressione `Ctrl + ` (backtick) ou vá em **Terminal > Novo Terminal**
- Se está usando **PyCharm**, vá em **View > Tool Windows > Terminal**
- Se está usando outro editor, procure pela opção Terminal/Console

#### 2️⃣ Navegue até a Pasta do Projeto
```bash
cd caminho/até/Projeto-unifecaf-python
```

Exemplo (Windows):
```bash
cd C:\Users\SeuUsuário\Documents\Projeto-unifecaf-python
```

Exemplo (Mac/Linux):
```bash
cd ~/Documents/Projeto-unifecaf-python
```

#### 3️⃣ Execute o Programa
```bash
python projeto.py
```

Ou, se você tem Python 3 instalado:
```bash
python3 projeto.py
```

#### 4️⃣ O Menu Aparecerá
O programa exibirá um menu interativo onde você pode escolher as opções.

## 📖 Menu do Sistema

Ao executar o programa, você verá:

```
Menu do Sistema de Controle de Producao:
1. Cadastrar nova peca
2. Listar pecas aprovadas/reprovadas
3. Remover peca cadastrada
4. Listar caixas fechadas
5. Gerar relatorio final
6. Sair
```

## 💡 Exemplos de Uso

### Exemplo 1: Cadastrando uma Peça Aprovada

```
Digite a sua escolha: 1

Digite o ID da peca: P001
Digite o peso da peca: 100
Digite a cor da peca: azul
Digite o comprimento da peca: 15

Peca P001 Aprovada e adicionada a caixa atual (1/10).
```

**O que aconteceu**: A peça P001 atende a todos os critérios (peso 100g está entre 95-105, cor é azul, comprimento 15cm está entre 10-20), então foi aprovada e adicionada à caixa.

### Exemplo 2: Cadastrando uma Peça Reprovada

```
Digite a sua escolha: 1

Digite o ID da peca: P002
Digite o peso da peca: 110
Digite a cor da peca: vermelho
Digite o comprimento da peca: 25

Peca P002 Reprovada pelos seguintes motivos:
  - peso fora do intervalo (95g a 105g)
  - cor invalida (cores aceitas: azul ou verde)
  - comprimento fora do intervalo (10cm a 20cm)
```

**O que aconteceu**: A peça P002 falha em todos os critérios. Não foi adicionada à caixa, apenas registrada no sistema.

### Exemplo 3: Listando Peças

```
Digite a sua escolha: 2

Lista de pecas:
1. ID: P001 | Aprovada | Peso: 100g | Cor: azul | Comprimento: 15cm
2. ID: P002 | Reprovada | Peso: 110g | Cor: vermelho | Comprimento: 25cm
     - peso fora do intervalo (95g a 105g)
     - cor invalida (cores aceitas: azul ou verde)
     - comprimento fora do intervalo (10cm a 20cm)
```

### Exemplo 4: Cadastrando 10 Peças para Fechar uma Caixa

Suponha que você cadastre 9 peças aprovadas e depois cadastra a 10ª:

```
Digite a sua escolha: 1

Digite o ID da peca: P010
Digite o peso da peca: 98
Digite a cor da peca: verde
Digite o comprimento da peca: 12

Peca P010 Aprovada e adicionada a caixa atual (10/10).
Caixa 1 fechada com 10 pecas!
```

**O que aconteceu**: Ao atingir 10 peças na caixa, ela foi automaticamente fechada e a contagem recomeça para uma nova caixa.

### Exemplo 5: Listando Caixas Fechadas

```
Digite a sua escolha: 4

Caixas fechadas: 1

Caixa 1:
  - ID: P001 | Peso: 100g | Cor: azul | Comprimento: 15cm
  - ID: P003 | Peso: 99g | Cor: verde | Comprimento: 14cm
  - ID: P005 | Peso: 102g | Cor: azul | Comprimento: 11cm
  [... mais 7 peças ...]

Caixa em aberto: 2/10 pecas
```

### Exemplo 6: Gerando Relatório Final

```
Digite a sua escolha: 5

RELATORIO FINAL
Total de pecas cadastradas: 5
Pecas aprovadas: 3
Pecas reprovadas: 2

Motivos de reprovacao:
  Peca P002:
    - peso fora do intervalo (95g a 105g)
    - cor invalida (cores aceitas: azul ou verde)
    - comprimento fora do intervalo (10cm a 20cm)
  Peca P004:
    - peso fora do intervalo (95g a 105g)

Caixas fechadas: 1
Caixa em aberto: 3/10 pecas
```

## 🔧 Opções do Menu Explicadas

| Opção | Descrição |
|-------|-----------|
| **1** | Abre um formulário para cadastrar uma nova peça com ID, peso, cor e comprimento |
| **2** | Exibe todas as peças cadastradas com status (aprovada/reprovada) e motivos |
| **3** | Remove uma peça específica da lista (você escolhe qual pela posição) |
| **4** | Mostra todas as caixas fechadas com 10 peças e a caixa aberta atual |
| **5** | Gera um relatório resumido com estatísticas de aprovação/reprovação |
| **6** | Encerra o programa |

## ⚠️ Observações Importantes

- **Entrada de Dados**: Certifique-se de digitar valores numéricos válidos para peso e comprimento
- **Cores**: Apenas "azul" e "verde" são aceitas (não diferencia maiúsculas/minúsculas)
- **IDs**: Os IDs podem ser qualquer valor (string) que você desejar
- **Dados Temporários**: Os dados são armazenados apenas durante a execução do programa. Ao sair, todos os dados são perdidos.

## 🎓 Conceitos Utilizados

Este projeto utiliza:
- **Listas**: Para armazenar peças e caixas
- **Dicionários**: Para estruturar os dados de cada peça
- **Funções**: Para organizar o código em módulos
- **Loops**: Para o menu interativo
- **Condicionais**: Para validação de dados

## 📝 Licença

Este projeto foi desenvolvido para a UNIFECAF.

---

**Desenvolvido com ❤️ em Python**