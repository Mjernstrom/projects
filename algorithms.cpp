//  Created by Matthew Jernstrom on 1/5/20.
//  Copyright © 2020 Matthew Jernstrom. All rights reserved.
//  Pretty much just hashing out some algorithms on here and using output to describe the process... 
//  Might refer to this file to paste in some more complex logic into other projects...
#include <iostream>
using namespace std;

void sorterTwoDimensional(int rows, int columns, int array[]) {
    int array2D[rows][columns];
    int temp;
    for (int i = 0; i < rows; i++)
        for (int j = 0; j < columns; j++)
            array2D[i][j] = array[(i * columns) + j];
    int x, y;
    for (x = 0; x < rows; x++)
        for (y = 0; y < columns; y++)
            for (int z = 0; z < rows; z++){
                for (int v = 0; v < columns; v++)
                    if (array2D[x][y] < array2D[z][v]){
                        temp = array2D[x][y];
                        array2D[x][y] = array2D[z][v];
                        array2D[z][v] = temp;
                    }
            }
    cout<<"Sorted 2D array --> "<<endl;
    cout<<"\n";
    for (x = 0; x < rows; x++){
        for (int y = 0; y < columns; y++){
            if (y == columns - 1)
                cout<<array2D[x][y]<<endl;
            else
                cout<<array2D[x][y]<<", ";
        }
    }
    cout<<"\n";
}
void sorter(int array[], int size) {
    int tmp;
    for (int i = 0; i < size; i++)
        for (int j = i + 1; j <= size - 1 - i; j++){
            if (array[i] > array[j]) {
                tmp = array[i];
                array[i] = array[j];
                array[j] = tmp;
            }
        }
    cout<<"\n"<<"The sorted array is --> {";
    for (int i = 0; i < size; i++){
        if (i == size - 1)
            cout<<array[i]<<"}"<<endl;
        else
            cout<<array[i]<<", ";
    }
}
int main(){    
    int arraySize;
    cout<<"Enter size of array --> "<<endl;
    cin>>arraySize;
    int array[arraySize];
    cout<<"Enter values for array -->"<<endl;
    for (int i = 0; i < arraySize; i++) {
        cin>>array[i];
    }
    sorter(array, arraySize);
    int rows, columns;
    cout<<"Enter number of rows in the 2D array --> "<<endl;
    cin>>rows;
    cout<<"Enter number of columns in the 2D array --> "<<endl;
    cin>>columns;
    int array2D[rows][columns];
    int i,x;
    for (i = 0; i < rows; i++){
        cout<<"Enter values into row "<<i<<" --> "<<endl;
        for (int j = 0; j < columns; j++)
            cin>>array2D[i][j];
    }
    cout<<"2D array as entered -- > "<<endl;
    cout<<"\n";
    for (x = 0; x < rows; x++){
        for (int j = 0; j < columns; j++){
            if (j == columns - 1)
                cout<<array2D[x][j]<<endl;
            else
                cout<<array2D[x][j]<<", ";
        }
    }
    cout<<"\n";
    int size = columns * rows;
    int arrayReference[size];
    int inc = 0;
    for (int x = 0; x < rows; x++){
        for (int y = 0; y < columns; y++){
            arrayReference[(columns * inc) + y] = array2D[x][y];
        }
        inc++;
    }
    for (i = 0; i < size; i++)
        cout<<arrayReference[i]<<" ";
    sorterTwoDimensional(rows, columns, arrayReference);
    return 0;
}
