def repeat(count):
    def decorator(func):
        def wrapper():
            for _ in range(count):
                func()

        return wrapper

    return decorator


@repeat(3)
def say_hi():
    print("Hi")


say_hi()


def multiply_by_two(func):
    def wrapper(a, b):
        return func(a, b) * 2

    return wrapper


@multiply_by_two
def add_numbers(a, b):
    return a + b


print(add_numbers(2, 3))


is_admin = False


def admin_required(func):
    def wrapper():
        if is_admin:
            func()
        else:
            print("Доступ запрещен!")

    return wrapper


@admin_required
def hello_world():
    print("Hello World")


hello_world()
is_admin = True
hello_world()


def show_messages(func):
    def wrapper():
        print("Начало")
        func()
        print("Конец")

    return wrapper


@show_messages
def greet():
    print("Привет!")


greet()
