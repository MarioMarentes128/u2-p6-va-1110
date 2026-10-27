import matplotlib.pyplot as plt
import numpy as np
#Mario Yañez NC 1110

cant_productos=[100,150,200,300,500]
precio = [4000, 7000,9000,12000,18000]

plt.plot(cant_productos,precio)
plt.show()

# personalizamos grafica
plt.plot(cant_productos,precio,color='green',marker='*',linestyle='dashed',linewidth=2, markersize=12)
plt.title("Ventas de Walmart 1110")
plt.xlabel(" cant prod")
plt.ylabel("precios")
plt.show()
