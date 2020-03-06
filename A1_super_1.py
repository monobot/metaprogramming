class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def salutation(self):
        return 'Smile, hello I am a human being!\n'


class Trooper(Human):

    def __repr__(self):
        return f'trooper {self.name} reporting!!'

    def salutation(self):
        return f'On your command sir! {super().salutation()}'


class SpaceShipPilot(Trooper):

    def __repr__(self):
        return f'Pilot {self.name}!!'

    def salutation(self):
        return f'I will destroy everything! {super().salutation()}'


clone_bomber = SpaceShipPilot('clone 368948')
