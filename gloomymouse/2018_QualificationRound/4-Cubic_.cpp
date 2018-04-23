#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<iomanip>
#include<memory.h>
#include<math.h>

using namespace std;

#define AREA_SMALL (1.414213)
#define AREA_LARGE (1.732050)


int main()
{
    int iCaseNum    = 0;
    int iCase       = 0;

    cin>>iCaseNum;

    for (iCase = 0; iCase < iCaseNum; iCase++)
    {
        double dArea = 0.0;

        cin>>dArea;

        //cout<<setiosflags(ios::fixed)<<setprecision(8)<<(double)(dArea * dArea)<<" "<<(2-(double)(dArea*dArea))
        //    <<" "<<(double)sqrt((2-(double)(dArea*dArea))/16)<<" "<<(((double)dArea/4)+((double)sqrt(0.125-(double)(dArea*dArea)/16)))<<endl;

        cout<<"Case #"<<(iCase+1)<<":"<<endl;

        if (AREA_SMALL >= dArea)
        {
            cout<<setiosflags(ios::fixed)<<setprecision(8)
                <<((dArea+sqrt(2-(dArea*dArea)))/4)<<" "
                <<((-dArea+sqrt(2-(dArea*dArea)))/4)<<" "
                <<0<<endl;
            cout<<setiosflags(ios::fixed)<<setprecision(8)
                <<((-dArea+sqrt(2-(dArea*dArea)))/4)<<" "
                <<((-dArea-sqrt(2-(dArea*dArea)))/4)<<" "
                <<0<<endl;
            cout<<0<<" "<<0<<" "<<0.5<<endl;
        }
        else
        {
            cout<<setiosflags(ios::fixed)<<setprecision(8)
                <<(sqrt(2.0)/4)<<" "
                <<(sqrt(2.0)/4)*(((dArea*sqrt(2.0))+(sqrt(3-(dArea*dArea)))) / 3)<<" "
                <<-(sqrt(2.0)/4)*((dArea-sqrt(2*(3-dArea*dArea)))/3)<<endl;
            cout<<setiosflags(ios::fixed)<<setprecision(8)
                <<(-(sqrt(2.0)/4))<<" "
                <<(sqrt(2.0)/4)*(((dArea*sqrt(2.0))+(sqrt(3-(dArea*dArea)))) / 3)<<" "
                <<-(sqrt(2.0)/4)*((dArea-sqrt(2*(3-dArea*dArea)))/3)<<endl;
            cout<<0<<" "
                <<(((dArea-sqrt(2*(3-dArea*dArea))) / 3) / 2)<<" "
                <<(((dArea*sqrt(2.0))+(sqrt(3-(dArea*dArea)))) / 3) / 2<<endl;
        }

    }

    return 0;
}
