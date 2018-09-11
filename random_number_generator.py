def seed(x):
    global xi
    xi = x

def rng():
    global xi
    xi = (a*xi + c)%m
    return xi

a = 3
c = 9
m = 16
xi = 0

for i in range(10):
    print (rng())
                                
