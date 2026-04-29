class Liquid:  # создаю клас
    def __init__(self, name, density):  # в конструктор передаю название и плотность
        self._name = name  # сохраняю название жидкости
        self._density = density  # сохраняю плотность жидкости

    def edit_density(self, density):  # метод для изменения плотности
        self._density = density  # записываю новую плотность

    def calc_v(self, m):  #считает объем по масе
        return m / self._density  # массу делю на плотность

    def calc_m(self, v):  # метод считает массу по объему
        return v * self._density  # объем умножаю на плотность

    def print_info(self):  # метод выводит информацию о жидкости
        print(f"Жидкость: '{self._name}' (плотность = {self._density} kg/m^3).")  # печатаю информацию


class Alcohol(Liquid):  # создаю класс для спирта
    def __init__(self, name, density, strength):  # сюда передаю название, плотность и крепость
        super().__init__(name, density)  # название и плотность беру из родительского класса
        self._strength = strength  # отдельно сохраняю крепость

    def edit_strength(self, strength):  # метод для изменения крепости
        self._strength = strength  # записываю новую крепость

    def print_strength(self):  # метод выводит крепость
        print(self._strength)  # печатаю крепость


q = Liquid("Wine", 1064.2)  # создаю объект жидкости
q.print_info()  # вывожу первую информацию о жидкости
q.edit_density(1000)  # меняю плотность
q.print_info()  # снова вывожу информацию

print("*"*20)  #

print(f"Вес 0.5 м^3 of Wine составляет {q.calc_m(0.5):.1f} кг.")  # считаю массу по объему
print(f"Объем 300 кг Wine равен {q.calc_v(300):.1f} м^3.")  # считаю объем по массе

print("*"*20)  #

a = Alcohol("Spirit", 789, 14)  # спирт
a.print_strength()  # вывожу первую
a.edit_strength(20)  # меняю 
a.print_strength()  # вывожу новую 
