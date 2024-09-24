import matplotlib.pyplot as plt
import numpy as np

#MARCELO ALVARO CHAMBI CHILLO
x1 = np.linspace(0, 3, 100)
x2_1 = (2 - 1.0001 * x1)  
x2_2 = (2 - 1.0000 * x1)  

plt.plot(x1, x2_1, 'r', label='1.0001x1 + 1.0000x2 = 2', linewidth=2)
plt.plot(x1, x2_2, 'b', label='1.0000x1 + 1.0000x2 = 2', linewidth=2)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Gráfico del sistema de ecuaciones lineales')
plt.legend()
plt.grid(True)
plt.show()
