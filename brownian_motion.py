import numpy as np


class Brownian:
    """
    A Brownian motion class constructor
    """

    def __init__(self, x0=0):
        """
        Init class
        """
        assert (
            type(x0) == float or type(x0) == int or x0 is None
        ), "Expect a float or None for the initial value"

        self.x0 = float(x0)

    def gen_normal(self, n_step=100, dt=0.1):
        """
           Generate motion by drawing from the Normal distribution

           Arguments:
               n_step: Number of steps

           Returns:
               A NumPy array with `n_steps
        + 1` points representing the Wiener process
        """
        w = np.zeros(n_step + 1)  # Initialize with zeros
        w[0] = self.x0
        for i in range(1, n_step + 1):
            # Efficiently sample one random number
            dw = np.random.normal(0, np.sqrt(dt))
            w[i] = w[i - 1] + dw
        return w

    def stock_price_classic(self, s0=100, mu=0.2, sigma=0.68, deltaT=52, dt=0.1):
        """
        Models a stock price S(t) using the Weiner process W(t) as
        `S(t) = S(0)*exp{(mu*t)+sigma*W(t)}`

        Arguments:
            s0: Inital stock price, default 100
            mu: 'Drift' of the stock (upwards or downwards), default 1
            sigma: 'Volatility' of the stock, default 1
            deltaT: The time period for which the future prices are computed, default 52 (as in 52 weeks)
            dt (optional): The granularity of the time-period, default 0.1

        Returns:
            s: A NumPy array with the simulated stock prices over the time-period deltaT
        """
        n_step = int(deltaT / dt)
        time_vector = np.linspace(0, deltaT, num=n_step + 1)
        stock_var = mu * time_vector
        # Weiner process (calls the `gen_normal` method)
        weiner_process = self.gen_normal(n_step, dt)
        # Add two time series, take exponent, and multiply by the initial stock price
        s = s0 * np.exp(stock_var + sigma * weiner_process)
        return s
