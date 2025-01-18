import math

print(f'{"No. terms":9}', f'{"Estimate":42}', f'{"Compared with math.pi":42}')

# loop to iterate through the terms of multiples of 5 from fifth term to 50th term
for num_terms in range(5, 51, 5):
    sum = 1
    product = 1
    
    # calculating the estimate pi depending on the term 
    for i in range(1, num_terms):
        est = i / (i*2 + 1)
        product *= est
        sum += product
    
    estimate_pi = 2*sum
    error_estimate = math.pi - estimate_pi
    print(f'{num_terms:9}', f'{estimate_pi:.40f}', f'{error_estimate:.40f}')
    
print(f'The last term is {product:.40f}')    
