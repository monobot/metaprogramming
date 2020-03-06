class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class Trooper(Human):

    def __repr__(self):
        return f'trooper {super().__repr__()}'


conn_ctor = Human('Conn ctor')
pein_hado = Trooper('Pein Hado')
