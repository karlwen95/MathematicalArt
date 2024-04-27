import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm


class Newton_fractals:

    def __init__(self,
                 polynomial_degree: int = 4,
                 x_lim: tuple = (-2, 2),
                 y_lim: tuple = (-2, 2),
                 resolution: int = 1000,
                 max_basins_iter: int = 50,
                 tolerance: float = 1e-6,
                 ):
        """
        :param polynomial_degree: int | Degree of the polynomial function.
        :param x_lim: Tuple (xmin, xmax_basins) | Specifying the x-ax_basinsis limits.
        :param y_lim: Tuple (ymin, ymax_basins) | Specifying the y-ax_basinsis limits.
        :param resolution: int | The resolution of the grid.
        :param max_basins_iter: int | Max_basinsimum number of iterations for Newton's method.
        :param tolerance: float | Tolerance for convergence.
        """
        self.degree = polynomial_degree
        self.x = np.linspace(x_lim[0], x_lim[1], resolution)
        self.y = np.linspace(y_lim[0], y_lim[1], resolution)
        self.max_basins_iter = max_basins_iter
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

    def compute(self):
        """
        Generate Newton's fractals for a given polynomial and its derivative.
        Converge tuple of array (attraction basin indices, number of iterations to converge).
        """
        if self.roots is None:
            print('Computing roots...')
            self.compute_roots()
            print('Done!')

        X, Y = np.meshgrid(self.x, self.y)
        Z = X + 1j * Y

        self.basin = np.zeros(Z.shape, dtype=int)
        self.iterations = np.zeros(Z.shape, dtype=int)

        for i in tqdm(range(self.max_basins_iter), desc='Iterations'):
            Z_prev = Z
            Z = Z - self.f(Z) / self.df(Z)
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

    def generate_basins_fig(self, fig_size=(4, 4), dpi=300, cmap='Greys'):
        """
        Generate the figure displaying the roots each pixel converges to.
        :param fig_size: tuple | Size of figure. Preferably square-shape.
        :param dpi: int | dots per inch.
        :param cmap: str | colormap for imshow
        :return: fig object
        """
        fig = plt.figure(figsize=fig_size, dpi=dpi)
        plt.imshow(self.basin, extent=(self.x[0], self.x[-1], self.y[0], self.y[-1]), cmap=cmap)
        plt.title('Attraction basins')
        return fig

    def generate_convergence_rate_fig(self, fig_size=(4.8, 4.8), dpi=300, cmap='Greys'):
        """
        Generate the figure displaying the convergence rate with which each pixel converges.
        :param fig_size: tuple | Size of figure. Preferably square-shape.
        :param dpi: int | dots per inch.
        :param cmap: str | colormap for imshow
        :return: fig object
        """
        fig = plt.figure(figsize=fig_size, dpi=dpi)
        plt.imshow(self.iterations, extent=(self.x[0], self.x[-1], self.y[0], self.y[-1]), cmap=cmap)
        plt.title('Convergence rate')
        return fig


if __name__ == '__main__':
    polynomial_degree = 4
    x_lim = (-2, 2)
    y_lim = (-2, 2)
    resolution = 10
    max_basins_iter = 50
    tolerance = 1e-6

    nf = Newton_fractals(polynomial_degree=polynomial_degree,
                         x_lim=x_lim,
                         y_lim=y_lim,
                         resolution=resolution,
                         max_basins_iter=max_basins_iter,
                         tolerance=tolerance)
    nf.compute()
    fig_basins = nf.generate_basins_fig()
    fig_basins.show()

    # remove all spines for basins figure
    ax_basins = fig_basins.gca()
    ax_basins.spines['top'].set_visible(False)
    ax_basins.spines['bottom'].set_visible(False)
    ax_basins.spines['right'].set_visible(False)
    ax_basins.spines['left'].set_visible(False)
    ax_basins.xaxis.set_visible(False)
    ax_basins.yaxis.set_visible(False)
    ax_basins.set_title('')
    fig_basins.savefig(f'../figures/newton_fractals/basins_resolution{resolution}.png', format='png')

    dpi = 300
    fig_size_pixel = 1280
    fig_size = (fig_size_pixel / dpi, fig_size_pixel / dpi)
    fig_rate = nf.generate_convergence_rate_fig(fig_size=fig_size, dpi=dpi)
    fig_rate.show()

    # remove all spines for convergence rate figure
    ax_convrate = fig_rate.gca()
    ax_convrate.spines['top'].set_visible(False)
    ax_convrate.spines['bottom'].set_visible(False)
    ax_convrate.spines['right'].set_visible(False)
    ax_convrate.spines['left'].set_visible(False)
    ax_convrate.xaxis.set_visible(False)
    ax_convrate.yaxis.set_visible(False)
    ax_convrate.set_title('')
    fig_rate.savefig(f'../figures/newton_fractals/convrate_resolution{resolution}.png', format='png')
