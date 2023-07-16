def greatest_common_divisor ( m, n):
    list_m = []
    for i in range (1,m+1):
        if m%i == 0 :
            list_m.append(i)

    list_n = []
    for j in range (1,m+1):
        if m % j == 0 :
            list_n.append(j)

    list_common_factors= []
    for factors in list_m:
        if factors in list_n:
            list_common_factors.append(factors)

    return list_common_factors


def main():
    sol = greatest_common_divisor ( 8, 12)[-1]
    print("The Greatest Common Divisor is : " )
    print(sol)

main()