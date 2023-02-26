import numpy as np
import matplotlib.pyplot as plt

def gaussian(mean , sigma ):
# find x in range mu-3*sigma to mu+3*sigma
    x = np.arange(mean-3 * sigma, mean + 3 * sigma, 0.1)
    y = np.exp(np.square(x-mean)/(-2.0 * sigma * sigma))/(sigma * np.sqrt(2 * np.pi))
    return x, y

if __name__=='__main__':
    print('gaussian_plot using numpy')
    x, y = gaussian(20 , 5)
    plt.plot(x, y)
    
    x, y = gaussian(20 , 1)
    plt.plot(x, y)
    
    x, y = gaussian(20 , 0.5)
    plt.plot(x, y)
    plt.show()
    
    

