import scipy.integrate as integrate
import scipy.special as special
import math as m

def angleFind(vec1,vec2):
    dot_vec1_vec2 = vec1[0]*vec2[0]+vec1[1]*vec2[1]+vec1[2]*vec2[2]
    mag_vec1 = (vec1[0]**2+vec1[1]**2+vec1[2]**2)**(0.5)
    mag_vec2 = (vec2[0]**2+vec2[1]**2+vec2[2]**2)**(0.5)
    return m.acos((dot_vec1_vec2)/(mag_vec1*mag_vec2)) 

def magnitude(vector):
    return (vector[0]*vector[0]+vector[1]*vector[1]+vector[2]*vector[2])**.5

def dot_product(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]

class Particle:
    def __init__(self, mass, charge, velocity, position):
        self.mass = mass
        self.charge = charge
        self.velocity = velocity
        self.position = position

    def MagneticForce(self, angle, Bfield):
        return self.charge*self.velocity*Bfield*m.sin(angle)
    
    def update(self, force, timestep):
        accel = force/self.mass
        self.velocity += accel*timestep
        self.position += self.velocity*timestep+.5*accel*timestep**2 

class B_Line_Source:
    def __init__(self, unit_mass, charge, current, velocity, position, direction, length):
        self.unit_mass = unit_mass
        self.charge = charge
        self.velocity = velocity
        self.position = position
        self.direction = direction/magnitude(direction)
        self.current = current 
        self.length = length

    def B_Integral(self, particle_pos):
        R = magnitude((particle_pos-self.position))*m.sin(m.acos(dot_product(self.direction,(particle_pos-self.position))/(magnitude(particle_pos)*magnitude(self.position)))) # this is too narrow and should be re-defined 
        return 1/(4*m.pi)*integrate.quad(lambda x: R/(x**2+particle_pos+R^2), 0, self.length/2)


p1 = Particle(1, 1, (1,0,0), (0,1,0))
l1 = B_Line_Source(1, 1, 1, (0,0,0), (0,0,0), (0,1,0), 1)

time = 0
timestep = 1
while time < 100:
    theta = angleFind(p1.position, #filler)
    p1.MagneticForce(theta)
    #do main loop
    time += timestep






#result = integrate.quad(lambda x: x**2, 0, 1)
#print(result[0], "with",result[1],"error")

