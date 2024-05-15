import sqlite3 as conector #importando sqlite3 e chamando ele de conector
import os #biblioteca para poder limpar os dados na tela do terminal

def criar_tabela(): #Função para criar a tabela Aluno
  try: #tenta executar o bloco abaixo:
    conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
    cursor = conexao.cursor() #cria um cursor para executar comandos sql

    comando = '''CREATE TABLE Aluno (
                  matricula INTEGER NOT NULL,
                  nome TEXT NOT NULL,
                  nascimento DATE NOT NULL,
                  nota INTEGER NOT NULL,
                  PRIMARY KEY (matricula)
                  );''' # no comando é criado a tabela aluno com as variaveis matricula (chave primária), nome, nascimento e nota.
    cursor.execute(comando) #executa o comando
    conexao.commit() #confirma a criação da tabela

  except conector.DatabaseError as erro: #caso ocorra um erro de conexão ou tabela já existe, será exibido o print abaixo
    print("Erro ao criar tabela", erro)

  finally: #executa o bloco abaixo independente do erro
    if conexao: #verifica se a conexão foi criada
      cursor.close() #fecha o cursor
      conexao.close() #fecha a conexão

      continuar = input("\nDeseja voltar para o menu inicial?\nDigite 'sim' para continuar.\n") #pergunta ao usuário se ele quer continuar no programa ou se deseja sair
      if(continuar == 'sim'): #se a resposta for 'sim', limpa a tela do console e chama a função main()
        os.system('cls')
        main()
      elif(continuar!='sim'): #se a resposta for diferente de 'sim', finaliza o programa.
        print("Programa finalizado.")
        exit() #finaliza o programa

def inserirAluno(): #Função para adicionar Aluno na tabela
  try: #tenta executar o bloco abaixo
    conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
    cursor = conexao.cursor() #cria um cursor para executar comandos sql

    matricula = int(input("Digite a matricula do aluno: "))
    nome = input("Digite o nome do aluno: ")
    nascimento = input("Digite a data de nascimento do aluno (dd/mm/aaaa):") #'nascimento' é string devido a data ser do formato dd/mm/aaaa.
    nota = float(input("Digite a nota do aluno: "))
    comando = f"INSERT INTO Aluno VALUES ({matricula}, '{nome}', '{nascimento}', {nota})" #comando para inserir os dados na tabela
    cursor.execute(comando) #executa o comando
    conexao.commit() #confirma a inserção dos dados
    print("Aluno inserido com sucesso!")

  except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
    print("Erro ao inserir aluno", erro)
  finally: #executa o bloco independente do erro
    if conexao: #verifica se a conexão foi criada
      cursor.close() #fecha o cursor
      conexao.close() #fecha a conexão

      continuar = input("\nDeseja voltar para o menu inicial?\nDigite 'sim' para continuar.\n") #pergunta ao usuário se ele quer continuar no programa ou se deseja sair
      if(continuar == 'sim'): #se a resposta for 'sim', limpa a tela do console e chama a função main()
        os.system('cls')
        main()
      elif(continuar!='sim'): #se a resposta for diferente de 'sim', finaliza o programa.
        print("Programa finalizado.")
        exit() #finaliza o programa

def excluirAluno(): #Função que exclui aluno(s) da tabela
  try: #tenta executar o bloco abaixo
    conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
    cursor = conexao.cursor() #cria um cursor para executar comandos sql

    matricula = int(input("Digite a matricula do aluno que deseja excluir: ")) #o aluno será excluído com base na matrícula dele.
    comando = f"DELETE FROM Aluno WHERE matricula = {matricula}" #comando para excluir o aluno.
    cursor.execute(comando) #executa o comando
    conexao.commit() #confirma a exclusão dos dados
    print("Aluno excluído com sucesso!")

  except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
    print("Erro ao excluir aluno", erro)
  finally: #executa o bloco independente do erro
    if conexao: #verifica se a conexão foi criada
      cursor.close() #fecha o cursor
      conexao.close() #fecha a conexão

      continuar = input("\nDeseja voltar para o menu inicial?\nDigite 'sim' para continuar.\n") #pergunta ao usuário se ele quer continuar no programa ou se deseja sair
      if(continuar == 'sim'): #se a resposta for 'sim', limpa a tela do console e chama a função main()
        os.system('cls')
        main()
      elif(continuar!='sim'): #se a resposta for diferente de 'sim', finaliza o programa.
        print("Programa finalizado.")
        exit() #finaliza o programa

