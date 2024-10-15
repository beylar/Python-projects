import math

# function to estimate_Pi with initial values of the parameters of num_terms and precision as integers and None return value
def estimate_Pi(num_terms: int, precision: int) -> None:
    # checking if the arguments passed in the function are integers 
    if not isinstance(num_terms, int) or not isinstance(precision, int):
        print("TypeError: both arguments must be integers.")
        return
    
    print(f'\nTerm Value of the term')
    
    numerator = 1
    denominator = 1
    sum = 1
    product = 1
    print(f'{int(numerator/denominator):4} {numerator/denominator:.{precision}f}')
    
    # for loop to estimate the value of Pi depending on a certain nth term using the horizontal first method
    for num in range(1, num_terms):
        numerator *= num
        denominator *= (num*2+1)
        product = numerator/denominator
        sum += product
        
        # printing every value of estimate of a given term from (1, nth term) inclusive and the second parameter representing the formating data 
        print(f"{num+1:4} {product:.{precision}f}")
    
    # multiply by 2 the sum to get the final estimated pi at the given nth 
    estimated_pi = 2 * sum
    
    # printing the estimated term
    print(f'The Pi is estimated to be: {estimated_pi:.{precision}f}')
    
    
# calling our function estimate_Pi with different nth term
estimate_Pi(10,144.1)
estimate_Pi(10.1,144)
estimate_Pi(10, 10)
estimate_Pi(10, 20)
estimate_Pi(15, 10)
estimate_Pi(15, 20)