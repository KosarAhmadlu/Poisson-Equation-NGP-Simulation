# Poisson Equation Solver Using the NGP Method

## Overview
This project simulates the charge density distribution of particles in a one-dimensional domain using the Nearest Grid Point (NGP) method. It then solves Poisson's equation numerically to calculate the electric potential and estimate the electric field.

The program generates plots showing particle positions, charge density, electric potential, and electric field.

## Numerical Methods
- **NGP method:** Assigns each particle's charge to its nearest grid cell.
- **Poisson equation:** Solves a linear system to determine the electric potential.
- **Dirichlet boundary conditions:** Sets the electric potential to zero at both boundaries.
- **Electric field:** Estimates the field using finite differences.

## Requirements
- Python 3
- NumPy
- Matplotlib

## Parameters
The simulation parameters include the number of particles, domain boundaries, and number of grid cells. These can be modified in the source code.

## Notes
Particle positions are randomly generated, so results may differ between runs.

## License
This project is available for educational and research purposes.