import math

"""
# helper function to generate psuedo random
def rng(xi, a, c, m):
    new_xi = (a*xi+c)%m
    return new_xi


#helper function to generate random_variate
#return exponentially  generated random variate
def random_variate_generator(lambda_mean, psuedo_random_number):
    logarithm = math.log(psuedo_random_number)
    random_variate = -logarithm/lambda_mean
    return random_variate


#main_function 
def random_number_main(lambda_mean, seed=0.1, a=3, c=9, m=16):
    
    psuedo_random_number = rng(seed, a, c, m)
    random_variate = random_variate_generator(lambda_mean, psuedo_random_number)
    return random_variate, psuedo_random_number
"""



xi = 1

#function to generate random number using congruential method
def rng(a, c, m):
    global xi
    xi = (a*xi + c)%m
    return xi/m

#function to generate exponential random variate using inverse transformation method
def random_variate_generator(lambda_mean, psuedo_random_number):
    logarithm = math.log(psuedo_random_number)
    random_variate = -(logarithm/lambda_mean)
    return random_variate

#main function to return generated random variate and seed
def random_number_main(lambda_mean, m=2**32, a=1103515245, c=12345):
    psuedo_random_number = rng(a, c, m)
    random_variate = random_variate_generator(lambda_mean, psuedo_random_number)
    return random_variate, psuedo_random_number


for i in range(10):

    random_variate, psuedo_random_number = random_number_main(lambda_mean=6)
    random_variate, psuedo_random_number = random_number_main(lambda_mean=5)

    print(random_variate, psuedo_random_number)

import numpy as np
def expon_icdf(p, lambd=1):
    """Inverse CDF of exponential distribution - i.e. quantile function."""
    return -np.log(1-p)/lambd

u = np.random.random(10000)
v = expon_icdf(u)
print(u,v)
