import numpy as np
from solver import solve

if __name__ == "__main__":
    x0 = np.array([[2], [0], [np.pi/2]])
    xf = np.array([[-2], [0]])

    constraint = {
        "u1_min": -1,
        "u1_max": 1,
        "u2_min": -1,
        "u2_max": 1
    }

    x_opt, u_opt = solve(x0, xf, constraint)

    print(x_opt[:, 0], x_opt[:, -1])
