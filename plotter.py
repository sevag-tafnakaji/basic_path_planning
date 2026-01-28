import matplotlib.pyplot as plt
import numpy as np


def plot_solution_in_state_space(x_tot,
                                 title,
                                 arc_length,
                                 eps=None,
                                 delta=None):
    x1 = x_tot[0]
    x2 = x_tot[1]
    fig = plt.figure(figsize=(7, 7))
    gs_position_space = fig.add_gridspec(1, 1)
    ax6 = fig.add_subplot(gs_position_space[0])
    ax6.set_title(title, fontsize=14)
    ax6.set_xlabel('x1')
    ax6.set_ylabel('x2')
    ax6.grid(True)
    ax6.set_aspect('equal')

    # Plot the initial and final states
    ax6.plot([x1[0], x1[-1]], [x2[0], x2[-1]], 'k.')
    ax6.plot(x1, x2, 'g-')
    epsilon = 0.05
    ax6.annotate(
        r'$\mathbf{x}^{\mathrm{ini}}$',
        xy=(x1[0], x2[0] + epsilon),
        xytext=(x1[0], x2[0] + epsilon)
    )
    ax6.annotate(
        r'$\mathbf{x}^{\mathrm{tar}}$',
        xy=(x1[-1] - 2*epsilon, x2[-1] + epsilon),
        xytext=(x1[-1] - 2*epsilon, x2[-1] + epsilon)
    )
    ax6.annotate(
        f'Arc length: {arc_length}',
        xy=(-2, 0.7),
        xytext=(-2, 0.7)
    )
    ax6.annotate(
        rf'$\varepsilon$: {eps}',
        xy=(-2, 0.6),
        xytext=(-2, 0.6)
    )
    ax6.annotate(
        rf'$\delta$: {delta}',
        xy=(-2, 0.5),
        xytext=(-2, 0.5)
    )

    # Plot the obstacles
    # TODO: Plot obstacles

    ax6.set_ylim(top=0.9, bottom=-0.9)

    fig.tight_layout(rect=[0, 0, 1, 0.95])


def plot_solution_in_statespace_and_control(x_tot,
                                            u_tot,
                                            arc_length,
                                            eps=None,
                                            delta=None):
    x1 = x_tot[0]
    x2 = x_tot[1]
    fig = plt.figure(figsize=(7, 9))
    gs_position_space = fig.add_gridspec(3, 1, height_ratios=[2, 1, 1])
    ax6 = fig.add_subplot(gs_position_space[0])
    ax6.set_title('State space', fontsize=14)
    ax6.set_xlabel('x1')
    ax6.set_ylabel('x2')
    ax6.grid(True)
    ax6.set_aspect('equal')

    # Plot the initial and final states
    ax6.plot([x1[0], x1[-1]], [x2[0], x2[-1]], 'k.')
    ax6.plot(x1, x2, 'g-')
    epsilon = 0.05
    ax6.annotate(
        r'$\mathbf{x}^{\mathrm{ini}}$',
        xy=(x1[0], x2[0] + epsilon),
        xytext=(x1[0], x2[0] + epsilon)
    )
    ax6.annotate(
        r'$\mathbf{x}^{\mathrm{tar}}$',
        xy=(x1[-1] - 2*epsilon, x2[-1] + epsilon),
        xytext=(x1[-1] - 2*epsilon, x2[-1] + epsilon)
    )
    ax6.annotate(
        f'Arc length: {arc_length}',
        xy=(-2, 0.7),
        xytext=(-2, 0.7)
    )
    ax6.annotate(
        rf'$\varepsilon$: {eps}',
        xy=(-2, 0.6),
        xytext=(-2, 0.6)
    )
    ax6.annotate(
        rf'$\delta$: {delta}',
        xy=(-2, 0.5),
        xytext=(-2, 0.5)
    )

    # Plot the obstacles
    # TODO: Plot obstacles

    ax6.set_ylim(top=0.9, bottom=-0.9)

    ax1 = fig.add_subplot(gs_position_space[1])
    ax2 = fig.add_subplot(gs_position_space[2], sharex=ax1)

    # Plot control versus time
    u1 = u_tot[0]
    u2 = u_tot[1]
    time = np.arange(u_tot.shape[1] + 1)
    ax1.step(time, np.append(u1[0], u1), 'g-', label='u1 (velocity)')
    ax1.set_title("u1 vs time", fontsize=14)
    ax1.set_xlabel('Time step')
    ax1.legend()
    ax1.grid(True)
    ax1.set_ylim(top=1.1, bottom=-1.1)

    ax2.step(time, np.append(u2[0], u2), 'g-', label='u2 (turning rate)')
    ax2.set_title("u2 vs time", fontsize=14)
    ax2.set_xlabel('Time step')
    ax2.legend()
    ax2.grid(True)
    ax1.set_ylim(top=1.1, bottom=-1.1)

    fig.tight_layout(rect=[0, 0, 1, 0.95])

    plt.show()
