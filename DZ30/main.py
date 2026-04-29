class Student:  # делаю класс для студента
    def __init__(self, name):  # сюда передаю имя
        self.name = name  # сохраняю имя
        self.notebook = self.Notebook()  # тут создаю ноутбук

    def show(self):  # метод для вывода всей информации
        print(self.name, "=>", end=" ")  # сначала вывожу имя
        self.notebook.show()  # потом вызываю метод вложенного класса

    class Notebook:  #класс для ноутбука
        def __init__(self):  # конструктор ноутбука
            self.model = "HP"  # модель ноутбука
            self.processor = "i7"  # процессор ноутбука
            self.memory = "16"  # память ноутбука

        def show(self):  # отдельный метод для вывода ноутбука
            print(self.model + ",", self.processor + ",", self.memory)  # вывожу все данные о ноутбуке


student1 = Student("Roman")  # перввй студента
student1.show()  # показываю данные первого студента

student2 = Student("Vladimir")  # второй студент
student2.show()  # показываю данные второго студента
