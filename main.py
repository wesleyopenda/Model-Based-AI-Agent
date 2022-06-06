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

class Agent(Environment): # to link the agent to the environment
    def __init__(self, Environment): # inherits constructors from the Environment class
        # To find out the location of the vacuum and the condition of where it is
        print('Vacuum location', Environment.vacuum_location)
        print('Location condition', Environment.location_condition)
        print('Cleaning Method', Environment.cleaning_method)
        count = 0 # makes it loop and not go out of range
        while count < 4:
            if Environment.location_condition[Environment.vacuum_location] == 1:
                if Environment.cleaning_method[Environment.vacuum_location] == 'l': # if location was cleaned lightly before, clean it thoroughly now
                    Environment.cleaning_method[Environment.vacuum_location] = 't'
                else:
                    Environment.cleaning_method[Environment.vacuum_location] = 'l'
                Environment.location_condition[Environment.vacuum_location] = 0
                print('Location ', Environment.vacuum_location ,'cleaned')
            else:
                print('Location', Environment.vacuum_location,' is already clean')

            new_index = Environment.location.index(Environment.vacuum_location) + 1 # read index from dict and added 1 to it
            if new_index == 4:
                new_index = 0

            Environment.vacuum_location = Environment.location[new_index] # moves the vacuum to the new location
            count += 1
        print('finished cleaning :-)')
        print('New conditions: ', Environment.location_condition, 'Cleaning Method', Environment.cleaning_method)

# object creation
count = 0
The_environment = Environment()
# clean more than once
while count < 10:
    print()
    print('----------Run', count+1, '--------------')
    print()
    The_environment.location_condition['a'] = random.randint(0, 1)
    The_environment.location_condition['b'] = random.randint(0, 1)
    The_environment.location_condition['c'] = random.randint(0, 1)
    The_environment.location_condition['d'] = random.randint(0, 1)
    The_agent = Agent(The_environment)
    count += 1