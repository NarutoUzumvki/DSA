class Calculator:

    # Addition

    def sum_of_no(self, n1 , n2):
         
        sum_ = (n1 + n2)
        return sum_

    # Subtraction

    def diff_of_no(self, n1 , n2=9):
      
        diff = (n1-n2)
        return diff

    # Multiplication

    def multiply_no( self , n1 , n2 ):
         
        multiply_ = (n1 * n2)
        return multiply_


    # Division

    def divide ( self , numerator , dinominator ):
         

        if numerator == 0 :
            print(" can't divide 0  : ")
            return

        elif  dinominator == 0 :
            print("Undefined Value : ")

        else:
            quotient= ( numerator / dinominator )
            return quotient


    # Power_func


    def power_of_no( self , n1 , n2 ):
         
        power_ = (n1 ** n2)
        return power_

            
        


if __name__ == "__main__":

    object=Calculator()
    ans_sum = object.sum_of_no(10,5)
    print("the Sum is : ")
    print(ans_sum)

    ans_diff = object.diff_of_no(10)
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




