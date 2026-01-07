#define CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void){
    int n, m;
    int buf[101] = {0, };
    scanf("%d %d", &n, &m);
    for(int i = 1; i <= n; i++) buf[i] = i;
    for(int i = 0; i < m; i++){
        int a, b, temp;
        scanf("%d %d", &a, &b);
        
        for(int j = 0; j < (b - a + 1) / 2; j++){
            temp = buf[a + j];
            buf[a + j] = buf[b - j];
            buf[b - j] = temp;
        }
    }
    for(int i = 1; i <= n; i++) printf("%d ", buf[i]);

    return 0;
}