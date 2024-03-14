#include <iostream>
using namespace std;

//INSERTION SORT
int main() {
    int lista[] = {3,2,5,4};
    int tamanho_lista = 4;
    
    for(int i = 0; i < tamanho_lista; i++){
        int menor_indice = i; //indice do menor elemento 
        for(int j = i; j < tamanho_lista; j++){
            if (lista[j] < lista[menor_indice]) {
                menor_indice = j; //atualizando o indice
                }
        }
        if(menor_indice != i){ // condição para trocar valores
            int temp = lista[i];
            lista[i] = lista[menor_indice];
            lista[menor_indice] = temp;
        }
    }
    //exibição da lista completa
    for (int i = 0; i < tamanho_lista; i++) {
        cout << lista[i] << " ";
    }
    cout << endl;
    return 0;
}
