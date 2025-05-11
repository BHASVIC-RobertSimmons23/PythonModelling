import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

g = 9.81
L = 5
mu = 0.3
dt = 0.01
time = 100

@np.vectorize
def get_theta_double_dot(theta: float, theta_dot: float) -> float:
	return -mu * theta_dot - (g/L) * np.sin(theta)

@np.vectorize
def get_magnitude(x, y):
	return np.sqrt(x ** 2 + y ** 2)

def simulate_pendulum(cur_theta, cur_theta_dot):
	def get_theta_double_dot(theta_dot: float, theta: float) -> float:
		return -mu * theta_dot - (g/L) * np.sin(theta)

	def step():
		nonlocal cur_theta
		nonlocal cur_theta_dot
		cur_theta += cur_theta_dot * dt
		cur_theta_double_dot = get_theta_double_dot(cur_theta_dot, cur_theta)
		cur_theta_dot += cur_theta_double_dot * dt
		return (cur_theta, cur_theta_dot)

	t = np.arange(0, time, dt)
	theta_arr = []
	theta_dot_arr = []
	for _ in t:
		result = step()
		theta_arr.append(result[0])
		theta_dot_arr.append(result[1])
	return [theta_arr, theta_dot_arr]


theta, theta_dot = np.meshgrid(np.linspace(-2 * np.pi, 2 * np.pi, 30), np.linspace(-4, 4, 30))
theta_double_dot = get_theta_double_dot(theta, theta_dot)
magnitudes = get_magnitude(theta_dot, theta_double_dot)

fig, ax = plt.subplots()
ax.quiver(theta, theta_dot, theta_dot/magnitudes, theta_double_dot/magnitudes, magnitudes, cmap='rainbow', scale=60)


ax.set_xlabel('theta')
ax.set_ylabel('angular velocity')

pendulum = simulate_pendulum(np.pi - 0.1, 0)
line = ax.plot(pendulum[0][0], pendulum[1][0], linewidth=2, color='red')[0]

def update(frame):
	x = pendulum[0][:frame]
	y = pendulum[1][:frame]
	line.set_xdata(x)
	line.set_ydata(y)
	return line


ani = animation.FuncAnimation(fig=fig, func=update, frames=math.floor(time/dt), interval=dt)
plt.show()