def modificarAluno(): #Função que modifica dados do aluno na tabela
  try: #tenta executar o bloco abaixo
    conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
    cursor = conexao.cursor() #cria um cursor para executar comandos sql
    matricula = int(input("Digite a matricula do aluno que deseja modificar: ")) #o aluno será encontrado no banco de dados com base na matrícula dele.
    print("\nO que deseja modificar? \n1: Nome\n2: Nascimento\n3: Nota\n4: Matrícula") #menu de escolha
    escolha = int(input("Escolha uma opção: ")) # variável que vai receber a decisão do usuário.
    match escolha:
      case 1: #se o usuario digitar '1', vai executar os comandos abaixo:
        nome = input("Digite o novo nome do aluno: ")
        comando = f"UPDATE Aluno SET nome = '{nome}' WHERE matricula = {matricula}" #comando para modificar o nome do aluno.
        cursor.execute(comando) #executa o comando
        conexao.commit() #confirma a modificação dos dados
        print("Aluno modificado com sucesso!")

      case 2: #se o usuario digitar '2', vai executar os comandos abaixo:
        nascimento = input("Digite a nova data de nascimento do aluno (dd/mm/aaaa): ")
        comando = f"UPDATE Aluno SET nascimento = '{nascimento}' WHERE matricula = {matricula}" #comando para modificar a data de nascimento do aluno.
        cursor.execute(comando) #executa o comando
        conexao.commit() #confirma a modificação dos dados
        print("Aluno modificado com sucesso!")

      case 3: #se o usuario digitar '3', vai executar os comandos abaixo:
        nota = int(input("Digite a nova nota do aluno: "))
        comando = f"UPDATE Aluno SET nota = {nota} WHERE matricula = {matricula}" #comando para modificar a nota do aluno.
        cursor.execute(comando)  #executa o comando
        conexao.commit() #confirma a modificação dos dados
        print("Aluno modificado com sucesso!")

      case 4: #se o usuario digitar '4', vai executar os comandos abaixo:
        NovaMatricula = int(input("Digite a nova matricula do aluno: "))
        comando = f"UPDATE Aluno SET matricula = {NovaMatricula} WHERE matricula = {matricula}" #comando para modificar a matricula do aluno.
        cursor.execute(comando) #executa o comando
        conexao.commit() #confirma a modificação dos dados
        print("Aluno modificado com sucesso!")

    if(escolha <= 0 or escolha >= 5): #se a escolha for menor ou igual a zero ou maior ou igual a 4, irá mostrar na tela 'opção inválida' e vai voltar ao menu() do programa.
      print("Opção inválida.")
      continuar = input("\nDeseja voltar para o menu inicial?\nDigite 'sim' para continuar.\n") #pergunta ao usuário se ele quer continuar no programa ou se deseja sair
      if(continuar == 'sim'): #se a resposta for 'sim', limpa a tela do console e chama a função main()
        os.system('cls')
        main()
      elif(continuar!='sim'): #se a resposta for diferente de 'sim', finaliza o programa.
        print("Programa finalizado.")
        exit() #finaliza o programa

  except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
    print("Erro ao modificar aluno", erro)
  finally: #executa o bloco independente do erro
    if conexao: #verifica se a conexão foi criada
      cursor.close() #fecha o cursor
      conexao.close() #fecha a conexão

      continuar = input("\nDeseja voltar para o menu inicial?\nDigite 'sim' para continuar.\n") #pergunta ao usuário se ele quer continuar no programa ou se deseja sair
      if(continuar == 'sim'): #se a resposta for 'sim', limpa a tela do console e chama a função main()
        os.system('cls')
        main()
      elif(continuar!='sim'): #se a resposta for diferente de 'sim', finaliza o programa.
        print("Programa finalizado.")
        exit() #finaliza o programa

