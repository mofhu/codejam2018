// author: mofhu
// POJ 2386

# include <cstdio>
# define MAX_N 1005

int n, m;
char a[MAX_N][MAX_N];

void flow(int i, int j) {
    if (a[i][j] == 'W') {
        a[i][j] = '.';
        int d[3] = {-1,0,1};
        for (int x=0; x<3; x++)
            // have to iterate all in this case!!!
            // 本题有可能出现绕大圈的情况, 因此必须全部循环, 不能只循环右和下3共四个方向, 经验是不如全部循环反而好写, 且可防此类 WA bug.
            // note: just iterate all as a safer code style in contest.
            for (int y=0; y<3; y++){
                int ix = i + d[x];
                int jy = j + d[y];
                if (0<=ix<n-1 && 0<=jy<m-1) flow(ix,jy);
            }
    }
    return;
}

void solve() {
    int num_pond = 0;
    // for (int i=0; i<n; i++){
    //    for (int j=0; j<m; j++)
    //        printf("%c", a[i][j]);
    //    printf("\n");
    //}
    for (int i=0; i<n; i++)
        for (int j=0; j<m; j++){
            if (a[i][j] == 'W'){
                // printf("%d %d;", i,j);
                flow(i,j);
                num_pond++;
            }
        }
    printf("%d\n", num_pond);
}

int main() {
    scanf("%d %d\n", &n, &m);
    for (int i=0; i<n; i++)
        scanf("%s", a[i]);
    solve();
}
