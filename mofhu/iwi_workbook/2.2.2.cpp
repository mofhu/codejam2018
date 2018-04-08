// author: mofhu

# include <cstdio>
# include <queue>
# define MAX_N 100005
using namespace std;

typedef pair<long, int> W; // t = first, n = second (don't need store s)

int n;
long s[MAX_N] = {};
long t[MAX_N] = {};

void solve() {
    queue<W> que;
    // init que;
    que.push(W(-1, 0));
    for (int i=0; i<n; i++){
        // printf("%ld %ld %d\n", s[i], t[i], i); //
        int not_insert = false;
        for (int j=0; j<que.size(); j++){
            W wi = que.front(); que.pop();
            if (wi.first < s[i]){
                wi.first = t[i];
                wi.second++;
                que.push(W(wi.first, wi.second));
            }
            else{
                not_insert = true;
                que.push(wi);
            }
        }
        if (not_insert == false){
            W n_max; // clean queue
            n_max.second = 0;
            for (int j=0; j<que.size(); j++){
                W wi = que.front(); que.pop();
                if (wi.second > n_max.second) {
                    n_max.first = wi.first;
                    n_max.second = wi.second;
                }
            que.push(n_max);
            }
        }
    }
    int ans = 0;
    for (int j=0; j<que.size(); j++){
        W wi = que.front(); que.pop();
        // printf("%ld, %d", wi.first, wi.second);
        if (wi.second > ans)
            ans = wi.second;
    }
    printf("%d\n", ans);
}

int main() {
    scanf("%d", &n);
    for (int i=0; i<n; i++)
        scanf("%ld", &s[i]);
    for (int i=0; i<n; i++)
        scanf("%ld", &t[i]);
    solve();
}
