import random
import time

class Performance:
    def __init__(self):
        self.score = 0
        self.visits = 0
        self.timestamp = 0

    def Display_Score(self):
        print('Score:', self.score)
        p = (self.score / self.visits) * 100
        print('Performance Score:', p, '%')
        return p

class Environment(object):
    def __init__(self):
        self.locationCondition = {'a': '0',
                                  'b': '0',
                                  'c': '0',
                                  'd': '0'}
        # randomize conditions
        self.locationCondition['a'] = random.randint(0, 1)
        self.locationCondition['b'] = random.randint(0, 1)
        self.locationCondition['c'] = random.randint(0, 1)
        self.locationCondition['d'] = random.randint(0, 1)

        # instantiate locations
        self.Location = ['a', 'b', 'c', 'd']
        self.vacuumLocation = random.choice(self.Location)

class MyAgent(Environment, Performance):
    def __init__(self, Environment, Performance):
        Performance.timestamp = Performance.timestamp + 1
        # Status before visit
        print('Vacuum is at Gate: ', Environment.vacuumLocation)
        print('Location condition before visit', Environment.locationCondition, 'at timestamp',
              Performance.timestamp)
        count = 0
        while count < 4:
            if Environment.locationCondition[Environment.vacuumLocation] == 1:
                Environment.locationCondition[Environment.vacuumLocation] = 0
                print('Gate:', Environment.vacuumLocation, 'has been Cleaned.')

                Performance.score = Performance.score + 1
            else:
                print('Boarding Gate:', Environment.vacuumLocation, 'is already clean.')
            newIndex = Environment.Location.index(Environment.vacuumLocation) + 1
            if newIndex == 4:
                newIndex = 0
            Environment.vacuumLocation = Environment.Location[newIndex]
            count += 1
            Performance.visits = Performance.visits + 1
        # Status after visit
        print('Environment Condition after visit ', Environment.locationCondition, 'at timestamp',
              Performance.timestamp)
        print()

x = 0
theScore = Performance()
timeinterval = 2  # simulates 2 hour interval
while x < 12:
    theEnvironment = Environment()
    theVacuum = MyAgent(theEnvironment, theScore)
    if x == 6:  # halfway through monitor performance/correct to 5
        p = theScore.Display_Score()
        if p > 50:
            print('Increasing visits and intervals')
            timeinterval = 1
            x = 0
        else:
            print('Reducing visits and intervals')
            timeinterval = 3
            x = x + 3
    time.sleep(timeinterval)
    x = x + 1
    theScore.Display_Score()
