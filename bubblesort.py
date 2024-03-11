import random

#Função Bubble sort
def bubble_sort(array):
    #variável para controle do tamanho da lista
    n = len(array)
    #loop externo para verificar até o penúltimo elemento, pois é com ele que fazemos a última comparação com o último elemento
    for i in range(n-1): 
        for j in range(n-i-1):
            #verficação se um número é maior que o próximo
            if array[j] > array[j+1]:
                #cria uma variavel temporaria
                temp = array[j]
                #muda o números de lugar
                array[j] = array[j+1]
                #coloca o array[j+1] na variavel temporaria para a proxima verificação
                array[j+1] = temp

def main():
    #gera números aleatorios entre 1 e 50
    numeros = random.sample(range(1,50),5)
    lista_teste = numeros
    print(f"\nLISTA ORIGINAL: {lista_teste}\n")
    #chamando a função com a lista de numeros aleatorios 
    bubble_sort(lista_teste)
    print(f"LISTA ORDENADA: {lista_teste}\n")

main()


