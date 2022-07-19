// author: mofhu

# include <cstdio>
# define MAX_N 105

int n;
int a[MAX_N] = {};

void solve(){
    int ans = 0;
    for (int i = n-1; i > 1; i--){
        int j = i-1;
        int k = i-2;
        if (a[j] + a[k] > a[i]){
            ans = a[i] + a[j] + a[k];
            break;
        }
    }
    printf("%d\n", ans);
}

int main(){
    scanf("%d", &n);
    for (int i=0; i<n; i++)
        scanf("%d", &a[i]);
    solve();
}
