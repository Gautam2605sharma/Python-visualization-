#include <iostream>
using namespace std;
int main()
{
    string origin;
    string destination;
    int choice_number;
    string flightlist1[3] = { "flight 200","flight 300","flight 400" };
    string flightlist2[3] = { "flight 10","flight 12","flight 13" };
    int d, m, y;
    cout << "enter the year:";
    cin >> y;
    if (y == 2023 || y == 2024)
    {
        cout << y << endl;
    }
    else
    {
        goto end;
    }
    cout << "enter the month number:";
    cin >> m;
    if (m >= 1 && m <= 12)
    {
        cout << m << endl;
    }
    else
    {
        goto end;
    }
    cout << "enter the day number:";
    cin >> d;
    if (d >= 1 && d <= 31)
    {
        if (m == 2 && d <= 28)
        {
            cout << d << endl;
        }

        else if (m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12)
        {
            cout << d << endl;
        }
        else if (m == 4 || m == 6 || m == 9 || m == 11 && d <= 30)
        {
            cout << d << endl;
        }
        else
        {
            goto end;
        }
    }
    else
    {
        goto end;
    }
    cout << "your selected date is:" << d << "/" << m << "/" << y << endl;
    cout << "enter your origin:";
    cin >> origin;
    cout << "enter your destination:";
    cin >> destination;
    if ((origin == "delhi" && destination == "pune")||(origin=="pune" && destination=="delhi"))
    {
        cout << "choose your flight" << endl;
        for (int i = 0; i < 3; i++)
        {
            cout << i+1<<"."<<flightlist1[i] << endl;
        }
        cin >> choice_number;
        switch (choice_number)
        {
        case 1:
        {
            cout << "congratulations!! your selected flight is " << flightlist1[0] << endl;
            break;
        }

        case 2:
        {
            cout << "congratulations!! your selected flight is " << flightlist1[1] << endl;
            break;
        }
        case 3:
        {
            cout << "congratulations!! your selected flight is " << flightlist1[2] << endl;
            break;
        }
        default:
        {
            cout << "please enter select the number displayed on the left side of the list" << endl;
            break;
        }
            


        }

    }
    else if ((origin == "delhi" && destination == "hyderabad")||(origin=="hyderabad" && destination=="delhi"))
    {
        cout << "choose your flight" << endl;
        for (int i = 0; i < 3; i++)
        {
            cout << i + 1 << "." << flightlist2[i] << endl;
        }
        cin >> choice_number;
        switch (choice_number)
        {
        case 1:
        {
            cout << "congratulations!! your selected flight is " << flightlist2[0] << endl;
            break;
        }

        case 2:
        {
            cout << "congratulations!! your selected flight is " << flightlist2[1] << endl;
            break;
        }
        case 3:
        {
            cout << "congratulations!! your selected flight is " << flightlist2[2] << endl;
            break;
        }
        default:
        {
            cout << "please enter select the number displayed on the left side of the list" << endl;
            break;
        }



        }

    }
    else
    {
        cout << "sorry!! no flights available currently"<<endl;
    }
    return 0;
end:
    cout << "invalid input";
  

}