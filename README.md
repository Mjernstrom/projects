/**
 * Differentiates a polynomial using classes.
 * Course: csc1253 Section x <br>
 * Programming Project #: 5 <br>
 * Instructor: Dr. Duncan <br>
 * @author Matthew Jernstrom <br>
 * @since November 27, 2019
 * @version 2
 */
 #include <cstdlib>
 #include <cmath>
 #include <sstream>
 #include <iostream>

 using namespace std;

 class Polynomial
 {
 private:
     double *poly;

 public:

     Polynomial()
     {
         poly = new double[2];
         poly[0] = 0;
         poly[1] = 0;
     }
     /**
      * @param degCoeffs an array containing the deg of the polynomial
      * as its first element, followed by its coefficients in
      * order of descending powers.
      */
     Polynomial(const double degCoeffs[]){
         int degree = degCoeffs[0];
         const int size = degree + 2;
         poly = new double[degree + 2];
         poly[0] = degree;
         int i;
         for (i = 1; i< size; i++){
             poly[i] = degCoeffs[i];

         }

     }

     ~Polynomial(){
         delete[]poly;
     }

     /**
      * @param x numeric value at which the polynomial is to be
      * evaluated.
      * @return the value of the polynomial when evaluated with x
      */
     double eval(double x) const
     {
         if (poly[0] != 0){
             int degree = poly[0];
             int i;
             double sum = poly[1] * x + poly[2];
             for(i = 3; i <= degree + 1; i++){
                 sum = sum * x + poly[i];
             }
             return sum;
         }
         else
             return poly[1];
     }
     /**
      * </pre>
      * @return a string representation of this polynomial
      */
     string str() const{
         stringstream sout;
         int degree = poly[0];
         if (degree == 0)
             sout<<poly[1];
         else if (degree == 1){
             if(poly[1] == 1)
                 sout<<"x";
             else if (poly[1] == -1)
                 sout<<"-x";
             else
                 sout<<poly[1]<<"x";
         }
         if(degree > 1){
             if (poly[1] == 1)
                 sout<<"x^"<<degree;
             if(poly[1] == -1)
                 sout<<"-"<<"x^"<<degree;
             if(poly[1] > 0 && poly[1] != 1)
                 sout<<poly[1]<<"x^"<<degree;
             if(poly[1] < 0 && poly[1] != -1 )
                 sout<<poly[1]<<"x^"<<degree;
         }
         if (degree == 1){
             if (poly[2] != 0 && (poly[2] > 1 || poly[2] < 1)){
                 if (poly[2] < 0)
                     sout<<" - "<<-poly[2];
                 if (poly[2] > 0)
                     sout<<" + "<<poly[2];
             }
             else if (poly[2] == -1)
                 sout<<" - 1";
             else if (poly[2] == 1)
                 sout<<" + 1";

         }
         int i;
         for (i = 2; i <= degree - 1; i++){
             if (poly[i] != 0){
                 if (poly[i] == 1)
                     sout<<" + "<< "x^"<<degree - i + 1;
                 if (poly[i] == -1)
                     sout<<" - "<<"x^"<<degree - i + 1;
                 if (poly[i] > 0 && poly[i] != 1)
                     sout<<" + "<<poly[i]<<"x^"<<degree - i + 1;
                 if (poly[i] < 0 && poly[i] != -1)
                     sout<<" - "<<-poly[i]<<"x^"<<degree - i + 1;
             }

         }
         if (poly[0] > 1){
             if (poly[degree] == 1)
                 sout<<" + "<<"x";
             if (poly[degree] == -1)
                 sout<<" - "<<"x";
             if (poly[degree] > 0 && poly[degree] != 1)
                 sout<<" + "<<poly[degree]<<"x";
             if (poly[degree] < 0 && poly[degree] != -1)
                 sout<<" - "<<-poly[degree]<<"x";
         }
         if (poly[0] > 1){
             if(poly[degree+1] > 0)
                 sout<<" + "<<poly[degree+1];
             if(poly[degree+1] < 0)
                 sout<<" - "<<-poly[degree+1];
         }

         return sout.str();
     }

     bool equals(const Polynomial& other) const{

         int i;
         int x = poly[0];
         int y = other.poly[0];
         if (x==y){
             for ( i = 0; i<= x; i++){
                 if (poly[i] != other.poly[i])
                     return false;
             }
         }
         else if (x != y)
             return false;

         return true;

     }


     Polynomial differentiate() const{

         if (poly[0] != 0){
             int degree = poly[0];
             double* polyprime = new double[degree + 1];
             int degDeriv = degree - 1;
             polyprime[0] = degDeriv;

             for(int i = 1; i <= degDeriv + 1; i++){
                 double coef = poly[i];
                 int coef_degree = (degree-i+1);
                 polyprime[i] = coef * coef_degree;
             }
             return Polynomial(polyprime);
         }
         else if (poly[0] == 0){
             return Polynomial();

         }
         return 0;
     }
 };


 int main() {
     int deg;
     double a, b, c;
     cout<<"Enter the degree of the polynomial -> ";
     cin>>deg;
     cout<<"Enter the coefficients -> ";

     const int SIZE = deg + 2;
     double* polynomialarray= new double[SIZE];
     polynomialarray[0] = deg;

     int i;
     for( i = 1; i < SIZE ; i++)
         cin >> polynomialarray[i];
     cout<<endl;

     Polynomial f(polynomialarray);
     delete[]polynomialarray;
     cout<<"f(x) = "<<f.str()<<endl;
     cout<<"Enter a value at which to evaluate this polynomial -> ";
     cin>>a;
     cout<<"f("<<a<<") = "<<f.eval(a)<<"\r\n\r\n";


     Polynomial dP = f.differentiate();
     cout<<"f'(x) = "<<dP.str()<<endl;
     cout<<"Enter a value at which to evaluate the 1st Derivative -> ";
     cin>>b;
     cout<<"f'("<<b<<") = "<<dP.eval(b)<<"\r\n\r\n";

     Polynomial deriv2 = dP.differentiate();
     cout<<"f\"(x) = "<<deriv2.str()<<endl;
     cout<<"Enter a value at which to evaluate the 2nd Derivative -> ";
     cin>>c;
     cout<<"f\"("<<c<<") = "<<deriv2.eval(c)<<"\r\n\r\n";

     int degree2;
     cout<<"Enter the degree of the second polynomial -> ";
     cin>>degree2;
     cout<<"Enter the coefficients -> ";

     const int size = degree2 + 2;
     double* array2= new double[size];
     array2[0] = degree2;

     int j;
     for( j = 1; j < size ; j++)
         cin >> array2[j];
     cout<<endl;

     Polynomial second(array2);
     cout<<"g(x) = "<<second.str()<<endl;

     if (dP.equals(array2)){
         cout<<"g(x) = f'(x)";
     }
     else
         cout<<"g(x) <> f'(x)";
     cout<<endl;

     return 0;
 }
