import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
import numpy.linalg as alg
from time import perf_counter
from matplotlib import animation
from pyfonts import load_font
import sys
# Setting font for the plot
cm = load_font(font_path="/Users/mav/Onedrive/026 Fonts/cm-unicode-0.7.0/cmunrm.ttf")


# Defining G the Gravitational Constant
G = const.G

# final time and change in time
frames = 480
t = 3.25e5
delta_t = 6.5

# Masses in our three body problem

m1 = 0
m2 = 1.898e27
m3 = 722


# Arrays for 1, 2, and 3 positions + defining the intial positions

positions_1 = np.ones([3,int(t/delta_t)+2])
positions_2 = np.ones([3,int(t/delta_t)+2])
positions_3 = np.ones([3,int(t/delta_t)+2])
positions_1[0:3,0] = [0,0,0]
positions_2[0:3,0] = [7.405e11,0,0]
positions_3[0:3,0] = [7.405e11-2.1147e9,-1.7873e9,0]
initial_diff = alg.norm(np.subtract(positions_3[:,0], positions_2[:,0]))

# Arrays for 1, 2, and 3 velocities + defining the initial velocities

velocities_1 = np.ones([3,int(t/delta_t)+2])
velocities_2 = np.ones([3,int(t/delta_t)+2])
velocities_3 = np.ones([3,int(t/delta_t)+2])
velocities_1[0:3,0] = [0,0,0]
velocities_2[0:3,0] = [0,-13070,0]
velocities_3[0:3,0] = [1e4,0,0]

# Arrays for 1, 2, and 3 accelerations + defining the initial accelerations (if any)

accelerations_1 = np.zeros([3,int(t/delta_t)+1])
accelerations_2 = np.zeros([3,int(t/delta_t)+1])
accelerations_3 = np.zeros([3,int(t/delta_t)+1])

# Array for time 

time_array = np.linspace(0, t, (int(t/delta_t))+1, True)


# We can define constants for everything that doesn't change, particularly  G*m1, G*m2, G*m3

constant_m1 = G*m1
constant_m2 = G*m2
constant_m3 = G*m3

# 4th order runge-kutte method for velocity, and position

def avg_slope(k_1, k_2, k_3, k_4):
	return (k_1 + 2*k_2 + 2*k_3 + k_4)/6

def odesystem_vel(const_1,const_2,posofmass,position_1,position_2):
	return (const_1/((alg.norm(np.subtract(position_1,posofmass)))**3))*np.subtract(position_1,posofmass)+(const_2/((alg.norm(np.subtract(position_2,posofmass)))**3))*np.subtract(position_2,posofmass)


