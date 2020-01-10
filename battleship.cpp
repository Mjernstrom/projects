//  BattleShip
//  Created by Matthew Jernstrom on 1/8/20.
//  Copyright © 2020 Matthew Jernstrom. All rights reserved.
//
#include <iostream>
using namespace std;


int main() {
    char boardOpp[12][12];
    char boardPlayer[12][12];
    for(int i = 0; i < 12; i++)
        for(int j = 0; j < 12; j++){
            if (i == 0 && j == 0){
                boardOpp[i][j] = ' ';
                boardPlayer[i][j] = ' ';
            }
            boardOpp[i][j] = '?';
            boardPlayer[i][j] = '.';
        }
    cout<<"\n"<<"    Welcome to the Battleship game!"<<endl
    <<"\n"<<"    Each time a ship is hit, a '!' will appear at the chosen spot. If the ship is destroyed, the ship's spots will appear as a '*'"<<endl;
    cout<<"\n"<<"    Your missed shots will not be remembered by the board, pay attention!"<<endl
    <<"\n"<<"    Each spot your ship takes up appears as a '+' "<<endl
    <<"\n"<<"    You have four game pieces (2 frigates and two attack boats): "<<endl<<"\n\n";
    cout<<"    1    2    3    4"<<"\n\n"<<"    +    +    +    +"<<endl<<"    +    +    +    +"<<endl<<"    +    +"<<"\n\n";
    cout<<"\n"<<"Place your pieces by :"<<endl;
    
    /**
    cout<<"\n"<<"CPU's board:"<<endl;
    for(int i = 0; i < 10; i++)
        for(int j = 0; j < 10; j++){
            if (j == 0)
                cout<<"\n\n"<<boardOpp[i][j]<<"   ";
            else
                cout<<boardOpp[i][j]<<"   ";
        }
    cout<<"\n\n";
    **/
    for(int i = 0; i < 12; i++)
        for(int j = 0; j < 12; j++){
            if (j == 0)
                cout<<"\n\n"<<boardPlayer[i][j]<<"   ";
            else
                cout<<boardPlayer[i][j]<<"   ";
        }
    cout<<"\n"<<"Player's board:"<<endl;
    for(int i = 0; i < 12; i++)
        for(int j = 0; j < 12; j++){
            if (j == 0)
                cout<<"\n\n"<<boardPlayer[i][j]<<"   ";
            else
                cout<<boardPlayer[i][j]<<"   ";
        }
    cout<<"\n\n";
    return 0;
}
