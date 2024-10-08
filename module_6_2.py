class Vehicle:
    __COLOR_VARIANTS = ["Красный", "Синий", "Зеленый", "Черный", "Белый"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

        if color not in Vehicle.__COLOR_VARIANTS:
            raise ValueError(f"{color} не является допустимым цветом. Выберите один из: {Vehicle.__COLOR_VARIANTS}")

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            raise ValueError(f"{new_color} не является допустимым цветом. Выберите один из: {Vehicle.__COLOR_VARIANTS}")


class Sedan(Vehicle):
    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)


# Пример использования:
try:
    my_sedan = Sedan("Иван", "Toyota Camry", 150, "Красный")
    my_sedan.print_info()

    print("\nИзменяем цвет на Синий:")
    my_sedan.set_color("Синий")
    my_sedan.print_info()

    print("\nПопытка установить недопустимый цвет:")
    my_sedan.set_color("Желтый")  
except ValueError as e:
    print(e)