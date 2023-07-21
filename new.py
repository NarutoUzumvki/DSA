def get_gcd(n1,n2):
    list_1 = []
    for i in range(1,n1):
        if  n1%i == 0 :
            list_1.append(i)

    list_2 =[]
    for j in range(1,n2):
        if n2%j == 0:
            list_2.append(j)

    
    common_list = []

    for factors in list_1:
        if factors in list_2:
            common_list.append(factors)

    return common_list 
 
output = "The Greatest Common Divisor for the two numbers n1 and n2 is --> {} ."
gcd = get_gcd(12,18)[-1]
print(output.format(gcd))