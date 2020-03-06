from math import sqrt


class PlanetCoordinates:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, destination):
        """Calculate the distance to other coordinates provided.

        :param destination: a destination we want to calculate the distance with
        :type destination: destination
        """
        x_delta = abs(self.x - destination.x)
        y_delta = abs(self.y - destination.y)
        return sqrt((x_delta ** 2) + (y_delta ** 2))


planet_a = PlanetCoordinates(0, 0)
planet_b = PlanetCoordinates(10, 10)
print(f'distance from a to b {planet_a.distance(planet_b)}')
print(f'distance from b to a {planet_b.distance(planet_a)}')
print(f'distance from a to a {planet_a.distance(planet_a)}')
print(f'distance from b to b {planet_b.distance(planet_b)}')
