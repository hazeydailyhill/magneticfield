import scipy.integrate as integrate
import scipy.special as special
import math as m
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt



def vector_correct(position, input_vector):
    corrected_vector = []
    for i in position:
        corrected_vector.append(i)
    for j in input_vector:
        corrected_vector.append(j)
    return corrected_vector

def Bfield(position,line_direction, line_position):
    current = 1
    return current*np.cross(line_direction,(position/np.linalg.norm(position)))/np.linalg.norm(position-line_position)**2
    

#line direction must be a unit vector
def descrete_integral(steps,start,end,function,position,line_direction):
    out = 0
    for i in range(1,steps+1):
        out += function(position, line_direction, start+line_direction*(end-start)/steps)
    return out

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



p1 = Particle(1, 1, np.array([1.,0.,0.]), np.array([0.,0.,0.]))

time = 0 
timestep = .1

bound_range = 10

output_vectors = []
for i in range(bound_range):
    for k in range(bound_range):
        output_vectors.append(vector_correct([float(i-bound_range/2),0,float(k-bound_range/2)], descrete_integral(10, 0., 1., Bfield, [float(i-bound_range/2),0,float(k-bound_range/2)], np.array([0.,1.,0.]))))


fig = plt.figure()

# draw vector
soa = np.array(output_vectors)

X, Y, Z, U, V, W = zip(*soa)
ax = fig.gca(projection='3d')

yline = np.linspace(-1, 1, 100)
xline = yline*0
zline = 0

ax.plot3D(xline, yline, zline, 'gray')

ax.quiver(X, Y, Z, U, V, W, length=1, normalize=True)
ax.set_xlim([-50, 50])
ax.set_ylim([-50, 50])
ax.set_zlim([-50, 50])
ax.set_title("Vectors")


plt.show()

#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.scatter3D(xpos, ypos, zpos,c=xpos, cmap='Greens')
#plt.show()



