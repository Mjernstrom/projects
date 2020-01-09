/**
 * This is an interactive program that determines the day of the week and the month of a date on the Gregorian calendar.
 * Course: CSC 1253 Section: 001
 * Programming Project #: 1
 * Instructor: Dr. Duncan
 * @author Matthew Jernstrom
 * @since September 30, 2019
 */
#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    int month,day,year;
    cout<<"Enter these values for month , day and year -> ";
    cin>>month>>day>>year;

    int m;
    bool valid, leap = year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
    if (month < 1 || month > 12 || day < 1 || day > 31 || year < 1583)
        valid = false;
    else if (day == 31 && (month == 4 || month == 6 || month == 9 || month == 11))
        valid = false;
    else if (month == 2)
    {
        if (leap)
        {
            if (day > 29)
                valid= false;
            else
                valid = true;
        }
        else if (day > 28)
            valid = false;

        else
            valid = true;
    }
    else
        valid = true;

    if (valid)
    {
        if (month == 1)
        {
            if (leap)
                m = 6;
            else
                m = 0;
        }
        else if (month == 2)
        {
            if (leap)
                m = 2;
            else
                m = 3;
        }
        else if (month == 3 || month == 11)
            m = 3;
        else if (month == 4 || month == 7)
            m = 6;
        else if (month == 5)
            m = 1;
        else if (month == 6)
            m = 4;
        else if (month == 8)
            m = 8;
        else if (month == 9 || month == 12)
            m = 5;
        else
            m = 0;
    }

    int century = year / 100;
    int v = year % 100;
    int u = 2 * (3 - (century % 4));
    int w = v / 4;
    int y = u + v + w + m + day;
    int dayOfWeek = y % 7;
    string dayName;
    string monthName;

    if (valid)
    {
        if (dayOfWeek == 0)
            dayName = "Sunday";
        else if (dayOfWeek == 1)
            dayName = "Monday";
        else if (dayOfWeek == 2)
            dayName = "Tuesday";
        else if (dayOfWeek == 3)
            dayName = "Wednesday";
        else if (dayOfWeek == 4)
            dayName = "Thursday";
        else if (dayOfWeek == 5)
            dayName = "Friday";
        else
            dayName = "Saturday";

        if (month == 1)
            monthName = "January";
        else if (month == 2)
            monthName = "February";
        else if (month == 3)
            monthName = "March";
        else if (month == 4)
            monthName = "April";
        else if (month == 5)
            monthName = "May";
        else if (month == 6)
            monthName = "June";
        else if (month == 7)
            monthName = "July";
        else if (month == 8)
            monthName = "August";
        else if (month == 9)
            monthName = "September";
        else if (month == 10)
            monthName = "October";
        else if (month == 11)
            monthName = "November";
        else
            monthName = "December";
    }
    if (valid)
    {
        if (leap)
            cout<<dayName<<", "<<monthName<<" "<<setw(2)<<setfill('0')<<day<<", "<<year
            <<" occurred in a leap year."<<endl;
        else
            cout<<dayName<<", "<<monthName<<" "<<setw(2)<<setfill('0')<<day<<", "<<year
            <<" occurred in a non-leap year."<<endl;
    }
    else
        cout<<month<<"/"<<day<<"/"<<year<<" is not a valid date."<<endl;
    return 0;
}
