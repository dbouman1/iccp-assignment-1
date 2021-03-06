"""
The velocity_verlet implements the standard velocity verlet algorithm to integrate the equations of motion.
The acceleration is calculated in a seperate function.

N           : amount of particles
h           : time step
pos         : array of size 3N, which contains the position in the x,y,z direction for each particle
v_0         : array of size 3N of the current velocities
a_0         : array of size 3N of the current accelerations
L           : length of the box
cutoff      : cutoff length for interaction
hist_bins   : The 'bins' where we divide our distances in to calculate the correlation function
"""
# Import libraries
import numpy as np
# Import functions
from acceleration import acceleration
from diffusion_constant import diffusion_constant
# Define velocity verlet function
def velocity_verlet(N, h, pos, v_0, a_0, L,cutoff, hist_bins):
    v_half_h = np.add(v_0,0.5*a_0*h)
    pos_h = np.add(pos,v_half_h*h)
    
    # Impose periodic boundary condition
    pos_h = np.where(pos_h<0,L+pos_h,pos_h)             # If particle has a position smaller than 0, add L
    pos_h = np.where(pos_h>L, pos_h-L, pos_h)           # If particle has a position larger than L, subtract L

    a_h,potential,virial,dist_hist = acceleration(N, pos_h, L, cutoff, hist_bins)
    v_h = np.add(v_half_h,(0.5*a_h*h))

    # Calculate diffusion constant from the displacement
    D = diffusion_constant(v_half_h,h,L)

    # Update acceleration, position and velocity to new values
    a_0 = a_h
    pos = pos_h
    v_0 = v_h

    return pos,v_0,a_0,potential,virial,dist_hist,D;