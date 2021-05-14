import scipy.integrate as integrate
import scipy.special as special
import math as m
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def path_func(x,y,z):
    return np.array([m.cos(50*z),m.sin(50*z),z])

def vector_correct(position, input_vector):
    corrected_vector = []
    for i in position:
        corrected_vector.append(i)
    for j in input_vector:
        corrected_vector.append(j)
    return corrected_vector

def Bfield(position, line_direction, line_position):
    current = 1
    return current*np.cross(line_direction/np.linalg.norm(line_direction),((position-line_direction)/np.linalg.norm(position-line_direction)))/np.linalg.norm(position-line_position)**2
    

#line direction must be a unit vector
def descrete_integral(steps,start,end,function,position,line_direction,curve):
    out = 0
    for i in range(1,steps+1):
        out += function(position, line_direction, curve(0,0,start+(end-start)/steps*i)) #wrong
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



bound_range = 15

output_vectors = []
for i in range(bound_range):
    output_vectors.append(vector_correct([0,0,i], descrete_integral(500, 0., 6*m.pi, Bfield, [0,0,i], path_func(0,0,i+.001)-path_func(0,0,i),path_func))) #testing the line x^2


fig = plt.figure()

# draw vector
soa = np.array(output_vectors)

X, Y, Z, U, V, W = zip(*soa)
ax = fig.gca(projection='3d')

zline = np.linspace(0, 6*m.pi, 5000)
yline = np.sin(50*zline)
xline = np.cos(50*zline)


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



