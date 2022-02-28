class City:
    """Class for City object. Attributes:
    -City ID
    -X coordinate
    -Y coordinate
    -Z value for Particle Swarm Optimization
    """
    def __init__(self, city_id, x, y):
        self.__city_id = city_id
        self.__x = x
        self.__y = y
        self.z = city_id  # particle swarm optimization parameter

    def __str__(self):
        return self.__city_id

    def __repr__(self):
        return self.__city_id

    def __eq__(self, other):
        return self.__city_id == other.__city_id

    def __lt__(self, other):
        return self.z < other.z

    def __sub__(self, other):
        self.z -= other.z
        return self

    def __add__(self, other):
        self.z += other.z
        return self

    def scale(self, scalar):
        """Scales the City's z parameter with the given scalar value."""
        self.z = self.z * scalar
        return self

    def get_city_id(self):
        return self.__city_id

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def distance(self, other):
        """Calculates the Euclidean distance between two cities."""
        return round(((self.__x - other.__x) ** 2 + (self.__y - other.__y) ** 2) ** (1/2))
