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


def generate_full(seed, max_steps=100):
    """
    Generate a full visualization matrix for the Shiftless Collatz trajectory,
    explicitly separating the internal two-phase structure:

        1. Reach phase: n -> 3n
        2. Fill phase: 3n -> 3n + LSB(n)

    This reveals how geometric expansion (Reach) and LSB injection (Fill)
    interact to produce carry avalanches and fractal distortions.

    The output matrix uses:
        0 = padding
        1 = bit '0'
        2 = bit '1'
    """

    n = seed
    history = []

    # --- Step 1: Ascending (Reach + Fill) ---
    while True:
        # Record current n
        history.append(bin(n)[2:])

        # Extract LSB weight
        lsb = n & -n

        # Reach phase: 3n
        n_triple = 3 * n
        history.append(bin(n_triple)[2:])

        # Fill phase: 3n + LSB
        n = n_triple + lsb

        # Jackpot check: n is a power of 2
        if n > 0 and ((n & (n - 1)) == 0):
            history.append(bin(n)[2:])
            break

        # Safety limit
        if len(history) > max_steps * 2:
            break

    # --- Step 2: Finale (n // 2) ---
    while n > 1:
        n //= 2
        history.append(bin(n)[2:])

    # --- Convert history to matrix ---
    max_len = max(len(bits) for bits in history)
    matrix = np.zeros((len(history), max_len))

    for i, bits in enumerate(history):
        bits_rev = bits[::-1]  # LSB on the right
        for j, char in enumerate(bits_rev):
            matrix[i, j] = 2 if char == '1' else 1

    return matrix


if __name__ == "__main__":
    seed = 27
    mat = generate_full(seed)

    fig, ax = plt.subplots(figsize=(6, 8))
    fig.patch.set_facecolor('#1a1a1a')
    ax.set_facecolor('#1a1a1a')

    # Cyberpunk color scheme:
    # 0 = background, 1 = bit 0 (gray), 2 = bit 1 (cyan)
    cmap = ListedColormap(['#1a1a1a', '#555555', '#00ffcc'])

    ax.imshow(mat, cmap=cmap, aspect='auto', interpolation='nearest')
    ax.invert_xaxis()  # LSB on the right

    ax.set_title(f"Shiftless Collatz (Reach + Fill): Seed {seed}",
                 color='white', fontsize=16)
    ax.set_ylabel("Sub-steps (Time Flow Downward)", color='white')
    ax.set_xlabel("Bit Position (0 is LSB on the Right)", color='white')

    ax.tick_params(colors='gray')
    for spine in ax.spines.values():
        spine.set_color('#333333')

    plt.tight_layout()
    plt.show()


# In[ ]:




