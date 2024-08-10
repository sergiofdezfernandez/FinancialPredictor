import pandas as pd
from black_scholes import estimation
import matplotlib.pyplot as plt
import math as mt
import numpy as np
import datetime 

## Función que reciba un conjunto de fechas y precios y dé una estrategia de inversión ##
def strategy(dates,prices, number_of_days = 7):
    dates = pd.to_datetime(dates)
    dt = dates.sort_values().diff().dt.days.min()
    result = estimation(prices,dt,number_of_days)
    mean = result[0]
    sd = result[1]
    if (abs(mean) > 0.75) and (sd < 0.5):
        action = 1*mt.copysign(mean)
    else:
        action = 0
    predicted_dates = []
    for i in range(number_of_days):
        fecha = dates[len(dates)-2] + datetime.timedelta(days=i+1)
        predicted_dates.append(fecha)
  
    plt.close()
    plt.plot(dates,prices)
    plt.plot(predicted_dates, result[2])
    plt.plot(predicted_dates, result[3])
    plt.show()
    return(action)