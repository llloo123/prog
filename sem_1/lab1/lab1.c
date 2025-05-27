#include <stdio.h>

int calc_sum_digits(int num)
{
    int sum_digits = 0;
    while(num != 0) {
        sum_digits += num % 10;
        num = num / 10;
    }   
    return sum_digits;
}

int main()
{
    int a, b;
    printf("Enter a -> ");
    scanf("%d", &a);
    printf("Enter b -> ");
    scanf("%d", &b);

    int sum_digits_a, sum_digits_b;
    sum_digits_a = calc_sum_digits(a);
    sum_digits_b = calc_sum_digits(b);

    if (sum_digits_a > b)
        printf("sum_digits_a = %d\n", sum_digits_a);
    if (sum_digits_a == b)
        printf("sum_digits_b = %d\n", sum_digits_b);
    if (sum_digits_a < b)
       printf("sum_digits_a + b = %d\n", sum_digits_a + b);
    return 0;
}
