/**
 * Describe what this program does: This program uses loops to compute the sum of the proper divisors of an integer and specifically classify whether that integer is abundant, positive, deficient, or almost deficient.
 * @author Matthew Jernstrom
 * @since October 8, 2019
 * File: PerfectChecker.cpp
 * CSC 1253 Project # 2 Section: 001
 * Instructor: Dr. Duncan
 */
#include <iostream>
    using namespace std;
    int main ()
    {
        int i, pos_Num, sum = 1;
        cout << "Enter a positive integer to determine if it is perfect -> ";
        cin >> pos_Num;
        if (pos_Num > 2)
        {
            cout<<"s("<<pos_Num<<") = 1";
            for (i = 2; i <= pos_Num/2; i++)
            {
                if (pos_Num % i == 0)
                {
                    cout<<" + "<<i;
                    sum += i;
                }
            }
            if (sum > 1)
                cout<<" = ";
            if (sum > pos_Num)
            {
                cout<<sum<<" > "<<pos_Num<<endl
                <<pos_Num<<" is an abundant number ."<<endl;
            }
            else if (sum == pos_Num)
            {
                cout<<sum<<endl<<pos_Num<<" is a perfect number ."<<endl;
            }
            else if (sum == pos_Num - 1)
            {
                cout<<sum<<" = "<<pos_Num<<" - 1"<<endl
                <<pos_Num<<" is an almost perfect and deficient number ."<<endl;
            }
            else if (sum < pos_Num && sum != 1)
                
            {   cout<<sum<<" < "<<pos_Num<<endl
                <<pos_Num<<" is a deficient number ."<<endl;
            }
            else
            {
                cout<<" < "<<pos_Num<<endl
                <<pos_Num<<" is a deficient number ."<<endl;
            }
        }
        else if (pos_Num == 1)
        {
            cout<<"s("<<pos_Num<<")"<<" = 0 = 1 - 1"<<endl
            <<pos_Num<<" is an almost perfect and deficient number ."<<endl;
        }
        else if (pos_Num == 2)
        {
            cout<<"s("<<pos_Num<<")"<<" = 1 = 2 - 1"<<endl
            <<pos_Num<<" is an almost perfect and deficient number ."<<endl;
        }
        else
            cout<< "ERROR : The number you enter must be a positive integer ."<<endl;
        return 0;
    }
    
