import random

def sorteia(path):
    with open(path, 'r') as arquivo:
        print random.choice(
            arquivo.readlines()
        )

if __name__ == '__main__':
    sorteia('sorteio.txt')

