# lift # ponial
# мы не знаем что это такое если бы мы знали что это такое
import time


class State:
    def call_from_floor(self, floor: str):
        pass

    def go_to_floor(self, floor: str):
        pass


class Elevator(State):
    state: State
    current_floor: str
    floors: list[str] = ['P', '1', '2', '3']
    weight: str

    def change_state(self, state: State):
        pass

    def have_enough_weight(self):
        pass

    def call_from_floor(self, floor: str):
        pass

    def go_to_floor(self, floor: str):
        pass

    def is_doors_open(self):
        pass

    def open_doors(self):
        pass

    def close_doors(self):
        pass


class ElevatorState(State):
    elevator: Elevator

    def call_from_floor(self, floor):
        pass

    def go_to_floor(self, floor: str):
        pass


class Passenger:
    Weight: str
    request_to: str
    request_from: str


class IdleState(ElevatorState):
    def waiting(self):
        pass


class ReadyState(ElevatorState):
    pass


class MovingState(ElevatorState):
    pass
