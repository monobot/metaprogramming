class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class Computer:
    is_evil = False

    @staticmethod
    def compute():
        return 'calculating'


class Robot:
    is_evil = True
    owner = Human('Onemee Gab Arohn')

    @staticmethod
    def compute():
        return 'conquer the world!'


class KSerie(Robot, Computer):

    @classmethod
    def compute(cls):
        return f'Yes sir! {super().compute()}'


class K2(KSerie):
    pass


class K3(KSerie):
    pass


k2so = K2()
k3 = K3()

print(k2so.compute())
print(k3.compute())

print(f'k2so.is_evil {k2so.is_evil}')
print(f'k3.is_evil {k3.is_evil}')

print(f'k2so.owner {k2so.owner}')
print(f'k3.owner {k3.owner}')
