// author: mofhu
// POJ 1852

# include <cstdio>
# define MAX_N 10000005

int ncase, l, n;
int a[MAX_N] = {};

void solve(){
    int ans = 0;
    int min = 0, max = 0;
    for (int i = 0; i < n; i++){
        // cal min and max time for each ant and update, O(n)
        int t = a[i];
        // printf("%d %d;", t, l-t);
        if (t<=l/2 && t>min) min = t;
        if (t>l/2 && l-t>min) min = l-t;
        if (t<=l/2 && l-t>max) max = l-t;
        if (t>l/2 && t>max) max = t;
    }
    printf("%d %d\n", min, max);
}

int main(){
    scanf("%d", &ncase);
    for (int i=0; i<ncase; i++){
        scanf("%d %d", &l, &n);
        for (int j=0; j<n; j++)
            scanf("%d", &a[j]);
        solve();
    }
}
