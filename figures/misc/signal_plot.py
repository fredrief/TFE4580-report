import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10,20,2000)
u1 = 0.5*np.sinc(t + 3) + np.sinc(t) - 0.7*np.sinc(t-3)
u2 = 0.5*np.sinc(t - 7) + np.sinc(t-10)- 0.7*np.sinc(t-12)


plt.plot(t, u1, label='u1')
plt.plot(t, u2, label='u2')
plt.legend()
plt.show()
plt.plot(t, 0.5*(u1+u2), label='0.5(u1+u2)')
plt.plot(t, 0.5*(u1-u2), label='0.5(u1-u2)')
plt.legend()
plt.show()
