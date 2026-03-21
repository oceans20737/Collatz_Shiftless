[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19141352.svg)](https://doi.org/10.5281/zenodo.19141352)

Shiftless Collatz Model
Binary Interference in the 3n+LSB Trajectory
Author: Hiroshi Harada
Date: March 21, 2026
License: Documents (CC BY 4.0), Code (MIT)

Overview
The Shiftless Collatz model is a reformulation of the classical Collatz mapping that removes the right-shift operation (/2) entirely. Instead of discarding the least significant bit (LSB), the model injects the full binary weight 2^v back into the system.
n_{k+1} = 3 n_k + LSB(n_k)
LSB(n_k) = 2^v
Here, v is the position of the least significant 1-bit.
This modification preserves all bit-level information and allows the entire trajectory to be visualized as a 2D binary canvas, revealing fractal structures, carry avalanches, and interference patterns that remain hidden in the standard Collatz process.
This repository includes:
- Python implementations of the Shiftless Collatz model
- Visualizations of trajectories and bitwise structures
- Full research reports (English and Japanese)
- Figures illustrating the model’s behavior

Key Findings
- Equivalence to the Standard Collatz Model
- The odd part of every step matches exactly
- The number of steps until reaching a power of two (“jackpot”) equals the number of odd steps until reaching 1 in the standard Collatz sequence
(Figure 1)
- Carry Avalanches and Fractal Structures
- Rapid disappearance of lower bits
- Sierpiński-like patterns in higher bits
- Complex fractal interference across the trajectory
(Figure 2)
- Two-Phase Structure: Reach and Fill
- Reach: n → 3n
- Fill: 3n → 3n + LSB
(Figure 3)
- Synchronized Comparison of 3n / 3n+1 / 3n+LSB
- 3n: clean Sierpiński gasket
- 3n+1: slightly distorted
- 3n+LSB: structure collapses due to heavy LSB injection
(Figure 4)
- Linear Decomposition and Interference Geometry
n_k = 3(k-1-i) L_i
- Component A: geometric expansion of the seed
- Component B: cumulative LSB contributions
- Interference: overlapping bits trigger carries and annihilate bits
(Figure 5)

Repository Structure
/code
code_01_collatz_shiftless_equivalence.py
code_02_collatz_shiftless_compact.py
code_03_collatz_shiftless_full.py
code_04_collatz_shiftless_comparison.py
code_05_collatz_shiftless_decomposition.py
/docs
Title_Collatz_Shiftless.pdf
Report_EN_Collatz_Shiftless.pdf
Report_JP_Collatz_Shiftless.pdf
README_EN
README_JP
LICENSE
LICENSE-CC-BY-4.0

Requirements
Python 3.9+
NumPy
Matplotlib
Install dependencies:
pip install numpy matplotlib

Running the Visualizations
Example:
python code_02_collatz_shiftless_compact.py
Each script generates one figure corresponding to the research report.

License
Documents: CC BY 4.0
Code: MIT License
Copyright (c) 2026 Hiroshi Harada

Citation
Harada, Hiroshi (2026).
"Shiftless Collatz Model: Binary Interference in the 3n + LSB Trajectory."
Zenodo. DOI: (to be assigned)
