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
import matplotlib.patches as mpatches


def generate_shiftless_decomposition(seed):
    """
    Simulate the Shiftless Collatz trajectory and decompose each step into:

        A_k = 3^k * n_0
        B_k = Σ_{i=0..k-1} 3^(k-1-i) * L_i
        n_k = A_k + B_k

    The output matrix encodes:
        0 = background
        1 = seed contribution (A_k)
        2 = LSB contribution (B_k)
        3 = interference (A_k and B_k both have bit=1 → carry trigger)
    """

    n = seed
    history_n = [n]
    lsbs = []

    # --- Generate Shiftless trajectory until reaching a power of 2 ---
    while not (n > 0 and ((n & (n - 1)) == 0)):
        lsb = n & -n
        lsbs.append(lsb)
        n = 3 * n + lsb
        history_n.append(n)

    steps = len(history_n)

    # Bit width large enough for A_k and B_k
    max_bits = history_n[-1].bit_length() + 2
    matrix = np.zeros((steps, max_bits))

    # --- Decompose each step ---
    for k in range(steps):
        # A_k = 3^k * seed
        ak = (3 ** k) * seed

        # B_k = n_k - A_k
        bk = history_n[k] - ak

        # Convert to reversed binary strings (LSB on the right)
        a_bin = bin(ak)[2:][::-1]
        b_bin = bin(bk)[2:][::-1]

        for j in range(max_bits):
            bit_a = int(a_bin[j]) if j < len(a_bin) else 0
            bit_b = int(b_bin[j]) if j < len(b_bin) else 0

            if bit_a and not bit_b:
                matrix[k, j] = 1  # Seed-only
            elif not bit_a and bit_b:
                matrix[k, j] = 2  # LSB-only
            elif bit_a and bit_b:
                matrix[k, j] = 3  # Interference (carry trigger)

    return matrix


if __name__ == "__main__":
    seed = 27
    mat = generate_shiftless_decomposition(seed)

    # Color map: background, seed (blue), LSB (gold), interference (magenta)
    cmap = ListedColormap([
        "#000000",  # 0 background
        "#00BFFF",  # 1 seed contribution
        "#FFD700",  # 2 LSB contribution
        "#FF00FF"   # 3 interference
    ])

    fig, ax = plt.subplots(figsize=(12, 14), facecolor="#000000")
    ax.set_facecolor("#000000")

    # Added vmin and vmax to lock the color mapping strictly to 0-3
    ax.imshow(mat, cmap=cmap, aspect="auto", interpolation="nearest", vmin=0, vmax=3)
    ax.invert_xaxis()

    ax.set_title(
        f"Shiftless Collatz Decomposition (Seed: {seed})",
        color="white", fontsize=20, pad=20, fontweight="bold"
    )
    ax.set_xlabel("Bit Position (MSB ← LSB)", color="#aaaaaa", fontsize=12)
    ax.set_ylabel("Evolution Steps (Time Flow)", color="#aaaaaa", fontsize=12)
    ax.tick_params(colors="#666666", labelsize=10)

    # Legend
    legend_items = [
        ("Background", "#000000"),
        ("Seed Contribution (3^k * n0)", "#00BFFF"),
        ("LSB Contribution (Σ 3^(k-1-i) * L_i)", "#FFD700"),
        ("Interference (Carry Trigger)", "#FF00FF")
    ]
    patches = [mpatches.Patch(color=c, label=l) for l, c in legend_items]

    leg = plt.legend(
        handles=patches,
        loc="upper left",
        bbox_to_anchor=(1.02, 1),
        facecolor="#0a0a0a",
        edgecolor="#333333",
        labelcolor="white",
        fontsize=11
    )
    leg.get_frame().set_linewidth(0.5)

    plt.tight_layout()
    plt.show()


# In[ ]:




