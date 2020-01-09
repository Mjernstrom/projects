#include <iostream>
#include <cmath>
#include <string>
using namespace std;
/**
TAKE IT EASY ON ME THIS IS A COMPLETE NOOB ATTEMPT 
Still need to implement proper handles for Player win conditions...
**/
void displayBoard_X(int X_input,char &spot_1,char &spot_2,char &spot_3,char &spot_4,char &spot_5,char &spot_6,char &spot_7,char &spot_8,char &spot_9,char &spot_10, char &spot_11,char &spot_12,char &spot_13,char &spot_14,char &spot_15)
{
  if(X_input == 1)
  {
    if (spot_1 != 'X' || spot_1 != 'O')
      spot_1 = 'X';
  }
  if(X_input == 2)
  {
    if (spot_3 != 'X' || spot_3 != 'O')
      spot_3 = 'X';
  }
  if(X_input == 3)
  {
    if (spot_5 != 'X' || spot_5 != 'O')
      spot_5 = 'X';
  }
  if(X_input == 4)
  {
    if (spot_6 != 'X' || spot_6 != 'O')
      spot_6 = 'X';
  }
  if(X_input == 5)
  {
    if (spot_8 != 'X' || spot_8 != 'O')
      spot_8 = 'X';
  }
  if(X_input == 6)
  {
    if (spot_10 != 'X' || spot_10 != 'O')
      spot_10 = 'X';
  }
  if(X_input == 7)
  {
    if (spot_11 != 'X' || spot_11 != 'O')
      spot_11 = 'X';
  }
  if(X_input == 8)
  {
    if (spot_13 != 'X' || spot_13 != 'O')
      spot_13 = 'X';
  }
  if(X_input == 9)
  {
    if (spot_15 != 'X' || spot_15 != 'O')
      spot_15 = 'X';
  }
}


void displayBoard_O(int O_input,char &spot_1,char &spot_2,char &spot_3,char &spot_4,char &spot_5,char &spot_6,char &spot_7,char &spot_8,char &spot_9,char &spot_10, char &spot_11,char &spot_12,char &spot_13,char &spot_14,char &spot_15)
{
  if(O_input == 1)
  {
    if (spot_1 != 'X' || spot_1 != 'O')
      spot_1 = 'O';
  }
  if(O_input == 2)
  {
    if (spot_3 != 'X' || spot_3 != 'O')
      spot_3 = 'O';
  }
  if(O_input == 3)
  {
    if (spot_5 != 'X' || spot_5 != 'O')
      spot_5 = 'O';
  }
  if(O_input == 4)
  {
    if (spot_6 != 'X' || spot_6 != 'O')
      spot_6 = 'O';
  }
  if(O_input == 5)
  {
    if (spot_8 != 'X' || spot_8 != 'O')
      spot_8 = 'O';
  }
  if(O_input == 6)
  {
    if (spot_10 != 'X' || spot_10 != 'O')
      spot_10 = 'O';
  }
  if(O_input == 7)
  {
    if (spot_11 != 'X' || spot_11 != 'O')
      spot_11 = 'O';
  }
  if(O_input == 8)
  {
    if (spot_13 != 'X' || spot_13 != 'O')
      spot_13 = 'O';
  }
  if(O_input == 9)
  {
    if (spot_15 != 'X' || spot_15 != 'O')
      spot_15 = 'O';
  }
}

bool game_condition(char &spot_1,char &spot_2,char &spot_3,char &spot_4,char &spot_5,char &spot_6,char &spot_7,char &spot_8,char &spot_9,char &spot_10, char &spot_11,char &spot_12,char &spot_13,char &spot_14,char &spot_15, bool game_on)
{
  if (spot_1 == 'X' && spot_3 == 'X' && spot_5 == 'X')
    return false;
  else if (spot_6 == 'X' && spot_8 == 'X' && spot_10 == 'X')
    return false;
  else if (spot_11 == 'X' && spot_13 == 'X' && spot_15 == 'X')
    return false;
  else if (spot_1 == 'X' && spot_6 == 'X' && spot_11 == 'X')
    return false;
  else if (spot_3 == 'X' && spot_8 == 'X' && spot_13 == 'X')
    return false;
  else if (spot_5 == 'X' && spot_10 == 'X' && spot_15 == 'X')
    return false;
  else if (spot_1 == 'X' && spot_8 == 'X' && spot_15 == 'X' )
    return false;
  else if (spot_5 == 'X' && spot_8 == 'X' && spot_11 == 'X')
    return false;
  else if (spot_1 == 'O' && spot_3 == 'O' && spot_5 == 'O')
    return false;
  else if (spot_6 == 'O' && spot_8 == 'O' && spot_10 == 'O')
    return false;
  else if (spot_11 == 'O' && spot_13 == 'O' && spot_15 == 'O')
    return false;
  else if (spot_1 == 'O' && spot_6 == 'O' && spot_11 == 'O')
    return false;
  else if (spot_3 == 'O' && spot_8 == 'O' && spot_13 == 'O')
    return false;
  else if (spot_5 == 'O' && spot_10 == 'O' && spot_15 == 'O')
    return false;
  else if (spot_1 == 'O' && spot_8 == 'O' && spot_15 == 'O' )
    return false;
  else if (spot_5 == 'O' && spot_8 == 'O' && spot_11 == 'O')
    return false;
  else
    return true;
}

int main()
{
    int playerX, playerO;
    char spot_1 ='_';
    char spot_2 = '|';
    char spot_3 ='_';
    char spot_4 = '|';
    char spot_5 ='_';
    char spot_6 ='_';
    char spot_7 ='|';
    char spot_8 ='_';
    char spot_9 ='|';
    char spot_10 ='_';
    char spot_11 ='_';
    char spot_12 ='|';
    char spot_13 ='_';
    char spot_14 ='|';
    char spot_15 ='_';
    bool game_run;

    cout<<spot_1<<spot_2<<spot_3<<spot_4<<spot_5<<endl
    <<spot_6<<spot_7<<spot_8<<spot_9<<spot_10<<endl<<
    spot_11<<spot_12<<spot_13<<spot_14<<spot_15<<endl;

      while (game_condition(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10, spot_11, spot_12, spot_13, spot_14, spot_15, true))
      {
            cout<<"Enter space for Player X"<<endl;
            cin>>playerX;
            displayBoard_X(playerX, spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10, spot_11, spot_12, spot_13, spot_14, spot_15);
            cout<<spot_1<<spot_2<<spot_3<<spot_4<<spot_5<<endl
            <<spot_6<<spot_7<<spot_8<<spot_9<<spot_10<<endl<<
            spot_11<<spot_12<<spot_13<<spot_14<<spot_15<<endl;
            
        if (game_condition(spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10, spot_11, spot_12, spot_13, spot_14, spot_15, true))
        {
            cout<<"Enter space for Player O"<<endl;
            cin>>playerO;
            displayBoard_O(playerO, spot_1, spot_2, spot_3, spot_4, spot_5, spot_6, spot_7, spot_8, spot_9, spot_10, spot_11, spot_12, spot_13, spot_14, spot_15);
            cout<<spot_1<<spot_2<<spot_3<<spot_4<<spot_5<<endl
            <<spot_6<<spot_7<<spot_8<<spot_9<<spot_10<<endl<<
            spot_11<<spot_12<<spot_13<<spot_14<<spot_15<<endl;
        }
        else
          cout<<"Player X wins!"<<endl;
      }
    return 0;
  }
