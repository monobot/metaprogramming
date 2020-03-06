class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'


class Trooper(Human):
    def register_to_squad(self, squad):
        print(f'... registering {self} to squad {squad.name}')

    def __repr__(self):
        return f'trooper {super().__repr__()}'


class Jedi(Trooper):

    def __init__(self, name, jedi_name):
        self.name = name
        self.jedi_name = jedi_name

    def __repr__(self):
        return f'{self.jedi_name} disguised as {super().__repr__()}'


class Computer:
    is_evil = False

    @staticmethod
    def compute():
        return 'calculating'


class Robot:
    is_evil = True

    @staticmethod
    def compute():
        return 'conquer the world!'


class KSerie(Robot, Computer):
    owner = None

    @classmethod
    def compute(cls):
        return f'Yes sir! {super().compute()}'


class SquadMeta(type):

    def __init__(cls_meta, name, bases, properties):
        for property in properties.values():
            if isinstance(property, Trooper):
                property.register_to_squad(cls_meta)

        meta_configuration = properties.get('Meta', cls_meta.Meta)
        kserie = properties.get('kserie')
        if meta_configuration and kserie:
            kserie.owner = getattr(meta_configuration, 'owner', None)


class Squad(metaclass=SquadMeta):
    owner = None

    class Meta:
        owner = Human('Darth Civicus')


class SquadDeathStar(Squad):
    name = 'Death Star'
    squad_leader = Trooper('Clone 026235')
    trooper_1 = Trooper('Clone 013568')
    trooper_2 = Trooper('Clone 323492')
    trooper_3 = Trooper('Clone 924254')
    trooper_4 = Trooper('Clone 252379')
    trooper_5 = Trooper('Clone 899248')
    trooper_6 = Trooper('Clone 824445')
    trooper_7 = Trooper('Clone 541258')
    trooper_8 = Trooper('Clone 625557')
    kserie = KSerie()


class SquadTatooine(Squad):
    name = 'Death Star'
    squad_leader = Trooper('Clone 026235')
    trooper_1 = Trooper('Clone 013568')
    trooper_2 = Trooper('Clone 323492')
    trooper_3 = Trooper('Clone 924254')
    trooper_4 = Trooper('Clone 252379')
    trooper_5 = Trooper('Clone 899248')
    trooper_6 = Jedi('Clone 824445', 'Ju Ankee No-Palmtri')
    trooper_7 = Trooper('Clone 541258')
    trooper_8 = Trooper('Clone 625557')
    kserie = KSerie()

    class Meta:
        owner = Human('Wankee Deking')


death_star = SquadDeathStar()
tatooine = SquadTatooine()

trooper = tatooine.trooper_1
jedi = tatooine.trooper_6

kserie_ds = death_star.kserie
kserie_t = tatooine.kserie

print(f'THE OWNER OF KSERIE DeathStar IS {kserie_ds.owner}')
print(f'THE OWNER OF KSERIE Tatooine IS {kserie_t.owner}')
