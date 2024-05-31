import sqlite3 as conector #importando sqlite3 e chamando ele de conector
import os #biblioteca para poder limpar os dados na tela do terminal

def criar_tabela(): #Função para criar a tabela Aluno
  try: #tenta executar o bloco abaixo:
    conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
    cursor = conexao.cursor() #cria um cursor para executar comandos sql

    comando = '''CREATE TABLE IF NOT EXISTS Aluno (
                      matricula INTEGER NOT NULL,
                      nome TEXT NOT NULL,
                      nascimento DATE NOT NULL,
                      PRIMARY KEY (matricula)
                      );'''
    cursor.execute(comando) #executa o comando

    comando = '''CREATE TABLE IF NOT EXISTS Nota (
                      id INTEGER NOT NULL,
                      matricula INTEGER NOT NULL,
                      disciplina TEXT NOT NULL,
                      nota REAL NOT NULL,
                      PRIMARY KEY (id),
                      FOREIGN KEY (matricula) REFERENCES Aluno (matricula)
                      );'''
    cursor.execute(comando) #executa o comando

    conexao.commit() #confirma a criação das tabelas
    print("Tabelas criadas com sucesso!")
    voltarMenu() #chama a função voltarMenu()

  except conector.DatabaseError as erro: #caso ocorra um erro de conexão ou tabela já existe, será exibido o print abaixo
    print("Erro ao criar tabela", erro)

  finally: #executa o bloco abaixo independente do erro
    if conexao: #verifica se a conexão foi criada
      cursor.close() #fecha o cursor
      conexao.close() #fecha a conexão

def inserirAluno(): #Função para adicionar Aluno na tabela
  try: #tenta executar o bloco abaixo
    conexao = conector.connect("cadastro_alunos.db")
    cursor = conexao.cursor()

    matricula = int(input("Digite a matrícula do aluno: "))
    nome = input("Digite o nome do aluno: ")
    nascimento = input("Digite a data de nascimento do aluno (dd/mm/aaaa): ")

    comando = f"INSERT INTO Aluno VALUES ({matricula}, '{nome}', '{nascimento}')"
    cursor.execute(comando)
    conexao.commit()
    print("Aluno inserido com sucesso!")

    while True:
      disciplina = input("Digite o nome da disciplina: ")
      while True:
        nota = float(input(f"Digite a nota para a disciplina {disciplina}: "))
        comando = f"INSERT INTO Nota (matricula, disciplina, nota) VALUES ({matricula}, '{disciplina}', {nota})"
        cursor.execute(comando)
        conexao.commit()
        print("Nota inserida com sucesso!")
        continuar = input("Deseja inserir outra nota para esta disciplina? (sim/nao): ")
        if continuar.lower() != 'sim':
          break
      continuar_disciplina = input("Deseja inserir outra disciplina? (sim/nao): ")
      if continuar_disciplina.lower() != 'sim':
        break

  except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, tabela já existente, conflito de dados e entre outros, mostra o print abaixo:
    print("Erro ao inserir aluno e/ou nota.\nErro:", erro)
  finally: #executa o bloco independente do erro
    if conexao: #verifica se a conexão foi criada
      cursor.close() #fecha o cursor
      conexao.close() #fecha a conexão
      voltarMenu() #chama a função voltarMenu()

def excluirAluno(): #Função que exclui aluno(s) da tabela
  try: #tenta executar o bloco abaixo
    conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
    cursor = conexao.cursor() #cria um cursor para executar comandos sql

    matricula = int(input("Digite a matricula do aluno que deseja excluir: ")) #o aluno será excluído com base na matrícula dele.
    cursor.execute(f"SELECT nome FROM Aluno WHERE matricula = {matricula}")
    aluno = cursor.fetchone() #armazena o nome do aluno na variável aluno
    if aluno: #verifica se o aluno existe
      nomeAluno = aluno[0]
      print("Aluno(a) '", nomeAluno, " 'excluído com sucesso!")
      comando1 = f"DELETE FROM Nota WHERE matricula = {matricula}" #comando para excluir a nota do aluno.
      cursor.execute(comando1) # Executa o comando

      comando2 = f"DELETE FROM Aluno WHERE matricula = {matricula}" #comando para excluir o aluno.
      cursor.execute(comando2) # Executa o comando
      conexao.commit() # Confirma a exclusão dos dados

  except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
    print("Erro ao excluir aluno", erro)
  finally: #executa o bloco independente do erro
    if conexao: #verifica se a conexão foi criada
      cursor.close() #fecha o cursor
      conexao.close() #fecha a conexão
      voltarMenu() #chama a função voltarMenu()

