import scipy.integrate as integrate
import scipy.special as special
import math as m
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt




def Harmonic_Oscillator(position, velocity, k, a):
    return -position*k -velocity*a



class Particle:
    def __init__(self, mass, charge, position, velocity):
        self.mass = mass
        self.charge = charge
        self.position = position
        self.velocity = velocity
        
    def MagneticForce(self, angle, Bfield):
        return self.charge*self.velocity*Bfield*m.sin(angle)
    
    def update(self, force, timestep):
        accel = force/self.mass
        self.velocity += accel*timestep
        self.position += self.velocity*timestep+.5*accel*timestep**2 



p1 = Particle(1, 1, np.array([1.,1.,1.]), np.array([-1.,1.,0.]))

time = 0 
timestep = .1
xpos = []
ypos = []
zpos = []



while time < 100:
    p1.update(Harmonic_Oscillator(p1.position, p1.velocity, 1, .25), timestep)

    xpos.append(p1.position[0])
    ypos.append(p1.position[1])
    zpos.append(p1.position[2])
    time += timestep

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xpos, ypos, zpos,c=xpos, cmap='Greens')
plt.show()





#result = integrate.quad(lambda x: x**2, 0, 1)
#print(result[0], "with",result[1],"error")

