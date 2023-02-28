import numpy as np
import matplotlib.pyplot as plt
# y = sinx
t = np.arange(0,6 *np.pi,0.1)
y = np.sin(t)
f = np.square(t)
plt.plot(t, y, f)
print(len(t))


# Y = d(sin x)/dx
dy = np.diff(y)
dt = np.diff(t)
df = np.diff(f)
gradient_sin = dy/dt
gradient_quad = df/dt
plt.plot(t[0:len(t)-1], gradient_sin, gradient_quad)
plt.show()
