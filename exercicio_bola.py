# Cria uma classe que modela uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    #Função para trocar a cor da bola
    def trocaCor(self):
        troca = input(f'Deseja trocar a cor? S/N')
        
        if troca == 'S' or troca == 's':
            nova = input('Digite a nova cor: ')
            self.cor = nova
        else:
            print(f'Cor não alterada.')
    #Função que mostra a cor da bola
    def mostraCor(self):
        print(f'A cor é {self.cor}')

def main():
    bola = Bola('verde', 5, 'Plástico')

    while True:
        bola.mostraCor()
        bola.trocaCor()

        continuar = input('Deseja continuar? S/N')
        if continuar == 'n' or continuar == 'N':
            break

    bola.mostraCor()
    
main()    
