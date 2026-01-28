from misc import RK4, calculate_arc_length, TIME_HORIZON, TIME_STEP

import casadi as ca
import numpy as np


def system(x: np.ndarray, u: np.ndarray):
    assert x.shape[0] == 3 and u.shape[0] == 2
    return ca.vertcat(u[0] * ca.cos(x[2]), u[0] * ca.sin(x[2]), u[1])


def cost_function(x: np.ndarray, u: np.ndarray):
    """
    Cost function to minimize

    Args:
        x_curr (np.ndarray): state variables. Expected size: 3 x K
        u_curr (np.ndarray): Control variables. Expected size: 2 x K
    """
    eps = 1e-6
    delta = 1e-4

    xk = x
    xkp1 = x[1:]

    state_cost = np.sum((np.linalg.norm(xkp1 - xk, axis=0)**2 + eps)**0.5)
    control_cost = delta * np.sum(np.linalg.norm(u, axis=0)**2)

    return state_cost + control_cost


def solve(x0, xf, constraints, eps=1e-4, delta=1e-3):

    # expected length of arc between points (i.e. distance between points)
    cost_scale = calculate_arc_length(np.hstack((x0[0:2], xf[0:2])))

    num_steps = int(TIME_HORIZON / TIME_STEP)

    u1_max = constraints['u1_max']
    u1_min = constraints['u1_min']
    u2_max = constraints['u2_max']
    u2_min = constraints['u2_min']

    opti = ca.Opti()

    x = opti.variable(3, num_steps + 1)  # num_steps + 1 due to initial state
    u = opti.variable(2, num_steps)

    # initial state
    opti.subject_to(x[:, 0] == x0)

    cost = 0
    for k in range(num_steps):
        # TODO: add future obstacle costs here as opti.subject_to

        opti.subject_to(x[:, k + 1] == RK4(x[:, k], u[:, k], system))

        state_cost_k = ca.sqrt((x[0, k+1] - x[0, k])**2 + (x[1, k+1] - x[1, k])**2 + eps)
        control_cost_k = delta*(u[0, k]**2 + u[1, k]**2)

        cost += (state_cost_k + control_cost_k) / (cost_scale)

    # TODO: Add warm start here

    opti.subject_to(x[0, -1] == xf[0, -1])
    opti.subject_to(x[1, -1] == xf[1, -1])

    opti.subject_to(opti.bounded(u1_min, u[0, :], u1_max))
    opti.subject_to(opti.bounded(u2_min, u[1, :], u2_max))

    opts = {"ipopt.print_level": 0,
            "print_time": 0,
            "ipopt.sb": "yes",
            "ipopt.nlp_scaling_method": "gradient-based"}

    opti.minimize(cost)
    opti.solver("ipopt", opts)

    solution = opti.solve()

    x_opt = solution.value(x)
    u_opt = solution.value(u)

    return x_opt, u_opt