def modificarAluno(): #Função que modifica dados do aluno na tabela
  try: #tenta executar o bloco abaixo
    conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
    cursor = conexao.cursor() #cria um cursor para executar comandos sql
    matricula = int(input("Digite a matricula do aluno que deseja modificar: ")) #o aluno será encontrado no banco de dados com base na matrícula dele.
    print("\nO que deseja modificar? \n1: Nome\n2: Nascimento\n3: Notas e Disciplinas\n4: Matrícula") #menu de escolha
    escolha = int(input("Escolha uma opção: ")) # variável que vai receber a decisão do usuário.
    match escolha:
      case 1: #se o usuario digitar '1', vai executar os comandos abaixo:
        nome = input("Digite o novo nome do aluno: ")
        comando = f"UPDATE Aluno SET nome = '{nome}' WHERE matricula = {matricula}" #comando para modificar o nome do aluno.
        cursor.execute(comando) #executa o comando
        conexao.commit() #confirma a modificação dos dados
        print("Aluno modificado com sucesso!")
        voltarMenu()

      case 2: #se o usuario digitar '2', vai executar os comandos abaixo:
        nascimento = input("Digite a nova data de nascimento do aluno (dd/mm/aaaa): ")
        comando = f"UPDATE Aluno SET nascimento = '{nascimento}' WHERE matricula = {matricula}" #comando para modificar a data de nascimento do aluno.
        cursor.execute(comando) #executa o comando
        conexao.commit() #confirma a modificação dos dados
        print("Aluno modificado com sucesso!")
        voltarMenu()

      case 3: #se o usuario digitar '3', vai executar os comandos abaixo:
        while True:
          print("\nOpções de modificação de disciplinas e notas:")
          print("1: Alterar nome da disciplina")
          print("2: Alterar nota da disciplina")
          print("3: Voltar")
          escolha_disciplina = int(input("Escolha uma opção: "))

          if escolha_disciplina == 1: #se o usuario digitar '1', vai executar os comandos abaixo:
            disciplina_atual = input("Digite o nome da disciplina atual: ")
            nova_disciplina = input("Digite o novo nome da disciplina: ")
            comando = f"UPDATE Nota SET disciplina = '{nova_disciplina}' WHERE matricula = {matricula} AND disciplina = '{disciplina_atual}'"
            cursor.execute(comando) #executa o comando
            conexao.commit() #confirma a modificação dos dados
            print("Nome da disciplina modificado com sucesso!")

          elif escolha_disciplina == 2:
            disciplina = input("Digite o nome da disciplina: ")
            comando = f"SELECT id, nota FROM Nota WHERE matricula = {matricula} AND disciplina = '{disciplina}'"
            cursor.execute(comando)
            notas = cursor.fetchall()
            if notas:
              print("Notas atuais:")
              for nota in notas:
                print(f"ID: {nota[0]}, Nota: {nota[1]}")
        
            while True:
              print("\nOpções:")
              print("1: Modificar uma nota")
              print("2: Remover uma nota")
              print("3: Voltar")
              escolha_modificar = int(input("Escolha uma opção: "))
            
              if escolha_modificar == 1:
                nota_id = int(input("Digite o ID da nota que deseja modificar: "))
                nova_nota = float(input("Digite a nova nota: "))
                comando = f"UPDATE Nota SET nota = {nova_nota} WHERE id = {nota_id}"
                cursor.execute(comando)
                conexao.commit()
                print("Nota da disciplina modificada com sucesso!")

              elif escolha_modificar == 2:
                nota_id = int(input("Digite o ID da nota que deseja remover: "))
                comando = f"DELETE FROM Nota WHERE id = {nota_id}"
                cursor.execute(comando)
                conexao.commit()
                print("Nota da disciplina removida com sucesso!")

              elif escolha_modificar == 3:
                break

              else:
                print("Opção inválida. Tente novamente.")
            else:
              print("Nenhuma nota encontrada para essa disciplina.")

          elif escolha_disciplina == 3: #se o usuario digitar '3', vai voltar ao menu() do programa.
            break

          else: #se o usuario digitar uma opção inválida, irá mostrar na tela 'opção inválida' e vai voltar ao menu() do programa.
            print("Opção inválida. Tente novamente.")
            voltarMenu() #chama a função voltarMenu()

      case 4: #se o usuario digitar '4', vai executar os comandos abaixo:
        NovaMatricula = int(input("Digite a nova matricula do aluno: "))
        comando = f"UPDATE Aluno SET matricula = {NovaMatricula} WHERE matricula = {matricula}" #comando para modificar a matricula do aluno.
        cursor.execute(comando) #executa o comando
        conexao.commit() #confirma a modificação dos dados
        print("Aluno modificado com sucesso!")
        voltarMenu()

    if(escolha <= 0 or escolha >= 5): #se a escolha for menor ou igual a zero ou maior ou igual a 5, irá mostrar na tela 'opção inválida' e vai voltar ao menu() do programa.
      print("Opção inválida.")
      voltarMenu() #chama a função voltarMenu()

  except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
    print("Erro ao modificar aluno", erro)
  finally: #executa o bloco independente do erro
    if conexao: #verifica se a conexão foi criada
      cursor.close() #fecha o cursor
      conexao.close() #fecha a conexão
      voltarMenu() #chama a função voltarMenu()

