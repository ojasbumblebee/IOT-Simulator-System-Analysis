import math


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



random_variate, psuedo_random_number = random_number_main(lambda_mean=6)
random_variate, psuedo_random_number = random_number_main(lambda_mean=5)

print(random_variate, psuedo_random_number)
