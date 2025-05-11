import matplotlib.pyplot as plt
import numpy as np

g = 9.81
L = 5
mu = 0.3

@np.vectorize
def get_theta_double_dot(theta: float, theta_dot: float) -> float:
	return -mu * theta_dot - (g/L) * np.sin(theta)

@np.vectorize
def get_magnitude(x, y):
	return np.sqrt(x ** 2 + y ** 2)


theta, theta_dot = np.meshgrid(np.linspace(-2 * np.pi, 2 * np.pi, 30), np.linspace(-4, 4, 30))
theta_double_dot = get_theta_double_dot(theta, theta_dot)
magnitudes = get_magnitude(theta_dot, theta_double_dot)

fig, ax = plt.subplots()
ax.quiver(theta, theta_dot, theta_dot/magnitudes, theta_double_dot/magnitudes, magnitudes, cmap='rainbow', scale=60)


ax.set_xlabel('theta')
ax.set_ylabel('angular velocity')
plt.show()