def consultarAluno(): #Função que consulta aluno na tabela
    try:
        conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
        cursor = conexao.cursor() #cria um cursor para executar comandos sql

        matricula = int(input("Digite a matrícula do aluno que deseja consultar: "))

        comando = f"SELECT Aluno.matricula, Aluno.nome, Aluno.nascimento, Nota.disciplina, Nota.nota" \
                  f" FROM Aluno JOIN Nota ON Aluno.matricula = Nota.matricula" \
                  f" WHERE Aluno.matricula = {matricula}"
        cursor.execute(comando) #executa o comando
        dados = cursor.fetchall() #armazena os dados na variável dados

        if dados: #verifica se foram encontrados registros
            print("Dados do Aluno:")
            print(f"\nMatrícula: {dados[0][0]}")
            print(f"Nome: {dados[0][1]}")
            print(f"Nascimento: {dados[0][2]}")
            disciplinas = {}
            for aluno in dados:
                disciplina = aluno[3]
                nota = aluno[4]
                if disciplina not in disciplinas:
                    disciplinas[disciplina] = []
                disciplinas[disciplina].append(nota)
            for disciplina, notas in disciplinas.items():
                notas_formatadas = ', '.join(map(str, notas))
                print(f"Notas da disciplina {disciplina}: {notas_formatadas}")
        else: #se não foram encontrados registros, irá mostrar na tela 'Aluno não encontrado'
            print("Aluno não encontrado.")

    except conector.DatabaseError as erro: # Se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
        print("Erro ao consultar aluno", erro)
    finally: # Executa o bloco independente do erro
        if conexao: # Verifica se a conexão foi criada
            cursor.close() # Fecha o cursor
            conexao.close() # Fecha a conexão
            voltarMenu() # Chama a função voltarMenu()

def listarTodosAlunos(): #função que mostra todos os alunos registrado no banco de dados
    try: #tenta executar o bloco abaixo
        conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
        cursor = conexao.cursor() #cria um cursor para executar comandos sql

        cursor.execute("SELECT Aluno.matricula, Aluno.nome, Aluno.nascimento, Nota.disciplina, Nota.nota" \
                       " FROM Aluno JOIN Nota ON Aluno.matricula = Nota.matricula")
        dados = cursor.fetchall() #armazena os dados na variável dados

        if dados: #verifica se foram encontrados registros
            print("\nLista de Todos Alunos:")
            alunos = {}
            for aluno in dados:
                matricula = aluno[0]
                if matricula not in alunos:
                    alunos[matricula] = {
                        "nome": aluno[1],
                        "nascimento": aluno[2],
                        "disciplinas": {}
                    }
                disciplina = aluno[3]
                nota = aluno[4]
                if disciplina not in alunos[matricula]["disciplinas"]:
                    alunos[matricula]["disciplinas"][disciplina] = []
                alunos[matricula]["disciplinas"][disciplina].append(nota)
            for matricula, info in alunos.items():
                print(f"\nMatrícula: {matricula}")
                print(f"Nome: {info['nome']}")
                print(f"Nascimento: {info['nascimento']}")
                for disciplina, notas in info["disciplinas"].items():
                    notas_formatadas = ', '.join(map(str, notas))
                    print(f"Notas da disciplina {disciplina}: {notas_formatadas}")
        else: #se não foram encontrados registros, irá mostrar na tela 'Nenhum aluno encontrado'
            print("Nenhum aluno encontrado.")

    except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
        print("Erro ao mostrar todos alunos", erro)
    finally: #executa o bloco independente do erro
        if conexao: #verifica se a conexão foi criada
            cursor.close() #fecha o cursor
            conexao.close() #fecha a conexão
            voltarMenu() #chama a função voltarMenu()

