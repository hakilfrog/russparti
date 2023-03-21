class ElevatorState:
    def __init__(self, elevator):
        self.elevator = elevator

    def get_state(self):
        raise NotImplementedError
    # def enter(self, weight):  # писал это сначала, но сейчас не требуется (вроде)
    #     pass
    #
    # def exit(self, weight):
    #     pass
    #
    # def go_up(self):
    #     pass
    #
    # def go_down(self):
    #     pass


class EmptyState(ElevatorState):
    def enter(self, weight):
        self.elevator.current_weight = weight
        self.elevator.state = OccupiedState(self.elevator)

    def exit(self, ):
        print("Лифт пуст")

    def go_up(self):
        print("Лифт на самом высоком этаже")

    def go_down(self):
        print("Лифт на самом нижнем этаже")

    def get_state(self):
        return 'Ожидание...'


class OccupiedState(ElevatorState):
    def enter(self, weight):
        if self.elevator.current_weight + weight > self.elevator.max_weight:
            print("Перевес!")
            return False

        elif self.elevator.current_weight + weight < self.elevator.min_weight:
            print("Лифт пуст")
            return False
        else:
            self.elevator.current_weight += weight
            return True

    def exit(self, weight):
        self.elevator.current_weight -= weight
        if self.elevator.current_weight == 0:
            self.elevator.state = EmptyState(self.elevator)

    def go_up(self):
        if self.elevator.current_floor == self.elevator.max_floor:
            print("Выше некуда")
        else:
            self.elevator.current_floor += 1

    def go_down(self):
        if self.elevator.current_floor == self.elevator.min_floor:
            print("Ниже некуда")
        else:
            self.elevator.current_floor -= 1

    def get_state(self):
        return "Занято"


class Elevator:
    def __init__(self, min_weight, max_weight, min_floor=0, max_floor=3):
        self.max_weight = max_weight
        self.min_weight = min_weight
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_weight = 0
        self.current_floor = 0
        self.state = EmptyState(self)

    def enter(self, weight):
        self.state.enter(weight)
        print("Текущий вес:", elevator.current_weight)

    def exit(self, weight):
        self.state.exit(weight)
        print("Текущий вес:", elevator.current_weight)

    def go_up(self):
        self.state.go_up()
        print("Текуций этаж:", elevator.current_floor)

    def go_down(self):
        self.state.go_down()
        print("Текущий этаж:", elevator.current_floor)

    def get_state(self):
        return self.state.get_state()


#######################################################

elevator = Elevator(min_weight=10, max_weight=500)

#####################################################
print(elevator.get_state())
elevator.enter(0)  # вход тела
# print("Текущий вес:", elevator.current_weight) # выводим вес
# print("Current state:",
#       type(elevator.state).__name__)  # почему выводится блять OccupiedState и че с ним делать (наполнение) ????
print(elevator.get_state())

elevator.go_up()
# print("Текущий этаж:", elevator.current_floor)  # 1 этаж
print(elevator.get_state())
elevator.go_up()
# print("Текущий этаж:", elevator.current_floor)  # 2 этаж

elevator.go_up()
# print("Текущий этаж:", elevator.current_floor)  # 3 этаж


elevator.go_up()
# print("Текущий этаж:", elevator.current_floor)  # а выше не получается да?
print(elevator.get_state())

elevator.go_down()
# print("Текущий этаж:", elevator.current_floor)  # спускаемся вниз

elevator.exit(0)
# print("Текущий вес:", elevator.current_weight)  # выход тела
print(elevator.get_state())
print("Current state:",
      type(elevator.state).__name__)  # да как сделать так, чтобы выводилось не имя класса сука сам сука

print("Current state:", )
