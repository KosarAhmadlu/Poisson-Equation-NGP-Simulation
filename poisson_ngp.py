
# Simulation of charge density distribution and Poisson's equation solution using the NGP method

import numpy as np
import matplotlib.pyplot as plt

# Number of particles and simulation domain range
num_particles = 30
x_start, x_end = 0, 10
N = 10  # Number of grid cells
dx = (x_end - x_start) / (N+1)  # Grid spacing (cell width)

# Generate random particle positions within the domain
particles_pos = np.random.uniform(x_start, x_end, num_particles)

# Calculate the center positions of each grid cell
cell_centers = x_start + dx * np.arange(1, N + 1)

# Initialize charge density array with zeros
rho = np.zeros(N)

# NGP method to assign particle charges to the closest cell
for x in particles_pos:
    # Find index of the nearest cell center to the particle
    index = int((x - x_start + dx/2) // dx)
    if 0 <= index < N:
        # Add particle charge (q = 1), normalized by cell width
        rho[index] += 1 / dx

# Create tridiagonal matrix A for solving Poisson's equation
A = np.zeros((N, N))
for i in range(N):
    A[i, i] = 2  # Diagonal elements
    if i > 0:
        A[i, i-1] = -1  # Subdiagonal elements
    if i < N-1:
        A[i, i+1] = -1  # Superdiagonal elements

# Right-hand side vector: b = -rho * dx^2
b = -(dx**2) * rho

# Solve the linear system A * phi = b to find the potential
phi_internal = np.linalg.solve(A, b)

# Add boundary conditions: phi = 0 at both ends (Dirichlet)
phi = np.zeros(N + 2)        # Include two extra points for boundaries
phi[1:-1] = phi_internal     # Fill internal potential values

# Compute electric field E = -d(phi)/dx using central difference
E = -(phi[2:] - phi[:-2]) / (2 * dx)

# Electric field is defined at cell centers
E_points = cell_centers

plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(particles_pos, np.zeros_like(particles_pos), 'ro')
plt.title("Particle Positions")
plt.xlim(x_start, x_end)

plt.subplot(3, 1, 2)
plt.bar(cell_centers, rho, width=dx*0.9)
plt.title("Charge Density (NGP)")
plt.xlim(x_start, x_end)

plt.subplot(3, 1, 3)
plt.plot(np.linspace(x_start, x_end, N + 2), phi, label='Potential Φ')
plt.plot(E_points, E, label='Electric Field E')
plt.title("Potential and Electric Field")
plt.legend()
plt.xlim(x_start, x_end)
plt.tight_layout()
plt.show()