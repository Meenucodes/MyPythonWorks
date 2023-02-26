import math as m
import matplotlib.pyplot as plt
def range_float(start,stop,step):
    x = []
    element = start
    x.append(element)    
    while(element < stop):
        element = element + step
        x.append(float (element))
    return x
def plot_gaussian(mu,sigma):
    # find x in range from mu-3sigma to mu+3sigma
    X = range_float((mu-3*sigma),(mu+3*sigma),0.1)
    Y = []
    for e in X:
        x_2 = (e-mu)**2/(-1*2*sigma**2)
        y_l = m.exp(x_2)/(sigma*m.sqrt(2*m.pi))
        Y.append(float (y_l))
        
    return X,Y

print("gaussian plot")
X_G,Y_G = plot_gaussian(20.0 , 2.0)
plt.plot(X_G,Y_G)
plt.show()
