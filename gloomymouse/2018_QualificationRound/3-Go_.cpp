#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
#include<memory.h>

using namespace std;

#define DEPOLY_TIMES (1000)
#define LENGTH       (1000)
#define AREA_SMALL   (20)
#define AREA_LARGE   (200)
#define RET_OK       (0)
#define RET_ERR      (-1)

int g_iOrchard[LENGTH][LENGTH] = {0};

int main()
{
    int iCaseNum    = 0;
    int iCase       = 0;

    cin>>iCaseNum;

    for (iCase = 0; iCase < iCaseNum; iCase++)
    {
        int iMinArea    = 0;

        int iDepRow     = 0;   // 2-999
        int iDepCol     = 0;
        int iRealRow    = 0;
        int iRealCol    = 0;
        int iMaxRow     = 0;

        memset(g_iOrchard, 0, (sizeof(int) * LENGTH * LENGTH));

        cin>>iMinArea;

        if (AREA_SMALL == iMinArea)
        {
            iMaxRow = 6;
        }
        else
        {
            iMaxRow = 66;
        }

        iDepRow = 2;
        iDepCol = 2;

        for (int t = 0; t < DEPOLY_TIMES; t++)
        {
            int i = 0;
            int j = 0;
            int iHasUnprep = 0;
            int iRowMove   = 0;


            cout<<iDepRow<<" "<<iDepCol<<endl;

            cin>>iRealRow>>iRealCol;

            if (RET_OK == iRealRow && RET_OK == iRealCol) 
            {
                break;
            }

            if (RET_ERR == iRealRow && RET_ERR == iRealCol)
            {
                return 0;
            }

            g_iOrchard[iRealRow-1][iRealCol-1] = 1;

            iHasUnprep = 0;

            for (i = iDepRow - 1; i <= iDepRow + 1; i++)
            {
                for (j = iDepCol - 1; j <= iDepCol + 1; j++)
                {
                    if (0 == g_iOrchard[i-1][j-1])
                    {
                        iHasUnprep = 1;
                        break;
                    }
                }

                if (1 == iHasUnprep)
                {
                    break;
                }
            }

            if (0 == iHasUnprep)
            {
                iDepRow += 3;
            }
            else
            {
                if (iDepRow == iMaxRow)
                {
                    continue;
                }
                iRowMove = 2 - ((iDepRow + 1 - i));
                iDepRow += iRowMove;
            }

        }


    }

    return 0;
}
