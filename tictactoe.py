import os
from threading import Timer
import msvcrt as m

""" 
Método: clearConsole
Descrição: Limpa o console
"""
def clearConsole():
	os.system('cls' if os.name=='nt' else 'clear')

""" 
Método: inicializarTabuleiro
Descrição: Função que inicializa o tabuleiro, isto é, prepara o tabuleiro para a jogada. Os parâmetros e o retorno devem ser definidos pelo programador.

parâmetro: tabuleiro a ser reiniciado
retorna: tabuleiro reiniciado
 """
def startBoard():
	board = [
		[' ', ' ', ' '],
		[' ', ' ', ' '],
		[' ', ' ', ' ']
	]
	return board

"""
Método: imprimirTabuleiro
Descrição: Função que imprime o tabuleiro de jogo da velha para o usuário. Obviamente, se ele já estiver preenchido com X's e O's, então estes deverão ser impressos. Não há retorno. Os parâmetros devem ser definidos pelo programador 
"""
def printBoard(board):
	for row in board:
		print(' ' + row[0] + ' | ' + row[1] + ' | ' + row[2])
		print('-' * 11)

""" 
Método: imprimeMenuPrincipal
Descrição: Função que imprime menu principal do jogo. Os parâmetros e o retorno devem ser definidos pelo programador.

retorna: o modo escolhido pelo usuário
"""
def printMenu():
	mode = 0
	while not (mode == 1 or mode == 2 or mode == 3):
		print(('-' * 25) + 'JOGO DA VELHA' + ('-' * 25))
		print('Selecione um modo de jogo')
		mode = int(input(
			'1 - Jogador x Jogador\n' +
			'2 - Jogador x CPU (Fácil)\n' +
			'3 - Jogador x CPU (Difícil)\n'
		))
		clearConsole()
	return mode

""" 
Método: leiaCoordenadaLinha
Descrição: Função sem parâmetros lê e devolve para o usuário a coordenada da linha.

retorna: a linha escolhida pelo usuário
"""
def collectRow():
	row = int(input('Linha: '))
	return row - 1

""" 
Método: leiaCoordenadaColuna
Descrição: Função sem parâmetros lê e devolve para o usuário a coordenada da coluna.

retorna: a coluna escolhida pelo usuário
"""
def collectColumn():
	column = int(input('Coluna: '))
	return column - 1

""" 
Método: imprimePontuacao
Descrição: Função que imprime o status do jogo, ou seja, a pontuação de cada jogador na partida Essa função deve ser chamada diversas vezes, sempre que iniciar um novo jogo. Não há retorno. Os parâmetros devem ser definidos pelo programador.
"""
def printScore(score, mode):
  print(
		'Pontuação: \n' +
		f'Jogador 1: {score[0]}\n' +
		f'{"Jogador 2:" if mode == 1 else "CPU:"} {score[1]}\n' +
		'-' * 11
	)
  
""" 
Método: posicaoValida
Descrição: Recebe coordenadas de linha e coluna e verifica se aquela posição é válida (ou seja, se ela é existente no tabuleiro e se aquela posição está vazia). O retorno deve ser definido pelo programador. Sugestão: retornar um valor booleano.

parâmetros: o tabuleiro atual, a linha e a coluna
retorna: verdadeiro caso a jogada seja válida
retorna: falso caso contrário
"""
def checkValidPosition(board, row, column):
	if row in range(3) and column in range(3):
		if board[row][column] != 'X' and board[row][column] != 'O':
			return True
  
	return False

""" 
Método: buildSequences
Descrição: Monta as sequências que serão verificadas para saber se há ou não algum ganhador

parâmetros: tabuleiro a com sequências a serem extraídas
retorna: sequências separadas
"""
def buildSequences(board):
	sequences = []
	for row in board: 
		sequences.append(row)
  
	for row in range(len(board)):
		columns = []
		for column in range(len(board[row])):
			columns.append(board[column][row])
		sequences.append(columns)

	diagonals = []
	for diagonal in range(len(board)):
		diagonals.append(board[diagonal][diagonal])
	sequences.append(diagonals)
  
	row = 0
	column = 2
	diagonals = []
	while row < len(board):
		diagonals.append(board[row][column])
		row += 1
		column -= 1
	sequences.append(diagonals)
	return sequences

