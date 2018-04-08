#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<memory.h>

using namespace std;

#define CHAR_NUM 31



int main()
{
    int iCaseNum    = 0;
    int iCase       = 0;

    cin>>iCaseNum;

    for (iCase = 0; iCase < iCaseNum; iCase++)
    {
        int     iShield         = 0;

        char    acStr[CHAR_NUM] = {0};
        int     iLen            = 0;

        int     iDamage         = 0;
        int     iStrength       = 1;

        int     iSwapNum        = 0;
        int     iSwap           = 0;

        cin>>iShield>>acStr;
        iLen = strlen(acStr);

        //cout<<iShield<<" "<<acStr<<" "<<len<<endl;

        cout<<"Case #"<<(iCase+1)<<": ";

        while (1)
        {
            iDamage     = 0;
            iStrength   = 1;

            for (int c = 0; c < iLen; c++)
            {
                if ('C' == acStr[c])
                {
                    iStrength *= 2;
                }
                else if ('S' == acStr[c])
                {
                    iDamage += iStrength;
                }
            }

            //cout<<"Log: "<<iStrength<<" "<<iDamage<<" Log End"<<endl;

            if (iDamage <= iShield)
            {
                break;
            }

            iSwap = 0;
            
            for (int c = iLen - 1; c > 0; c--)
            {
                if ('S' == acStr[c] && 'C' == acStr[c - 1])
                {
                    acStr[c]    = 'C';
                    acStr[c-1]  = 'S';
                    iSwap       = 1;
                    iSwapNum++;
                    break;
                }
            }

            if (0 == iSwap)
            {
                break;
            }
        }

        if (iDamage > iShield)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<iSwapNum<<endl;
        }

    }

    return 0;
}
