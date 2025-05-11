import matplotlib.pyplot as plt
import numpy as np

g = 9.81
L = 5
mu = 0.3
theta = np.pi - 0.1
theta_dot = 0
dt = 0.01

def get_theta_double_dot(theta_dot: float, theta: float) -> float:
	return -mu * theta_dot - (g/L) * np.sin(theta)

def step():
	global theta
	global theta_dot
	theta += theta_dot * dt
	theta_double_dot = get_theta_double_dot(theta_dot, theta)
	theta_dot += theta_double_dot * dt
	return theta

t = np.arange(0, 100, dt)
theta_arr = []
for _ in t:
	theta_arr.append(step())

fig, ax = plt.subplots()
ax.plot(t, theta_arr)
plt.show()