def mostrarNotas(): #Função que mostra todas as notas dos alunos
  try: #tenta executar o bloco abaixo
        conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
        cursor = conexao.cursor() #cria um cursor para executar comandos sql

        cursor.execute("SELECT Aluno.matricula, Aluno.nome, Aluno.nascimento, Nota.disciplina, Nota.nota" \
                       " FROM Aluno JOIN Nota ON Aluno.matricula = Nota.matricula")
        dados = cursor.fetchall() #armazena os dados na variável dados

        if dados: #verifica se foram encontrados registros
            print("\nLista de Notas dos Alunos:")
            alunos = {}
            for aluno in dados:
                matricula = aluno[0]
                if matricula not in alunos:
                    alunos[matricula] = {
                        "nome": aluno[1],
                        "nascimento": aluno[2],
                        "disciplinas": {}
                    }
                disciplina = aluno[3]
                nota = aluno[4]
                if disciplina not in alunos[matricula]["disciplinas"]:
                    alunos[matricula]["disciplinas"][disciplina] = []
                alunos[matricula]["disciplinas"][disciplina].append(nota)
            for matricula, info in alunos.items():
                print(f"\nNome: {info['nome']}")
                for disciplina, notas in info["disciplinas"].items():
                    notas_formatadas = ', '.join(map(str, notas))
                    print(f"Notas da disciplina {disciplina}: {notas_formatadas}")
        else: #se não foram encontrados registros, irá mostrar na tela 'Nenhum aluno encontrado'
            print("Nenhum aluno encontrado.")

  except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
        print("Erro ao mostrar todos alunos", erro)
  finally: #executa o bloco independente do erro
        if conexao: #verifica se a conexão foi criada
            cursor.close() #fecha o cursor
            conexao.close() #fecha a conexão
            voltarMenu() #chama a função voltarMenu()

def voltarMenu(): #Função para voltar ao menu principal
  continuar = input("\nDeseja voltar para o menu inicial?\nDigite 'sim' para continuar.\n") #pergunta ao usuário se ele quer continuar no programa ou se deseja sair
  if continuar == 'sim': #se a resposta for 'sim', limpa a tela do console e chama a função main()
    os.system('cls')
    main()
  else: #se a resposta for diferente de 'sim', finaliza o programa.
    print("Programa finalizado.")
    exit() #finaliza o programa

def main(): #Função principal
  print('-'*40)
  print("Cadastro de Notas de Alunos")
  print('-'*40)
  print("1. Criar a Tabela Aluno e Nota")
  print("2. Inserir Aluno")
  print("3. Excluir Aluno")
  print("4. Modificar Aluno")
  print("5. Consultar Aluno")
  print("6. Listar Todos os Alunos")
  print("7: Listar Todas as notas dos Alunos")
  print("8. Sair")
  escolha = int(input("Escolha uma opção: ")) #variável que vai receber a escolha desejada pelo usuário

  match escolha: #estrutura de condição match case
    case 1: #caso a escolha seja '1', redireciona para a função "criar_tabela()"
      criar_tabela()
    case 2: #caso a escolha seja '2', redireciona para a função "inserirAluno()"
      inserirAluno()
    case 3: #caso a escolha seja '3', redireciona para a função "excluirAluno()"
      excluirAluno()
    case 4: #caso a escolha seja '4', redireciona para a função "modificarAluno()"
      modificarAluno()
    case 5: #caso a escolha seja '5', redireciona para a função "consultarAluno()"
      consultarAluno()
    case 6: #caso a escolha seja '6', redireciona para a função "listarTodosAlunos()"
      listarTodosAlunos()
    case 7: #caso a escolha seja '7', redireciona para a função "mostrarNotas()"
      mostrarNotas()
    case 8: #caso a escolha seja '8', finaliza o programa
      print("Fechando programa")
      exit() #finaliza o programa
  if(escolha <= 0 or escolha > 8): #se a escolha for menor ou igual a zero ou maior que 7, irá mostrar na tela 'opção inválida' e vai voltar ao menu() do programa.
    print("Opção inválida.")
    exit() #finaliza o programa

main() #início do código, chamando a função main()