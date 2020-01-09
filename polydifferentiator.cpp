/**
 * This program displays a polynomial and then evaluates the polynomial at it's first and second derivative.
 * Course: csc1253 Section 2 <br>
 * Programming Project #: 4 <br>
 * Instructor: Dr. Duncan <br>
 * @author Matthew Jernstrom<br>
 * @since November 14, 2019
 * @version 1
 */
#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <sstream>
#include <new>
using namespace std;
/**
 * @param poly a degree-coefficients array representation of a
 * polynomial.
 * @return a string representation of this polynomial
 */
string polyToString(const double poly[]){
    int degree = poly[0];
    stringstream str;
    
    if (degree == 0)
    {
        str<<poly[1];
    }
    else if (degree == 1)
    {
        if (poly[1] == 1)
        {
            str<<"x";
        }
        else if (poly[1] == -1)
        {
            str<<"-x";
        }
        else
        {
            str<<poly[1]<<"x";
        }
        if (poly[2] != 0)
        {
            if (poly[2] < 0)
                str<< " - "<<-poly[2];
            else
                str<<" + "<<poly[2];
        }
    }
    else
    {
        if (poly[1] == 1)
            str<<"+x^"<<degree;
        else if(poly[1] == -1)
            str<<"-x"<<degree;
        else if (poly[1] < 0)
            str<<poly[1]<<"x^"<<degree;
        else
            str<<poly[1]<<"x^"<<degree;
        int j = degree - 1;
        for(int i = 2; i <= degree - 1; i++)
        {
            if(poly[i] != 0)
            {
                if (poly[i] == 1)
                    str<<" + x^"<<j;
                else if (poly[i] == -1)
                    str<<" - x^"<<j;
                else if (poly[i] < 0)
                    str<<" - "<<-poly[i]<<"x^"<<j;
                else
                    str<<" + "<<poly[i]<<"x^"<<j;
            }
         j--;
        }
        if (poly[degree] != 0) {
            if (poly[degree] == 1)
                str<<" + x";
            else if (poly[degree] == -1)
                str<< " - x";
            else if (poly[degree] < 0)
                str<<" - "<<-poly[degree]<<"x";
            else
                str<<" + "<<poly[degree]<<"x";
        }
        if (poly[degree + 1] != 0) {
            if (poly[degree + 1] < 0)
                str<<" - "<<-poly[degree + 1];
            else
                str<<" + "<<poly[degree + 1];
        }
    }
    return str.str();
}

/**
 * @param poly a degree-coefficients array representation of a
 * polynomial.
 * @param x numeric value at which the polynomial is to be
 * evaluated.
 * @return the value of the polynomial when evaluated with x
 */
double polyEval(const double poly[],double x){
    int degree = poly[0];
    double result = 0;
    int n = 1;
    int i;
    
    for (i = degree; i > 0; i--)
    {
        result += poly[i]*(pow(x,n));
        n++;
    }
    result += poly[degree + 1];

    return result;
}
/**
 * @param poly a degree-coefficients array representation of a
 * polynomial.
 * @return the array representation of the derivative of the
 * specified polynomial.
 */
double* differentiate(const double poly[]){
    int degree = poly[0];
    double *result = new double[degree + 1];
    if (degree > 0)
        *result = degree - 1;
    int n = degree;
    int i;
    for (i = 1; i <= degree; i++)
    {
        result[i] = poly[i] * n;
        n--;
    }
    return result;
    delete[] result;
}

int main(){
    int degree, i;
    cout<<"Enter the degree of the polynomial -> "<<endl;
    cin>>degree;
    cout<<"Enter the coefficients -> "<<endl;
    double* poly = new double [degree + 2];
    poly[0] = degree;
    for(int i = 1; i < degree + 2; i++)
      cin>>poly[i];
    cout<<endl;
    
    cout<<"\n"<<"f(x) = "<<polyToString(poly)<<endl;
    cout<<"Enter a value at which to evaluate the polynomial ->";
    double x;
    cin>>x;
    
    cout<<"f("<<x<<") = "<<setprecision(6)<<polyEval(poly, x)<<endl;
    double* prime = NULL;
    
    prime = differentiate(poly);
    cout<<"\n"<<"f'(x) = "<<setprecision(6)<<polyToString(prime)<<endl;
    cout<<"Enter a value at which to evaluate the 1st derivative -> ";
    double firstDeriv;
    
    cin>>firstDeriv;
    cout<<"f'("<<firstDeriv<<") = "<<setprecision(6)<<polyEval(prime, firstDeriv)<<endl;
    
    double* prime_two = NULL;
    prime_two = differentiate(prime);
    cout<<"\n"<<"f\"\(x) = "<<setprecision(6)<<polyToString(prime_two)<<endl;
    
    double secondDeriv;
    cout<<"Enter a value at which to evaluate the 2nd derivative -> "<<endl;
    cin>>secondDeriv;
    
    cout<<"f\"\("<<secondDeriv<<") = "<<setprecision(6)<<polyEval(prime_two, secondDeriv)<<endl;
    
    delete[] prime;
    delete[] prime_two;
    delete[] poly;
    return 0;
}