def consultarAluno(): #Função consulta dados de aluno
    try: #tenta executar o bloco abaixo
        conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
        cursor = conexao.cursor() #cria um cursor para executar comandos sql

        matricula = int(input("Digite a matricula do aluno que deseja consultar: "))
        comando = f"SELECT * FROM Aluno WHERE matricula = {matricula}" #comando para consultar o aluno com base na matrícula dele.
        cursor.execute(comando) #executa o comando
        dados = cursor.fetchall() #armazena os dados na variável dados

        if dados: #verifica se foi encontrados registros
            print("Dados do Aluno:")
            for aluno in dados: #Mostra a matricula, nome, nascimento e nota do aluno
                print(f"\nMatrícula: {aluno[0]}")
                print(f"Nome: {aluno[1]}")
                print(f"Nascimento: {aluno[2]}")
                print(f"Nota: {aluno[3]}")
        else: #caso não ache informações do aluno-alvo
            print("Aluno não encontrado.")

    except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
        print("Erro ao consultar aluno", erro)
    finally: #executa o bloco independente do erro
        if conexao: #verifica se a conexão foi criada
            cursor.close() #fecha o cursor
            conexao.close() #fecha a conexão

            continuar = input("\nDeseja voltar para o menu inicial?\nDigite 'sim' para continuar.\n") #pergunta ao usuário se ele quer continuar no programa ou se deseja sair
            if continuar == 'sim': #se a resposta for 'sim', limpa a tela do console e chama a função main()
                os.system('cls')
                main()
            else: #se a resposta for diferente de 'sim', finaliza o programa.
                print("Programa finalizado.")
                exit() #finaliza o programa

def listarTodosAlunos(): #função que mostra todos os alunos registrado no banco de dados
    try: #tenta executar o bloco abaixo
        conexao = conector.connect("cadastro_alunos.db") #conecta ao banco de dados "cadastro_alunos"
        cursor = conexao.cursor() #cria um cursor para executar comandos sql

        cursor.execute("SELECT matricula, nome, nascimento, nota FROM Aluno") #comando para mostrar todos os alunos
        dados = cursor.fetchall() #armazena os dados na variável dados

        if dados: #verifica se foi encontrados registros
            print("\nLista de Todos Alunos:")
            for aluno in dados: #mostra os dados de todos os alunos presentes no banco de dados
                print(f"\nMatrícula: {aluno[0]}")
                print(f"Nome: {aluno[1]}")
                print(f"Nascimento: {aluno[2]}")
                print(f"Nota: {aluno[3]}")
        else: #Se não tiver aluno no banco de dados, mostra o print abaixo:
            print("Não há alunos cadastrados.")

    except conector.DatabaseError as erro: #se ocorrer um erro de conexão ao banco de dados, mostra o print abaixo:
        print("Erro ao mostrar todos alunos", erro)
    finally: #executa o bloco independente do erro
        if conexao: #verifica se a conexão foi criada
            cursor.close() #fecha o cursor
            conexao.close() #fecha a conexão

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
  print("1. Criar a Tabela Aluno")
  print("2. Inserir Aluno")
  print("3. Excluir Aluno")
  print("4. Modificar Aluno")
  print("5. Consultar Aluno")
  print("6. Listar Todos os Alunos")
  print("7. Sair")
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
    case 7: #caso a escolha seja '7', finaliza o programa
      print("Fechando programa")
      exit() #finaliza o programa
  if(escolha <= 0 or escolha > 7): #se a escolha for menor ou igual a zero ou maior que 7, irá mostrar na tela 'opção inválida' e vai voltar ao menu() do programa.
    print("Opção inválida.")
    exit() #finaliza o programa

main() #início do código, chamando a função main()