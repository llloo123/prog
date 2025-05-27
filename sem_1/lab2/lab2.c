#include <stdio.h>
#include <math.h>
int main(){
    double h, x=0;
    FILE *graph;
    printf("Введите h:");
    scanf("%lf", &h);
    graph = fopen("my_graph.txt", "w");
    while(x<=2 + (h/2)){
        if(x<=1){
            fprintf(graph, "%lf\t%lf\n", x, cos(x+pow(x,3)));
            printf("%lf\t%lf\n", x, cos(x+pow(x,3)));
        }else{
            fprintf(graph, "%lf\t%lf\n", x, exp(pow(-x,2)) -pow(x,2) + 2*x);
            printf("%lf\t%lf\n", x, exp(pow(-x,2)) -pow(x,2) + 2*x);
        }
        x+=h;
    }
    fclose(graph);
    return 0;
}  