""" 
Método: verificaVelha
Descrição: Função que verifica se o jogo encerrou em velha, isto é, empate. Os parâmetros e o retorno devem ser definidos pelo programador.

parâmetro: sequências para verificação
retorna: verdadeiro caso ninguém tenha ganhado
retorna: falso caso contrário
"""
def checkDraw(sequences):
	for sequence in sequences:
		if sequence == ['X', 'X', 'X'] or sequence == ['O', 'O', 'O']:
			return False
	return True
 
""" 
Método: verificaVencedor
Descrição: Função que verifica se houve um vencedor, seja ele o jogador 1, jogador 2 ou máquina. Os parâmetros e o retorno devem ser definidos pelo programador.

parâmetro: sequências para verficação
parâmetro: modo escolhido pelo usuário
retorna: jogador 1 caso este tenha ganhado
retorna: jogador 2 caso este tenha ganhado
retorna: cpu caso este tenha ganhado
"""
def checkWinner(sequences, mode):
	if not checkDraw(sequences):
		for sequence in sequences:
			if sequence == ['X', 'X', 'X']:
				return 'Jogador 1'
			elif sequence == ['O', 'O', 'O']:
				return 'Jogador 2' if mode == 1 else 'CPU'
	return 'Empate'

""" 
Método: modoJogador
Descrição: Função que realiza todas as operações para a opção de usuário-jogador vs. usuário-jogador. Os parâmetros e o retorno devem ser definidos pelo programador
"""
def playerMode(mode):
	while True:
		matches = 0
		turns = 0
		score = [0, 0]
		board = startBoard()
	
		playerWhoStart = 'Jogador 1' if matches % 2 == 0 else 'Jogador 2'
		playerTurn = playerWhoStart
		while not 4 in score:
			clearConsole()
			printScore(score, mode)
			printBoard(board)
			if not 3 in score:
				row = collectRow()
				column = collectColumn()
				clearConsole()
				if playerTurn == 'Jogador 1':
					mark = 'X'
				else:
					mark = 'O'
				if userPlay(row, column, board, mark):
					turns += 1
					playerTurn = 'Jogador 1' if playerTurn == 'Jogador 2' else 'Jogador 2'
					sequences = buildSequences(board)
					winner = checkWinner(sequences, mode)
					if winner == 'Jogador 1':
						score[0] += 1
						
						printBoard(board)
						print(f'{winner} ganhou!')
						print('Pressiona para continuar')
						m.getch()
						board = startBoard()
					elif winner == 'Jogador 2':
						score[1] += 1
						board = startBoard()
					elif turns == 9:
						board = startBoard()
			else:
				print(f'O {winner} ganhou!')
		matches += 1

		while True:
			op = int(input('Deseja jogar novamente no mesmo modo? 1- Sim | 2 - Não\n'))
			if op == 1 or op == 2:
				break
		if op == 2:
			break


""" 
Método: jogar
Descrição: Função que recebe as coordenadas de linha e coluna e preenche exclusivamente o tabuleiro. O atribuição no tabuleiro só pode ser feito por esta função. Ela deverá ser usada pelos jogadores e pelo computador. A função jogada apenas atribui "X" ou "O" no tabuleiro. A validação da jogada (por exemplo, se a coordenada é válida ou não) deve ser feita em outra função. 
"""
def makePlay(row, column, board, mark):
	if checkValidPosition(board, row, column):
		board[row][column] = mark
		return True
	return False
  
""" 
Método: jogadaUsuario
Descrição: Função que recebe as coordenadas do jogador e obrigatoriamente chama a função jogar para inserir no tabuleiro. O retorno deve ser definido pelo programador.
"""
def userPlay(row, column, board, mark):
	return makePlay(row, column, board, mark)