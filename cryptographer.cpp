//  cryptographer
//  Created by Matthew Jernstrom on 1/8/20.
//  Copyright © 2020 Matthew Jernstrom. All rights reserved.
//  More complicated encryptions to come! (I promise)
//  This one might be turned into some kind of a game...perhaps a mystery game or a hacking game...
#include <iostream>
#include <new>
using namespace std;

void decrypterTierTwo(string message){ 
    
}

void encrypterTierTwo(string message, int array[]){
    cout<<"\n"<<"Intercepting packet . . . "<<"\n"<<
    "You have 2 minutes to decrypt and edit: {";
    
}

void interception(int arrayEncrypted[], int size){
    
}

void decrypterTierOne(int arrayDecrypt[], int size){
    char charArray[size];
    cout<<"\n"<<"You have recieved a message from a user, decrypting message { ";
    for(int i = 0; i < size; i++)
        cout<<arrayDecrypt[i]<<" ";
    cout<<" }"<<endl;
    cout<<"\n"<<"Reversing order decryption . . . { ";
    for(int i = 0; i < size/2; i++){
        int tmpFirst = arrayDecrypt[i];
        int tmpSecond = arrayDecrypt[size - i - 1];
        arrayDecrypt[i] = tmpSecond;
        arrayDecrypt[size - i - 1] = tmpFirst;
    }
    for(int i = 0; i < size; i++)
        cout<<arrayDecrypt[i]<<" ";
    cout<<" }";
    cout<<"\n"<<"Converting message to string . . ."<<endl;
    for(int i = 0; i < size; i++){
        charArray[i] = arrayDecrypt[i];
    }
    string finalMessage;
    for(int i = 0; i < size; i++){
        finalMessage.insert(i, 1, charArray[i]);
    }
    cout<<"\n"<<"Your message is '"<<finalMessage<<"'"<<endl;
}

void encrypterTierOne(string message){
    int size = message.size();
    int *arrayNum = new int[size];
    char array[size];
    
    for(int i = 0; i < size; i++)
        array[i] = message.at(i);
    cout<<"\n"<<"Converting string to characters . . . "<<"\n"<<"{ ";
    for (int i = 0; i < size; i++)
        cout<<array[i]<<" ";
    cout<<" }"<<endl;
    for(int i = 0; i < size; i++)
        arrayNum[i] = array[int(i)];
    cout<<"\n"<<"Converting characters to integers . . . "<<"\n"<<"{ ";
    for(int i = 0; i < size; i++)
        cout<<arrayNum[i]<<" ";
    cout<<" }"<<endl;
    for(int i = 0; i < size/2; i++){
        int tmpFirst = arrayNum[i];
        int tmpSecond = arrayNum[size - i - 1];
        arrayNum[i] = tmpSecond;
        arrayNum[size - i - 1] = tmpFirst;
    }
    
    cout<<"\n"<<"Re-arranging integers . . . "<<"\n"<<"{ ";
    for(int i = 0; i < size; i++)
        cout<<arrayNum[i]<<" ";
    cout<<" }"<<endl;
    cout<<"\n"<<"Sending encrypted message . . . "<<endl;
    interception(arrayNum, size);
    decrypterTierOne(arrayNum, size);
}

int main() {
    string message;
    int secLevel;
    cout<<"Compose new message in one string --> "<<endl;
    cin>>message;
    cout<<"\n"<<"Enter security level: 1 - 3 --> "<<endl;
    cin>>secLevel;
    cout<<"\n"<<"Sending message '"<<message<<"' to the encryptor . . . "<<endl;
    if (secLevel == 1)
        encrypterTierOne(message);
    if (secLevel == 2)
        encrypterTierTwo(message);
    return 0;
}

