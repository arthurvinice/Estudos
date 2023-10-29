#Este problema foi gerado pelo ChatGPT. Ele solicitou o desenvolvendo de 
#um sistema de gerenciamento de uma instituição educacional que lida com cursos e alunos. 
#Crie uma classe abstrata chamada Pessoa que representará uma pessoa genérica. Essa classe deve ter atributos para o nome, idade e endereço. Ela também deve conter métodos abstratos para obter_informacoes() e cumprimentar(). 
#O método obter_informacoes() deve ser responsável por imprimir o nome, idade e endereço da pessoa, enquanto o método cumprimentar() deve imprimir uma saudação genérica.
#Crie uma classe Aluno que herda da classe Pessoa. A classe Aluno deve incluir atributos adicionais, como o número de registro do aluno e uma lista de cursos em que está matriculado. 
#Ela também deve implementar o método obter_informacoes() para imprimir informações específicas do aluno, incluindo o número de registro e os cursos matriculados. O método cumprimentar() deve imprimir uma saudação específica para alunos.
#Crie uma classe Curso que represente um curso na instituição. Ela deve ter atributos como nome do curso, código do curso e uma lista de alunos matriculados. 
#A classe Curso também deve incluir um método adicionar_aluno() para adicionar um aluno ao curso e um método listar_alunos() para listar os alunos matriculados no curso.


class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade= idade
        self.endereco = endereco
    
    def get_infos(self):
        return print(f"\nNOME: {self.nome}.\nIDADE: {self.idade}.\nENDEREÇO: {self.endereco}.")
    
    def cumprimentar(self):
        return print("Olá! Tudo bem?")
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, endereco, registro):
        super().__init__(nome, idade, endereco)
        self.__registro = registro
        self.lista_cursos = []

    #FUNÇÃO PARA ADICIONAR CURSO À LISTA DE CURSOS DO ALUNO
    def adc_curso(self, curso):
        if isinstance(curso, Curso):
            self.lista_cursos.append(curso)
    
    def get_infos(self):
        super().get_infos() 
        print(f"MATRÍCULA: {self.__registro}.\nCURSOS:", end="")
        for curso in self.lista_cursos:
            print(f" -{curso}")
    
    def cumprimentar(self):
        super().cumprimentar()
        print(f'Tenho que estudar para a prova!')
        
class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.lista_alunos = []

    #ADICIONA ALUNOS À LISTA DO CURSO E ADICIONA O CURSO À LISTA DE CURSOS DO ALUNO    
    def adc_aluno(self, nome):
        if isinstance(nome, Aluno):
            self.lista_alunos.append(nome)
            nome.adc_curso(self)
            
    def listar_alunos(self):
        print(f'\nLista de alunos {self.nome}:')
        for aluno in self.lista_alunos:
            aluno.get_infos()
    
    def __str__(self):
        return f"{self.nome} ({self.codigo})"


#TESTANDO O CÓDIGO
def main():
    #CRIANDO CURSOS
    curso1 = Curso('POO', '01')
    curso2 = Curso('PABD', '02')
    #CRIANDO ALUNOS
    aluno1 = Aluno('Lucas José',23,'Avenida JK',2023123)
    aluno2 = Aluno('José Lucas',22,'Avenida JK',2023456)
    #ADICIONANDO ALUNOS AOS CURSOS
    curso1.adc_aluno(aluno1)
    curso2.adc_aluno(aluno1)
    curso2.adc_aluno(aluno2)
    #LISTANDO ALUNOS DOS CURSOS
    curso1.listar_alunos()
    curso2.listar_alunos()
    
main()
