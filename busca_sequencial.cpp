#include <iostream>

using namespace std;

int main() {
    int valor = 2;
    int n = 8;
    int array[]= {5,4,10,2,25,13,0,7};
        for (int i=0; i<n; i++){
            if (array[i] == valor)  {
                    cout << "Valor encontrado: " << array[i] << endl;
                    return 0;  
                } 
        }
    cout << "Numero nao encontrado!";
    return -1;
}