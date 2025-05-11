# boilerplate
import numpy as np
from collections.abc import Callable

# Integrand from Q8
def ln_spiral(x: float) -> float:
	return np.log(x) * np.cos(x) * np.sqrt(np.log(x) ** 2 + x ** -2)

# Integrand from Q3
def elliptic_integral(x: float) -> float:
	return np.sqrt(1 + 3 * np.cos(2 * x) ** 2)

# interesting bit
def simpsons(integrand: Callable[[float], float], lower_bound: float, upper_bound: float, num_strips: int = 1000):
	if num_strips % 2 != 0: raise ValueError('Number of strips must be even')
	interval, h = np.linspace(lower_bound, upper_bound, num_strips + 1, retstep=True)
	y_values = integrand(interval)
	sum = y_values[0] + y_values[-1] + 4 * np.sum(y_values[1:-1:2]) + 2 * np.sum(y_values[2:-1:2])
	return 1/3 * h * sum

# boring trapezium rule
def trapezium(integrand: Callable[[float], float], lower_bound: float, upper_bound: float, num_strips: int = 1000):
	interval, h = np.linspace(lower_bound, upper_bound, num_strips + 1, retstep=True)
	y_values = integrand(interval)
	sum = y_values[0] + y_values[-1] + 2 * np.sum(y_values[1:-1])
	return 1/2 * h * sum

print('Question 8:', np.abs(simpsons(ln_spiral, 1, np.pi) * 2 * np.pi))
print('Question 3:', simpsons(elliptic_integral, 0, np.pi / 2), trapezium(elliptic_integral, 0, np.pi/2))