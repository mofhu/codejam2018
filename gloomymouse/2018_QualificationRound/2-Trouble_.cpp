#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<memory.h>

using namespace std;

#define MAX_NUM (100000)

int g_iArray[MAX_NUM] = {0};


int main()
{
    int iCaseNum    = 0;
    int iCase       = 0;

    cin>>iCaseNum;

    for (iCase = 0; iCase < iCaseNum; iCase++)
    {
        int iNum = 0;

        int i    = 0;
        int j    = 0;
        int t    = 0;
        int iErr = 0;
    

        cin>>iNum;

        memset(g_iArray, 0, sizeof(int) * MAX_NUM);

        for (i = 0; i < iNum; i++)
        {
            cin>>g_iArray[i];
        }

        for (j = 0; j < iNum - 2; j++)
        {
            for (i = 0; i < iNum - 2 - j; i++)
            {
                if(g_iArray[i] > g_iArray[i + 2])
                {
                    t             = g_iArray[i];
                    g_iArray[i]   = g_iArray[i+2];
                    g_iArray[i+2] = t;
                }
            }
        }

        cout<<"Case #"<<(iCase+1)<<": ";

        for (i = 0; i < iNum - 1; i++)
        {
            if (g_iArray[i] > g_iArray[i+1])
            {
                iErr = 1; 
                break;
            }
        }

        if (0 == iErr)
        {
            cout<<"OK"<<endl;
        }
        else
        {
            cout<<i<<endl;
        }

    }

    return 0;
}
