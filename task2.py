class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class MassCount(Road):
    def __init__(self, _length, _width, weight_of_asphalt, coating_thickness):
        super().__init__(_length, _width)
        self.weight_of_asphalt = weight_of_asphalt
        self.coating_thickness = coating_thickness

    def mass(self):
        return self._length * self._width * self.weight_of_asphalt * self.coating_thickness/1000


MassClass = MassCount(20, 5000, 25, 5)
print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна {MassClass.mass()} т.")