cur_col = 0
speed_probe = []
for i in time_array:
	cur_pos_1 = positions_1[0:3,cur_col]
	cur_pos_2 = positions_2[0:3,cur_col]
	cur_pos_3 = positions_3[0:3,cur_col]
	cur_vel_1 = velocities_1[0:3,cur_col]
	cur_vel_2 = velocities_2[0:3,cur_col]
	cur_vel_3 = velocities_3[0:3,cur_col] 
	cur_probe_speed = alg.norm(cur_vel_3)
	speed_probe.append(cur_probe_speed)
	if (alg.norm(np.subtract(cur_pos_3,cur_pos_2)))<= 6.9e7:
		print("Oops looks like Voyager crashed into Jupiter")
		sys.exit()
	# Finding estimated accelerations (k1s) for the three objects
	a_1_1 = odesystem_vel(constant_m2, constant_m3,cur_pos_1,cur_pos_2,cur_pos_3)
	a_1_2 = odesystem_vel(constant_m1, constant_m3,cur_pos_2,cur_pos_1,cur_pos_3)
	a_1_3 = odesystem_vel(constant_m1, constant_m2,cur_pos_3,cur_pos_1,cur_pos_2)
	# Estimating x based on our first approximation of acceleration, k1 in the usual equation for a fourth order Runge-Kutte Method
	new_vel_est_1 = cur_vel_1 + a_1_1*(delta_t/2)
	new_vel_est_2 = cur_vel_2 + a_1_2*(delta_t/2)
	new_vel_est_3 = cur_vel_3 + a_1_3*(delta_t/2)
	new_pos_est_1 = cur_pos_1 + new_vel_est_1*(delta_t/2)
	new_pos_est_2 = cur_pos_2 + new_vel_est_2*(delta_t/2)
	new_pos_est_3 = cur_pos_3 + new_vel_est_3*(delta_t/2)
	# Finding other estimated accelerations (k2s) for the three objects
	a_2_1 = odesystem_vel(constant_m2, constant_m3, new_pos_est_1, new_pos_est_2, new_pos_est_3)
	a_2_2 = odesystem_vel(constant_m1,constant_m3, new_pos_est_2, new_pos_est_1, new_pos_est_3)
	a_2_3 = odesystem_vel(constant_m1, constant_m2, new_pos_est_3, new_pos_est_1, new_pos_est_2)
	# Estimating x based on our second approximation of acceleration, k2 in the usual equation for a fourth order Runge-Kutte Method
	new_vel_est_1 = cur_vel_1 + a_2_1*(delta_t/2)
	new_vel_est_2 = cur_vel_2 + a_2_2*(delta_t/2)
	new_vel_est_3 = cur_vel_3 + a_2_3*(delta_t/2)
	new_pos_est_1 = cur_pos_1 + new_vel_est_1*(delta_t/2)
	new_pos_est_2 = cur_pos_2 + new_vel_est_2*(delta_t/2)
	new_pos_est_3 = cur_pos_3 + new_vel_est_3*(delta_t/2)
	# Finding other estimated accelerations (k3s) for the three objects
	a_3_1 = odesystem_vel(constant_m2, constant_m3, new_pos_est_1, new_pos_est_2, new_pos_est_3)
	a_3_2 = odesystem_vel(constant_m1,constant_m3, new_pos_est_2, new_pos_est_1, new_pos_est_3)
	a_3_3 = odesystem_vel(constant_m1, constant_m2, new_pos_est_3, new_pos_est_1, new_pos_est_2)
	# Estimating x based on our third approximation of acceleration, k3 in the usual equation for a fourth order Runge-Kutte Method 
	new_vel_est_1 = cur_vel_1 + a_3_1*(delta_t)
	new_vel_est_2 = cur_vel_2 + a_3_2*(delta_t)
	new_vel_est_3 = cur_vel_3 + a_3_3*(delta_t)
	new_pos_est_1 = cur_pos_1 + new_vel_est_1*(delta_t)
	new_pos_est_2 = cur_pos_2 + new_vel_est_2*(delta_t)
	new_pos_est_3 = cur_pos_3 + new_vel_est_3*(delta_t)
	# Finding other estimated accelerations (k4s) for the three objects
	a_4_1 = odesystem_vel(constant_m2, constant_m3, new_pos_est_1, new_pos_est_2, new_pos_est_3)
	a_4_2 = odesystem_vel(constant_m1,constant_m3, new_pos_est_2, new_pos_est_1, new_pos_est_3)
	a_4_3 = odesystem_vel(constant_m1, constant_m2, new_pos_est_3, new_pos_est_1, new_pos_est_2)
	# Determining new positions using weighted average of the Runge-Kutte Method
	new_vel_1 = cur_vel_1+avg_slope(a_1_1, a_2_1,a_3_1, a_4_1)*delta_t
	new_vel_2 = cur_vel_2+avg_slope(a_1_2, a_2_2,a_3_2, a_4_2)*delta_t
	new_vel_3 = cur_vel_3+avg_slope(a_1_3, a_2_3,a_3_3, a_4_3)*delta_t
	new_pos_1 = cur_pos_1 + new_vel_1 * delta_t
	new_pos_2 = cur_pos_2 + new_vel_2 * delta_t
	new_pos_3 = cur_pos_3 + new_vel_3 * delta_t
	current_com = m1*(cur_pos_1) + m2*(cur_pos_2)+m3*(cur_pos_3)
	current_com
	cur_col += 1
	velocities_1[0:3,cur_col] = new_vel_1
	velocities_2[0:3,cur_col] = new_vel_2
	velocities_3[0:3,cur_col] = new_vel_3
	positions_1[0:3,cur_col] = new_pos_1
	positions_2[0:3,cur_col] = new_pos_2
	positions_3[0:3,cur_col] = new_pos_3
	accelerations_1[0:3, cur_col-1] = avg_slope(a_1_1, a_2_1,a_3_1, a_4_1)
	accelerations_2[0:3, cur_col-1] = avg_slope(a_1_2, a_2_2,a_3_2, a_4_2)
	accelerations_3[0:3, cur_col-1] = avg_slope(a_1_3, a_2_3,a_3_3, a_4_3)
	curr_diff = alg.norm(np.subtract(new_pos_3, new_pos_2))
	print(curr_diff)
	print(initial_diff)
	if curr_diff > initial_diff: # The for loop stops when the current difference in position is bigger than the inital difference, as requested. 
		break
