
import pandas as pd
from black_scholes import estimation
import matplotlib.pyplot as plt
from predict import strategy
# Vamos a utilizar como datos de entrenamiento los días del mes de julio 
# y trateremos de predecir las cotizaciones en agosto

bsan = pd.read_csv("BANCO-SANTANDER.csv", sep = ";", skiprows= 1, names = ["price","date"])
bsan["date"] = pd.to_datetime(bsan["date"], format='%d-%m-%Y')
bsan = bsan.sort_values(by = "date", ascending = True).reset_index(drop=True)
july = bsan[bsan["date"].dt.month == 7] 
august = bsan[bsan["date"].dt.month == 8]
august = pd.concat([july.iloc[-1:],august],ignore_index= True )


july_estimation = estimation(july["price"], 1/253,6)
# print([july_estimation[0], july_estimation[1]])

# plt.close()
# plt.plot(august["date"],august["price"])
# plt.plot(july["date"],july["price"])
# plt.plot(august["date"],july_estimation[2])
# plt.plot(august["date"],july_estimation[3])
# plt.show()

print(strategy(july["date"],july["price"]))


