class UOMember:
    def __init__(self, name):
        self.name = name

    def receive_notifications(self, message: str):
        print(f'UO Member {self.name} has received message: {message}')


class Police:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def send_message(self, message, obj=None):
        for observer in self.observers:
            if obj is None:
                observer.receive_notifications(message)
            elif type(observer) in obj:
                observer.receive_notifications(message)


class Student(UOMember):
    def __init__(self, name):
        super().__init__(name)

    def receive_notifications(self, message: str):
        print(f'UO Student {self.name} has received message: {message}')


class Faculty(UOMember):
    def __init__(self, name):
        super().__init__(name)

    def receive_notifications(self, message: str):
        print(f'UO Faculty {self.name} has received message: {message}')


class Staff(UOMember):
    def __init__(self, name):
        super().__init__(name)

    def receive_notifications(self, message: str):
        print(f'UO Staff {self.name} has received message: {message}')


if __name__ == '__main__':
    police = Police()

    police.register_observer(Student('John'))
    police.register_observer(Faculty('Mary'))
    police.register_observer(Staff('Bob'))

    print("Notifying all:")
    police.send_message('Police alert 1!')

    print("Notifying just students:")
    police.send_message('Police alert 2!', obj=[Student])

    print("Notifying faculty and staff:")
    police.send_message('Police alert 3!', obj=[Faculty, Staff])
