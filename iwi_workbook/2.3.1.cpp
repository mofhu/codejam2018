// author: mofhu

#include <cstdio>
#define MAX_N 105

int n; 
int w[MAX_N] = {};
int v[MAX_N] = {};
int W;
long value;


void bag (int n0, int w0, long value0){
    // n0 for catch num; w0 for catch weight; value0 for value
    if (n0 == n) {
        // last thing finished, test max value
        printf("value is %ld; max value is %ld.\n", value0, value); 
        if (value0 > value)
            value = value0;
        return;
    }
    else {
        if (w0+w[n0] <= W){
            bag(n0+1, w0+w[n0], value0+v[n0]); // add
        }
        bag(n0+1, w0, value0); // not add
    }
}


void solve (){
    // test code
    for (int i = 0; i<n; i++){
        printf("%d %d\n", w[i], v[i]);
    }
    // test code finished

    // basic 2^n method for 0-1 baggage
    bag(0, 0, 0);

    printf("%ld", value);

    return;
}


int main (){
    scanf("%d", &n);
    for(int i = 0; i<n; i++){
        scanf("%d, %d", &w[i], &v[i]);
    }
    scanf("%d", &W);
    solve();

}