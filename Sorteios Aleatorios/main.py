# --- Sorteio de Numeros aleatórios com numero de participantes definido pelo usuário. Mais detalhes no arquivo readme.md ---

# --- importação de Elemento randomico com Biblioteca Random ---
import random

# --- variável com a entrada de numeros de participantes do sorteio ---
total_participantes = int (input("Digite o numero de participantes do sorteio: "))


# --- Formula de Calculo ---

sorteado = random.randint(1,total_participantes)


# --- imprimir na tela o numero sorteado ---
print ("\n O numero Sorteado foi: {} ".format (sorteado) )

