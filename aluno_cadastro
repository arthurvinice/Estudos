class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.__matricula = matricula
        self.__notas = []
    
    #ENCAPSULANDO A MATRÍCULA    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,matricula):
        return print(f'Não é possível alterar a matrícula.')
    
    #ADICIONAR NOTA À LISTA DE NOTAS
    def adc_nota(self, nota):
        if nota < 0:
            print('Erro: nota menor que zero.')
        else:
            self.__notas.append(nota)
    
    #CALCULAR A MÉDIA DE NOTAS        
    def calc_media(self):
        media = (sum(self.__notas)/len(self.__notas))
        if media >= 60:
            print(f'Parabens, voce foi aprovado. Média: {media:.0f}.')
        elif 30 < media < 60:
            print(f'Ficou de recuperação. Média:: {media:.0f}.')
        else:
            print(f'Reprovado. Média:: {media:.0f}.')
     
    #MOSTRA AS INFORMAÇÕES DO ALUNO   
    def relatorio(self):
        return print(f'Nome:{self.nome}.\nIdade:{self.idade}.\nMatrícula:{self.__matricula}.')
    
    
def main():
    #CRIANDO O OBJETO
    aluno1 = Aluno('José Maria', '19', '2023999')
    #ADICIONANDO NOTAS
    aluno1.adc_nota(60)
    aluno1.adc_nota(70)
    aluno1.adc_nota(80)
    aluno1.adc_nota(90)
    #CALCULANDO A MÉDIA
    aluno1.calc_media()
    aluno1.relatorio()
    #TESTE DE ALTERAÇÃO DE MATRÍCULA
    aluno1.matricula = 2023666
    
main()
