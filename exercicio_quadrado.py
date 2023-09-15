# Cria uma classe que modela um quadrado:

# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def tamanhoLado(self):
        troca = input(f'Deseja trocar o valor do lado do quadrado? S/N ')
        
        if troca == 'S' or troca == 's':
            novo_lado = input('Digite a novo valor: ')
            self.lado = novo_lado
        else:
            print(f'Lado não alterado.')
    
    def mostraLado(self):
        print(f'O valor do lado é {self.lado}.')
    
    def calcularArea(self):
        area = (int(self.lado)) * (int(self.lado))
        print(f'A área do quadrado é {area}')


def main():
    quadrado = Quadrado(4)
    quadrado.tamanhoLado()
    quadrado.mostraLado()
    quadrado.calcularArea()

main()
    
        