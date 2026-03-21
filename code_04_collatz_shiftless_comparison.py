#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Copyright (c) 2026 Hiroshi Harada
# Licensed under the MIT License.
# https://opensource.org/licenses/MIT
# Author: Hiroshi Harada
# Date: March 21, 2026

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def get_shiftless_steps(seed):
    """
    Compute the number of steps required for the Shiftless Collatz trajectory
    (n -> 3n + LSB) to reach a power of two (the Jackpot).

    This step count is used to synchronize:
        - 3n
        - 3n + 1
        - 3n + LSB
    so that all three dynamics can be compared fairly.
    """
    n = seed
    steps = 0

    # Already a power of 2?
    if n > 0 and ((n & (n - 1)) == 0):
        return steps

    while True:
        lsb = n & -n
        n = 3 * n + lsb
        steps += 1

        # Jackpot check
        if n > 0 and ((n & (n - 1)) == 0):
            break

    return steps


def generate_matrix_synced(seed, mode, total_steps):
    """
    Generate a binary matrix representing the evolution of one of the following:
        - '3n'       : pure geometric expansion
        - '3n+1'     : standard Collatz odd-step
        - '3n+LSB'   : Shiftless Collatz

    All dynamics are progressed for exactly total_steps iterations.
    """
    n = seed
    history = [bin(n)[2:]]

    for _ in range(total_steps):
        if mode == "3n":
            n = 3 * n
        elif mode == "3n+1":
            n = 3 * n + 1
        elif mode == "3n+LSB":
            lsb = n & -n
            n = 3 * n + lsb

        history.append(bin(n)[2:])

    # Convert history to matrix
    max_len = max(len(bits) for bits in history)
    matrix = np.zeros((len(history), max_len))

    for i, bits in enumerate(history):
        bits_rev = bits[::-1]  # LSB on the right
        for j, char in enumerate(bits_rev):
            matrix[i, j] = 2 if char == "1" else 1

    return matrix


if __name__ == "__main__":
    seed = 27

    # Step count synchronized to Shiftless Collatz jackpot
    max_steps = get_shiftless_steps(seed)

    # Generate all three dynamics
    mat_3n = generate_matrix_synced(seed, "3n", max_steps)
    mat_3n1 = generate_matrix_synced(seed, "3n+1", max_steps)
    mat_shiftless = generate_matrix_synced(seed, "3n+LSB", max_steps)

    # Plotting setup
    fig, axes = plt.subplots(1, 3, figsize=(16, 8), facecolor="#1a1a1a")

    cmap = ListedColormap(["#1a1a1a", "#555555", "#00ffcc"])  # BG, 0-bit, 1-bit
    titles = [
        "Pure Expansion: 3n",
        "Fixed Addition: 3n + 1",
        "Shiftless Collatz: 3n + LSB"
    ]
    matrices = [mat_3n, mat_3n1, mat_shiftless]

    for ax, matrix, title in zip(axes, matrices, titles):
        ax.set_facecolor("#1a1a1a")
        ax.imshow(matrix, cmap=cmap, aspect="auto", interpolation="nearest")
        ax.invert_xaxis()  # LSB on the right

        ax.set_title(title, color="white", fontsize=14, pad=15)
        ax.set_xlabel("Bit Position (0 is LSB on Right)", color="white")
        ax.tick_params(colors="gray")

        for spine in ax.spines.values():
            spine.set_color("#333333")

    axes[0].set_ylabel(
        f"Steps (Synchronized to {max_steps} jumps)",
        color="white"
    )

    fig.suptitle(
        f"Binary Dynamics Comparison (Time-Synced): Seed {seed}",
        color="white",
        fontsize=20,
        fontweight="bold"
    )

    plt.tight_layout()
    plt.show()


# In[ ]:




