import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


class Newton_fractals:

    def __init__(self,
                 polynomial_degree: int = 4,
                 x_lim: tuple = (-2, 2),
                 y_lim: tuple = (-2, 2),
                 resolution: int = 1000,
                 max_iter: int = 50,
                 tolerance: float = 1e-6,
                 ):
        """
        :param polynomial_degree: int | Degree of the polynomial function.
        :param x_lim: Tuple (xmin, xmax) | Specifying the x-axis limits.
        :param y_lim: Tuple (ymin, ymax) | Specifying the y-axis limits.
        :param resolution: int | The resolution of the grid.
        :param max_iter: int | Maximum number of iterations for Newton's method.
        :param tolerance: float | Tolerance for convergence.
        """
        self.degree = polynomial_degree
        self.x = np.linspace(x_lim[0], x_lim[1], resolution)
        self.y = np.linspace(y_lim[0], y_lim[1], resolution)
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.roots = self.compute_roots()
        self.basin = None
        self.iterations = None

    def compute_roots(self):
        return [np.exp(2j * np.pi * i / self.degree) for i in range(self.degree)]

    def f(self, z):
        """
        :param z: Complex numbers representing coordinates in the complex plane
        :return: The polynomial z^x - 1
        """
        return z ** self.degree - 1

    def df(self, z):
        """
        :param z: Complex numbers representing coordinates in the complex plane
        :return: The derivative of the polynomial
        """
        return self.degree * z ** (self.degree - 1)

    def newton_fractals(self):
        """
        Generate Newton's fractals for a given polynomial and its derivative.
        Converge tuple of array (attraction basin indices, number of iterations to converge).
        """
        X, Y = np.meshgrid(self.x, self.y)
        Z = X + 1j * Y

        self.basin = np.zeros(Z.shape, dtype=int)
        self.iterations = np.zeros(Z.shape, dtype=int)

        for i in tqdm(range(self.max_iter)):
            Z_prev = Z
            Z = Z - f(Z) / df(Z)
            converged = np.abs(Z - Z_prev) < self.tolerance  # not changing
            not_assigned = (self.basin == 0)
            newly_converged = converged & not_assigned
            self.iterations[newly_converged] = i
            for root_idx, root in enumerate(self.roots, start=1):
                is_root = np.abs(Z - root) < self.tolerance
                self.basin[is_root & newly_converged] = root_idx

            if np.all(converged):
                break

        # return basin, iterations


def newton_fractals(f, df, roots, xlim, ylim, resolution, max_iter, tolerance):
    """
    Generate Newton's fractals for a given polynomial and its derivative.

    Parameters:
    - f: The polynomial function.
    - df: The derivative of the polynomial.
    - roots: Known roots of the polynomial for color mapping.
    - xlim: Tuple (xmin, xmax) specifying the x-axis limits.
    - ylim: Tuple (ymin, ymax) specifying the y-axis limits.
    - resolution: The resolution of the grid.
    - max_iter: Maximum number of iterations for Newton's method.
    - tolerance: Tolerance for convergence.

    Returns:
    - Tuple of arrays: (attraction basin indices, number of iterations to converge)
    """
    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    basin = np.zeros(Z.shape, dtype=int)
    iterations = np.zeros(Z.shape, dtype=int)

    for i in tqdm(range(max_iter)):
        Z_prev = Z
        Z = Z - f(Z) / df(Z)
        converged = np.abs(Z - Z_prev) < tolerance  # not changing
        not_assigned = (basin == 0)
        newly_converged = converged & not_assigned
        iterations[newly_converged] = i
        for root_idx, root in enumerate(roots, start=1):
            is_root = np.abs(Z - root) < tolerance
            basin[is_root & newly_converged] = root_idx

        if np.all(converged):
            break

    return basin, iterations


# Example usage:
def f(z):
    return z ** 3 - 1  # Example polynomial: z^3 - 1


def df(z):
    return 3 * z ** 2  # Derivative of the polynomial


# Known roots of the polynomial for color mapping
roots = [np.exp(2j * np.pi * i / 3) for i in range(3)]

# Generate fractals
basin, iterations = newton_fractals(f, df, roots, (-2, 2), (-2, 2), resolution=1000, max_iter=50, tolerance=1e-6)

# Plotting
plt.figure(figsize=(12, 6))

# Attraction basins
plt.subplot(1, 2, 1)
plt.imshow(basin, extent=(-2, 2, -2, 2), cmap='Greys')
plt.title('Attraction Basins')

# Convergence rate
plt.subplot(1, 2, 2)
plt.imshow(iterations, extent=(-2, 2, -2, 2), cmap='Greys')
plt.title('Convergence Rate')

plt.show()
