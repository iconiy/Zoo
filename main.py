from datetime import *

class Animal:
    def __init__(self, name, species, height, diet):
        self.name = name
        self.species = species
        self.height = height
        self.diet = diet
        self.hungry = True

    def feed(self):
        today = date.today()
        print(f'{self.name} was given {self.diet}')
        print(f'{self.name} was fed {self.diet} on ' + str(today))
        self.hungry = False
        return today

    def hunger_habits(self):
        if self.hungry:
            Animal.feed(self)
        else:
            print(f'{self.name} is not hungry yet')

    def feed_schedule(self):

            print(f'{self.name} was last fed on {self.feed} and needs to be fed {date.today()}')


Alfred = Animal('Alfred', 'Lion', '5', 'meat')
Alfred.feed()
Alfred.feed_schedule()
Alfred.hunger_habits()