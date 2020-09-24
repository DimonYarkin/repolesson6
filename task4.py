class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Старт машины {self.name}'

    def stop(self):
        return f'Машина {self.name} остановлена'

    def turn_right(self):
        return f'Машина {self.name} повернула на право'

    def turn_left(self):
        return f'Машина повернула {self.name} на лево'

    def show_speed(self):
        return f'Скорость машины {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f' Текущая скорость городской машины {self.name} составляем {self.speed}')

        if self.speed > 60:
            return f'Машина {self.name} привысела скорость органичение 40 км/ч'
        else:
            return f'Машина {self.name} едет с нормальной скоростью'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Машина {self.name} привысила скорость ограниечение 60 км/ч'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Машина {self.name} полиции'
        else:
            return f'Машина {self.name} не принадлежит полиции'


audi = SportCar(100, 'Red', 'Audi', False)
Mazda = TownCar(30, 'White', 'Mazda', False)
lada = WorkCar(70, 'Rose', 'Lada', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(f"Путь спорт кара {audi.name} цвета {audi.color} ")
print(f"{audi.go()} : {audi.show_speed()} \n{audi.turn_left()} \n{audi.turn_right()} \n{audi.stop()}")