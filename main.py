import random

class Environment(object):
    def __init__(self):
        self.location = ['a', 'b', 'c', 'd']
        self.mode = ['t', 'l'] # represents modes of cleaning, thorough or light
        self.location_condition = {'a' : '0',
                                   'b' : '0',
                                   'c' : '0',
                                   'd' : '0'}
        self.cleaning_method = {'a' : 't',
                                'b' : 't',
                                'c' : 't',
                                'd' : 't'}
        self.vacuum_location = random.choice(self.location) # pick a random location
        self.location_condition['a'] = random.randint(0, 1)
        self.location_condition['b'] = random.randint(0, 1)
        self.location_condition['c'] = random.randint(0, 1)
        self.location_condition['d'] = random.randint(0, 1)
        self.cleaning_method['a'] = random.choice(self.mode) # pick a random cleaning method
        self.cleaning_method['b'] = random.choice(self.mode)
        self.cleaning_method['c'] = random.choice(self.mode)
        self.cleaning_method['d'] = random.choice(self.mode)