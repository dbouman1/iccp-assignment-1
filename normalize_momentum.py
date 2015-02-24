## Import libraries
import numpy as np
## Define function
def normalize_momentum(N,velocity,T):
	kb = 1.38*np.power(10,-23)
	total_velocity = np.zeros(velocity.shape,dtype=float)
	## Normalize velocities
	total_velocity[:,0] = sum(velocity[:,0])
	total_velocity[:,1] = sum(velocity[:,1])
	total_velocity[:,2] = sum(velocity[:,2])
	velocity[:,0] = velocity[:,0]-total_velocity[:,0]/N
	velocity[:,1] = velocity[:,1]-total_velocity[:,1]/N
	velocity[:,2] = velocity[:,2]-total_velocity[:,2]/N

	#rescaling_factor = np.sqrt((3*(N-1)*kb*T)/(sum(sum(np.array(velocity)**2))))
	rescaling_factor = 1
	velocity = rescaling_factor*velocity

	return velocity;