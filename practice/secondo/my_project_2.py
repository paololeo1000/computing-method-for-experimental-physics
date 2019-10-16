import math

class Particle:
    """ Class describing a generic particle.
    """
    def __init__(self, mass, charge = 0, name = None, momentum = 0):
        """ Class constructor """
        self._mass = mass # in MeV/c^2
        self._charge = charge # in e
        self.name = name 
        self._momentum = momentum # in MeV/c


    def print_info(self):
        message = 'The Particle {} has: mass {} Mev/c^2, charge {} e, momentum {} MeV/c'
        print(message.format(self.name, self.mass, self.charge, self.momentum))
        
    @property
    def mass(self):
        return self._mass

    @property
    def charge(self):
        return self._charge

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, value):
        if (value < 0):
            print('Cannot set the momentum to a value inferior than zero.')
            print('The momentum will be set to zero!')
            self._momentum = 0.
        else:
            self._momentum = value

    @property
    def energy(self):
        return math.sqrt((self.momentum**2 + self.mass**2))

    @energy.setter
    def energy(self, value):
        if(value < self.mass):
            message = 'Cannot set the particle energy to a value smaller than its mass ({})!'
            print(message.format(self.mass))
            return
        self.momentum = math.sqrt(value**2 - self.mass**2)

    @property
    def beta(self):
        if not (self.energy > 0.):
            return 0
        else:
            return (self.momentum/self.energy)

    @beta.setter
    def beta(self, value):
        if (value < 0.) or (value > 1.):
            print('Beta must be in the [0., 1.] range')
            return
        if (not (value < 1.)) and (self.mass > 0.):
            print('Only massless particles can travel at Beta = 1!')
            return
        self.momentum = (value * self.mass)/(math.sqrt(1 - value**2))

    @property
    def gamma(self):
        if not ((self.beta > 0.) and (self.beta < 1.)):
            return 0
        else:
            return (1 / (math.sqrt(1 - self.beta**2)))

    @gamma.setter
    def gamma(self, value):
        if (value < 0.):
            print('Gamma must be positive!')
            return
        self.momentum = self.mass * (math.sqrt(value**2 - 1))


class Proton(Particle):
    """ Class describing a proton """
    MASS = 1.02
    CHARGE = 1.
    NAME = 'Proton'

    def __init__(self, momentum = 0.):
        Particle.__init__(self, self.MASS, self.CHARGE, self.NAME, momentum)
        
proton = Proton(200.)
proton.print_info()
proton.beta = 0.8
proton.print_info()

