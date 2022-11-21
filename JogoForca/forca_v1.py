# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.erro = 0
		self.asserts = []
		
		
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter in self.word:
			for i in range(0,len(self.word)):
				if letter == self.word[i]:
					self.asserts.append(i)
		else:
			self.erro +=1
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.erro == (len(board)-1)
	
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		return (len(self.asserts) == len(self.word))

	# Método para não mostrar a letra no boarda
	def hide_word(self):
		for i in range(0,len(self.word)):
			if i in self.asserts:
				print(self.word[i], end="")
			else:
				print("_", end=" ")
		
	# Método para checar o status do game e imprimir o board na tela
	# [j,u,l,i,a]
	def print_game_status(self):
		print(board[self.erro])


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
	with open('palavras.txt', "r") as f:
			bank = f.readlines()
	return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())
	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

	# Verifica o status do jogo
	game.print_game_status()
	game.hide_word()
	while (True):
		letter = input('\n Por favor, digite uma letra: ')
		game.guess(letter)
		game.print_game_status()
		game.hide_word()
		if  game.hangman_over() or game.hangman_won():
			break

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\n\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