t = cur_col*delta_t
time_array = np.linspace(0, t, cur_col, True)

#Plotting the motion of voyager
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
plot_mass_2_1, = ax.plot(positions_2[0, :cur_col], positions_2[1, :cur_col], positions_2[2, :cur_col], label="Jupiter", linewidth=1.0, color = '#66b3ff', alpha=0.9)
plot_mass_3_1, = ax.plot(positions_3[0, :cur_col], positions_3[1, :cur_col], positions_3[2, :cur_col], label="Voyager", linewidth=1.0, color = '#99ff99', alpha=0.9)
plot_mass_2_2, = ax.plot(positions_2[0, :cur_col], positions_2[1, :cur_col], positions_2[2, :cur_col], 'o', color = '#66b3ff', alpha=0.9)
plot_mass_3_2, = ax.plot(positions_3[0, :cur_col], positions_3[1, :cur_col], positions_3[2, :cur_col], 'o', color = '#99ff99', alpha=0.9)
fig.legend()
ax.set_title("Figure 5a: Voyager's Slingshot around Jupiter", font = cm)
ax.set_xlabel("x (m)", font = cm)
ax.set_ylabel("y (m)", font = cm)
ax.set_zticks([])


def update(frame):
	ax.view_init(azim = -90, elev = 90)
	cur_frame_ind = int(((t/delta_t)/frames)*frame)
	next_ind = int(((t/delta_t)/frames)*frame)+1
	point_2 = plot_mass_2_2.set_data_3d(positions_2[0,cur_frame_ind:next_ind], positions_2[1,cur_frame_ind:next_ind],positions_2[2,cur_frame_ind:next_ind])
	point_3 = plot_mass_3_2.set_data_3d(positions_3[0,cur_frame_ind:next_ind], positions_3[1,cur_frame_ind:next_ind],positions_3[2,cur_frame_ind:next_ind])
	line_2 = plot_mass_2_1.set_data_3d(positions_2[0,cur_frame_ind-3500:cur_frame_ind], positions_2[1,cur_frame_ind-3500:cur_frame_ind],positions_2[2,cur_frame_ind-3500:cur_frame_ind])
	line_3 = plot_mass_3_1.set_data_3d(positions_3[0,cur_frame_ind-3500:cur_frame_ind], positions_3[1,cur_frame_ind-3500:cur_frame_ind],positions_3[2,cur_frame_ind-3500:cur_frame_ind])
	return line_2, line_3, point_2, point_3

ani = animation.FuncAnimation(fig, update,frames)

ani.save("Q4 (P36): Jupiter Slingshot.gif", fps = 120)
plt.show()


#Plotting the speed of voyager

fig_1 = plt.figure()
plt.plot(time_array, speed_probe)
plt.title("Figure 5a: The speed of voyager, over time, in the case of success", font = cm)
plt.xlabel("Time (s)", font = cm)
plt.ylabel("Speed (m/s)", font = cm)
plt.yticks(np.linspace(0,40e3, 5, True),font = cm)
plt.xticks(np.linspace(0,3e5,4, True),font = cm)
plt.savefig("Q4 (P36) Speed Increse Plot.svg")

plt.show()	

print("The speed of the probe is", speed_probe[-1]-speed_probe[0])
print("The number of days is", time_array[-1]/86400)