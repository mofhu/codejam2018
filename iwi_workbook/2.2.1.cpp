// author: mofhu

# include <cstdio>

long c1, c5, c10, c50, c100, c500, A;
long m[6] = {1, 5, 10, 50, 100, 500};
long n[6];

void solve() {
    long ans = 0;
    for (int i=5; i>-1; i--){
        // printf("%ld ",A);
        int tmax = A / m[i];
        if (tmax <= n[i])
            ans += tmax;
        else {
            tmax = n[i];
            ans += tmax;
        }
        A = A-tmax*m[i];
    }
    printf("%ld\n", ans);
}

int main() {
    for (int i=0; i<6; i++)
        scanf("%ld", &n[i]);
    scanf("%ld", &A);
    solve();
}
