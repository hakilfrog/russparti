import time


class MaxErrorWeight(Exception):
    pass  # print("Error, incorrect weight")


class MinErrorWeight(Exception):
    pass  # print("Error, incorrect weight")


class ElevatorState:
    # weight = 0

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
        #try:
            self.elevator.current_weight = weight
            if self.elevator.current_weight > self.elevator.max_weight:
                raise MaxErrorWeight
            elif self.elevator.current_weight  < self.elevator.min_weight:
                print("Лифт пуст")
                self.elevator.state = EmptyState(self.elevator)
                raise MinErrorWeight
            else:
                self.elevator.state = OccupiedState(self.elevator)

        # except MaxErrorWeight:
        #     print("Перевес! Попробуйте ещё раз")
        #
        #
        # except MinErrorWeight:
        #     print("Недостаточный вес!")

    def exit(self, weight):
        if self.elevator.current_weight - weight < 0:
            raise MinErrorWeight
        else:
            self.elevator.current_weight -= weight
        print("Лифт пуст")

    def go_up(self):
        self.elevator.state = EmptyState(self.elevator)  # print("Лифт на самом высоком этаже")  # нахуя в эмти стайт это?

    def go_down(self):
        self.elevator.state = EmptyState(self.elevator)
        #  print("Лифт на самом нижнем этаже") # нахуя в эмти стайт это?

    def get_state(self):
        return 'Ожидание...'


class OccupiedState(ElevatorState):

    def enter(self, weight):
        self.elevator.current_weight += weight
        # self.weight += weight
        # if self.elevator.current_weight + weight > self.elevator.max_weight:
        #     print("Перевес!")
        #     self.elevator.state = EmptyState(self.elevator)
        #     raise ErrorWeight

            # return False

        # elif self.elevator.current_weight + weight < self.elevator.min_weight:
        #     print("Лифт пуст")
        #     self.elevator.state = EmptyState(self.elevator)
        #     raise ErrorWeight
        #
        # else:
        #     self.elevator.current_weight += weight

    def exit(self, weight):
        self.elevator.current_weight -= weight
        if self.elevator.current_weight == 0:
            self.elevator.state = EmptyState(self.elevator)

    def go_up(self, floor):
        if self.elevator.min_weight <= self.elevator.current_weight <= self.elevator.max_weight:
            if self.elevator.current_floor == self.elevator.max_floor:
                print("Выше некуда")
            else:
                self.elevator.current_floor += floor - self.elevator.current_floor
        # elif self.enter(elevator.current_weight):
        #     self.elevator.current_floor += 1 # ЭТО ЧТО ЗА ХУЙНЯ?

    def go_down(self, floor):
        if self.elevator.min_weight <= self.elevator.current_weight <= self.elevator.max_weight:
            if self.elevator.current_floor == self.elevator.min_floor:
                print("Ниже некуда")
            else:
                self.elevator.current_floor -= self.elevator.current_floor - floor

    def get_state(self):
        return "В пути с пассажиром"


class IncomingState(ElevatorState):

    def go_to_p(self, floor):
        if elevator.min_floor < floor < elevator.max_floor:
            if self.elevator.current_floor == floor:
                self.elevator.state = EmptyState(self.elevator)
            else:
                time.sleep(0.5)
                self.elevator.current_floor = floor
        else:
            raise ValueError


    def get_state(self):
        return "На пути к пассажиру"


class Elevator:
    def __init__(self, min_weight, max_weight, min_floor=0, max_floor=3):  # сука лист ['p', '1', '2', '3']
        self.max_weight = max_weight
        self.min_weight = min_weight
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_weight = 0
        self.current_floor = 0
        self.state = EmptyState(self)

    def enter(self, weight):
        self.state.enter(weight)
        print("Текущий вес:", elevator.current_weight)  # он разве не должен в ентер в состоянии вызываться???

    def exit(self, weight):
        self.state.exit(weight)
        print("Текущий вес:", elevator.current_weight)

    def go_up(self, floor):
        self.state.go_up(floor)
        time.sleep(0.5)
        print("Текущий этаж:", elevator.current_floor)

    def go_down(self, floor):
        self.state.go_down(floor)
        time.sleep(0.5)
        print("Текущий этаж:", elevator.current_floor)

    def get_state(self):
        return self.state.get_state()


#######################################################

elevator = Elevator(min_weight=10, max_weight=500)

#####################################################
print(elevator.get_state())
elevator.enter(420)  # вход тела
# print("Текущий вес:", elevator.current_weight) # выводим вес
# print("Current state:",
#       type(elevator.state).__name__)  # почему выводится блять OccupiedState и че с ним делать (наполнение) ????
print(elevator.get_state())

elevator.go_up(1)
# print("Текущий этаж:", elevator.current_floor)  # 1 этаж
print(elevator.get_state())
elevator.go_up(2)
# print("Текущий этаж:", elevator.current_floor)  # 2 этаж

elevator.go_up(3)
# print("Текущий этаж:", elevator.current_floor)  # 3 этаж


elevator.go_up(5)
# print("Текущий этаж:", elevator.current_floor) # а выше не получается да?
print(elevator.get_state())
elevator.exit(420)

elevator.enter(40)
elevator.go_down(1)
# print("Текущий этаж:", elevator.current_floor)  # спускаемся вниз

elevator.exit(40)
# print("Текущий вес:", elevator.current_weight)  # выход тела
print(elevator.get_state())
