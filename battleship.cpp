//  BattleShip
//  Created by Matthew Jernstrom on 1/8/20.
//  Copyright © 2020 Matthew Jernstrom. All rights reserved.
//  Excited about this one; going to implement intelligent AI
//  Planning on allowing bot to remember every other miss made to make it more difficult for the player
//  My plan for the AI is to follow simple battleship logic. If the bot hits one of your ships spots, it turns on what I call "hit mode"
//  The bot stores all memory of turns with missed spots adjacent to a hit spot
//  So the bot will choose to hit another adjacent spot on it's next turn, and not choosing the previously missed spot
//  Once the bot sinks your ship, "hit mode" is turned off. 
#include <iostream>
using namespace std;
string boardOpp[12][12];
string boardPlayer[12][12];

void shipPlacement(){
    string placeInput;
    if(placeInput[0] == 'A' || placeInput[0] == 'a'){
        
    }
}

void displayCpuBoard(){
    cout<<"\n"<<"CPU's board:"<<endl;
    for(int i = 0; i < 12; i++)
        for(int j = 0; j < 12; j++){
            if (j == 0)
                cout<<"\n\n"<<boardOpp[i][j]<<"   ";
            else if (i == 0 && j == 10)
                cout<<boardOpp[i][j]<<"  ";
            else
                cout<<boardOpp[i][j]<<"   ";
        }
}
void displayPlBoard(){
    cout<<"\n"<<"Player's board:"<<endl;
    for(int i = 0; i < 12; i++)
        for(int j = 0; j < 12; j++){
            if (j == 0)
                cout<<"\n\n"<<boardPlayer[i][j]<<"   ";
            else if (i == 0 && j == 10)
                cout<<boardPlayer[i][j]<<"  ";
            else
                cout<<boardPlayer[i][j]<<"   ";
        }
}
void createBoard(){
    char incrementChar = 65;
    
    for(int i = 0; i < 12; i++)
        for(int j = 0; j < 12; j++){
            if (i == 0 && j == 0){
                boardOpp[i][j] = " ";
                boardPlayer[i][j] = " ";
            }
            else if (i < 12 && j == 0){
                boardOpp[i][j] = incrementChar;
                boardPlayer[i][j] = incrementChar;
                incrementChar++;
            }
            else if (i == 0 && j < 12){
                
                boardOpp[i][j] = to_string(j);
                boardPlayer[i][j] = to_string(j);
            }
            else {
                boardOpp[i][j] = "?";
                boardPlayer[i][j] = ".";
            }
        }
}

int main() {
    // Display game instructions
    cout<<"\n"<<"    Welcome to the Battleship game!"<<endl
    <<"\n"<<"    Each time a ship is hit, a '!' will appear at the chosen spot. If the ship is destroyed, the ship's spots will appear as a '*'"<<endl;
    cout<<"\n"<<"    Your missed shots will not be remembered by the board, pay attention!"<<endl
    <<"\n"<<"    Each spot your ship takes up appears as a '+' "<<endl
    <<"\n"<<"    You have four game pieces (2 frigates and two attack boats): "<<endl<<"\n\n";
    cout<<"    1    2    3    4"<<"\n\n"<<"    +    +    +    +"<<endl<<"    +    +    +    +"<<endl<<"    +    +"<<"\n\n";
    cout<<"\n"<<"Place your pieces by entering the Letter followed by the number of the spot such as 'A5'. No diagnal placement! :"<<endl;
    createBoard();
    displayPlBoard();

    cout<<"\n\n";
    return 0;
}
