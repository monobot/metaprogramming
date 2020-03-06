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


class R2D(Computer, Robot):
    @classmethod
    def compute(cls):
        return f'Bli pi blibli pipi! {super().compute()}'


class KSerie(Robot, Computer):
    @classmethod
    def compute(cls):
        return f'Yes sir! {super().compute()}'


r2d2 = R2D
k2so = KSerie
