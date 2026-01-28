import numpy as np

TIME_STEP = 0.1  # s
TIME_HORIZON = 10  # steps

K = int(TIME_HORIZON / TIME_STEP)


def RK4(x_curr: np.ndarray, u_curr: np.ndarray, func):

    k1 = func(x_curr, u_curr)
    k2 = func(x_curr + (k1 * TIME_STEP/2), u_curr)
    k3 = func(x_curr + (k2 * TIME_STEP/2), u_curr)
    k4 = func(x_curr + (k3 * TIME_STEP), u_curr)

    rk4 = k1 + 2 * k2 + 2 * k3 + k4

    return x_curr + ((TIME_STEP / 6) * rk4)
