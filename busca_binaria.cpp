#include <iostream>
using namespace std;

int main(){
    int lista[] = {1,5,6,10,23,55,88,99};
    int n = 8;
    int left = 0;
    int right = n-1;
    
    int buscado = 6;
    
    for(int meio = left+right/2;left <= right; meio=left+right/2){
        if(lista[meio]==buscado){
            cout << "achou" << endl;
            return 0;
        } else if(lista[meio]<buscado){
            left = meio + 1;
        } else {
           right = meio - 1;
        }
    }
    
    
    return 0;
}
