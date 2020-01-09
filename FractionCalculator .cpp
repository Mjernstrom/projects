/**
 * Describe what this program does: This program uses a modular design using void
 and value-returning functions to evaluate numerical expressions involving
 fractions.
 * @author Matthew Jernstrom
 * @since October 23, 2019
 * File: FractionCalculator.cpp
 * CSC 1253 Project # 3 Section: 001
 * Instructor: Dr. Duncan
 */
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
using namespace std;
/**
 * Gives the greatest common divisor of two integers or returns 0 if the
 * gcd is undefined. Uses the Euclidean GCD algorithm
 * @param a an integer
 * @param b an integer
 * @return the gcd of the specified parameter or 0 if both a and b are 0
 */

int gCD(int a, int b)
{
    int gcd, r;
    a = abs(a);
    b = abs(b);
    if (a == 0 && b == 0)
        gcd = 0;
    else if (a == 0 || b == 0)
        gcd = abs(a + b);
    else
        r = a % b;
    while (r != 0)
    {   a = b;
        b = r;
        r = a % b;
    }
    gcd = b;
    return gcd;
}
/**
 * Computes the sum of two fractions
 * @param n1 the numerator of the augend
 * @param d1 the denominator of the augend
 * @param n2 the numerator of the addend
 * @param d2 the denominator of the addend
 * @param num the numerator of the sum
 * @param den the denominator of the sum
 */
void add(int num1, int den1, int num2, int den2, int &num, int &den)
{
    num = (num1 * den2) + (num2 * den1);
    den = den1 * den2;
}
/**
 * Computes the difference of two fractions
 * @param n1 the numerator of the minuend
 * @param d1 the denominator of the minuend
 * @param n2 the numerator of the subtrahend
 * @param d2 the denominator of the subtrahend
 * @param num the numerator of the difference
 * @param den the denominator of the difference
 */
void sub(int num1,int den1,int num2,int den2,int &num, int &den)
{
    num = (num1 * den2) - (num2 * den1);
    den = den1 * den2;
}
/**
 * Computes the product of two fractions
 * @param n1 the numerator of the multiplier
 * @param d1 the denominator of the multiplier
 * @param n2 the numerator of the multiplicand
 * @param d2 the denominator of the multiplicand
 * @param num the numerator of the product
 * @param den the denominator of the product
 */
void mult(int num1,int den1,int num2,int den2,int &num, int &den)
{
    num = num1 * num2;
    den = den1 * den2;
}
/**
 * Computes the quotient of two fractions, if defined
 * @param n1 the numerator of the dividend
 * @param d1 the denominator of the dividend
 * @param n2 the numerator of the divisor
 * @param d2 the denominator of the divisor
 * @param num the numerator of the quotient
 * @param den the numerator of the quotient
 * or 0 if the quotient is undefinded
 */
void divd(int num1,int den1,int num2,int den2,int &num, int &den)
{
    num = num1 * den2;
    den = num2 * den1;
}
/**
 * Gives the string representation of a fraction
 * @param n the numerator of the fraction
 * @param d the denominator of the fraction
 * @param normalize gives a string represnetation
 * of a fraction in normalized form where the
 * numerator and denominator are relatively prime
 * and n/d when normalized is false.
 * @return n/d when normalized is false; otherwise,
 * 1. d = 0 -> nan
 * 2. n = 0 -> 0
 * 3. d = 1 -> n
 * 4. d = -1 -> -n
 * 5. n and d have the same sign -> |n|/|d|
 * 6. n and d have different signs -> -|n|/|d|
 */
string str(int n, int d,bool normalize)
{
    stringstream answer;
    int divisor;
    if (normalize)
    {
        if (d == 0) return "nan";
        if (n == 0) return "0";
        if (n == d) return "1";
        if (n == -d) return "-1";
        
        divisor = gCD(n,d);
        n = n / divisor;
        d = d / divisor;
    
        if (d == 1)
        {
            answer<<n;
            return answer.str();
        }
        if (d == -1)
        {
            answer<<-n;
            return answer.str();
        }
        if (d < 0)
        {   n*= -1;
            d*= -1;
            answer<<n<<"/"<<d;
            return answer.str();
        }
    }
    answer<<n<<"/"<<d;
    return answer.str();
}
int main()
{
    int num1, den1, num2, den2, num3, den3, num, den, n, d, f1_num, f1_den, f2_num, f2_den, f3_num, f3_den, product_num, product_den;
    bool normalize;
    
    cout<<"Enter the numerator and denominator of f1 > ";
    cin>>num1>>den1;
    cout<<"Enter the numerator and denominator of f2 > ";
    cin>>num2>>den2;
    cout<<"Enter the numerator and denominator of f3 > ";
    cin>>num3>>den3;
    if (den1 == 0|| den2 == 0 || den3 == 0)
        cout<<"ERROR : The denominator of a fraction cannot be 0."<<endl;
    else
    {
        cout<<endl;
        cout<<"f1 = "<<str(num1, den1, false)<<endl;
        cout<<"f2 = "<<str(num2, den2, false)<<endl;
        cout<<"f3 = "<<str(num3, den3, false)<<endl;
        
        add(num1, den1, num2, den2, num, den);
        cout<<"\n"<<"f1 + f2 = "<<str(num, den, true)<<endl;
        sub(num1, den1, num2, den2, num, den);
        cout<<"f1 - f2 = "<<str(num, den, true)<<endl;
        mult(num1, den1, num2, den2, num, den);
        cout<<"f1 x f2 = "<<str(num, den, true)<<endl;
        divd(num1, den1, num2, den2, num, den);
        cout<<"f1 / f2 = "<<str(num, den, true)<<endl;
        add(num2, den2, num3, den3, num, den);
        f2_num = num;
        f2_den = den;
        mult(num1, den1, f2_num, f2_den, num, den);
        product_num = num;
        product_den = den;
        add(num1, den1, num3, den3, num, den);
        f3_num = num;
        f3_den = den;
        divd(product_num, product_den, f3_num, f3_den, num, den);
        cout<<"f1 x ( f2 + f3 ) / ( f1 + f3 ) = "<<str(num, den, true)<<endl;
    }
        return 0;
}





