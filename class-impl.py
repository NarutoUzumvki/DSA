class Calculator:

    # Addition

    def sum_of_no(self, n1 , n2):
        self.n1 = n1
        self.n2 = n2
        sum_ = (n1 + n2)
        return sum_

    # Subtraction

    def diff_of_no(self , n1 , n2):
        self.n1 = n1
        self.n2 = n2
        diff = (n1-n2)
        return diff

    # Multiplication

    def multiply_no( self , n1 , n2 ):
        self.n1 = n1
        self .n2 = n2
        multiply_ = (n1 * n2)
        return multiply_


    # Division

    def divide ( self , n1 , n2 ):
        self.n1 = n1
        self.n2 = n2

        if n1 == 0 :
            print(" cant divide 0  : ")
            return

        elif  n2 == 0 :
            print("Undefined Value : ")

        else:
            divide_= ( n1 / n2 )
            return divide_


    # Power_func


    def power_of_no( self , n1 , n2 ):
        self.n1 = n1
        self.n2 = n2

        power_ = (n1 ** n2)
        return power_

            
        


if __name__== "__main__":

    object=Calculator()
    ans_sum = object.sum_of_no(10,5)
    print("the Sum is : ")
    print(ans_sum)

    ans_diff = object.diff_of_no(10,5)
    print("The Diff. is : ")
    print(ans_diff)

    ans_mul = object.multiply_no(2,5)
    print("The Multiplication is : ")
    print(ans_mul)

    ans_div = object.divide(5,5)
    print("The Division is : ")
    print(ans_div)

    ans_pow = object.power_of_no(5,4)
    print("The Power value is : ")
    print(ans_pow)




