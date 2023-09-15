# Cria uma classe que modela um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;


class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
    
    def tamanhoLado(self):
        troca = input(f'Deseja trocar o valor de algum lado do retangulo? S/N ')
        if troca == 'S' or troca == 's':
            lado_escolhido = input('Qual lado deseja alturar o valor? C/L ')
            if lado_escolhido == 'c' or lado_escolhido == 'C':
                segundo_comprimento = input('Digite o novo valor do comprimento: ')
                self.comprimento = segundo_comprimento
                nova_escolha = input('Deseja alterar a largura? S/N ')
                if nova_escolha == 's' or nova_escolha == 'S':
                    segunda_largura = input('Digite o novo valor da largura: ')
                    self.largura = segunda_largura
            if lado_escolhido == 'l' or lado_escolhido == 'L':
                segunda_largura = input('Digite o novo valor da largura: ')
                self.largura = segunda_largura
            else:
                print('Entrada inválida.')       
        else:
            print(f'Nenhum lado alterado.')
            
    def mostraLado(self):
        print(f'O valor do comprimento é {self.comprimento}.')
        print(f'O valor da largura é {self.largura}.')
    
    def calcularArea(self):
        area = (int(self.comprimento)) * (int(self.largura))
        print(f'A área do retângulo é {area}')
    
    def calcularPerimetro(self):
        perimetro = (int(self.comprimento)) + (int(self.largura))
        print(f'O perímetro do retângulo é {perimetro}')
        
    def quantoPrecisa(self):
        print(f'São necessários {(int(self.comprimento)) * (int(self.largura))} metros quadrados de pisos e {(int(self.comprimento)) + (int(self.largura))} metros de rodapé.')


def main():
    retangulo = Retangulo(int(input('Digite o valor do comprimento: ')), int(input('Digite o valor da largura: ')))
    retangulo.tamanhoLado()
    retangulo.mostraLado()
    retangulo.calcularArea()
    retangulo.calcularPerimetro()
    retangulo.quantoPrecisa()
    
main()
    
    
    
        