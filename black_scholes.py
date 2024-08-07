import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from brownian_motion import Brownian

data = pd.read_csv("Datos.csv")


def estimation(prices, dt, number_of_days=31):
    logs_return = []
    for i in range(1, len(prices)):
        logs_return.append(prices[i] / prices[i - 1])
    logs_return = np.log(logs_return)
    mu = np.mean(logs_return) / dt
    sigma = np.std(logs_return) / np.sqrt(dt)
    z_score = stats.norm.ppf(0.975)
    delta = [i * dt for i in range(number_of_days)]
    aux = np.sqrt(delta) * sigma * z_score + mu * np.array(delta)
    min_interval, max_interval = (
        np.exp(-aux) * data["price"][len(data["price"]) - 1],
        np.exp(+aux) * data["price"][len(data["price"]) - 1],
    )
    return (mu, sigma, min_interval, max_interval)


result = estimation(data["price"][:-7], 1 / 253)
brownian_motion = Brownian(0)

    
def plot_stock_price(mu, sigma, min_intervals, max_intervals):
    """
    Plots stock price for multiple scenarios
    """
    plt.figure(figsize=(9, 4))
    plt.plot(min_intervals, "o", markersize=20)
    plt.plot(max_intervals, "o", markersize=20)
    for i in range(100):
        plt.plot(
            brownian_motion.stock_price_classic(
                s0=data["price"][len(data["price"]) - 1],
                mu=mu,
                sigma=sigma,
                dt=1 / 253,
                deltaT=7 / 253,
            )
        )
    plt.show()


plt.plot(data["price"])
plt.plot(result[2])
plt.plot(result[3])
plt.plot(result[0] * np.arange(1, 59))
# plt.xlim(51, 58)
plt.show()
# plot_stock_price(result[0], result[1], result[2], result[3])
# Esto es lo que vio coto