//  animation
//  Created by Matthew Jernstrom on 1/9/20.
//  Copyright © 2020 Matthew Jernstrom. All rights reserved.
#include <iostream>
using namespace std;
string array1[10][10];
int horiz = 0;
int horizTwo = 0;
int vertTwo;
int horizSet = 9;

void converger2(int vertLimit){
    for(int x = 9; x >= horizTwo; x--){
        array1[vertLimit][x - horizTwo] = '.';
        array1[x - horizTwo][vertLimit] = '.';
    }
    if (horizTwo > 0){
        for(int x = 9; x >= horizTwo + 2; x--){
            array1[vertLimit + 1][x - horizTwo + 1] = '|';
            array1[x - horizTwo + 1][vertLimit + 1] = '|';
        }
    }
    horizTwo++;
}
void converger1(int vertLimit){
    for(int x = 0; x <= horizSet - horiz; x++){
        array1[vertLimit][x + horiz] = '.';
        array1[x + horiz][vertLimit] = '.';
    }
    if (horiz > 0){
        for(int x = 0; x <= horizSet - horiz + 2; x++){
            array1[vertLimit - 1][x + horiz - 1] = '|';
            array1[x + horiz - 1][vertLimit - 1] = '|';
        }
    }
    horiz++;
    horizSet--;
}
int main() {
    // Insert symbols into array and output the array
    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            array1[i][j] = '|';
            if(j == 0)
                cout<<"\n"<<"\n"<<array1[i][j]<<"    ";
            else
                cout<<array1[i][j]<<"    ";
        }
    }
    cout<<"\n\n";
    // Run converger functions
    for(int vertLimit = 0; vertLimit < 10; vertLimit++){
        converger1(vertLimit);
        converger2(9 - vertLimit);
        for(int i = 0; i < 10; i++){
            for(int j = 0; j < 10; j++){
                if(j == 0)
                    cout<<"\n"<<"\n"<<array1[i][j]<<"    ";
                else
                    cout<<array1[i][j]<<"    ";
            }
        }
        cout<<"\n\n\n\n";
    }
    return 0;
}
