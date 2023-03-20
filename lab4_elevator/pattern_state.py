import random
import time


class State:
    def process(self):
        raise NotImplementedError()


class VendingMachine:
    state: State

    def process_current_state(self):
        self.state.process()

    def change_state(self, new_state: State):
        self.state = new_state


def random_true_false():
    random_number = random.randrange(start=1, stop=11)
    ans = False
    if random_number >= 6:
        ans = True
    return ans


class Selection:
    product_number: int

    def __init__(self, product_number):
        self.product_number = product_number

    def is_avaliable_and_valid(self):
        # Проверка наличия продукта в автомате
        # (имитация)
        return random_true_false()

    def is_paid(self):
        # Проверка успешности оплаты
        # (имитация)
        return random_true_false()

    def timed_process_working_imitation(self):
        for i in (3, 2, 1):
            t = str(i) + ' '
            print(t, end='')
            time.sleep(0.25)
        print('done!')


class VendingMachineState(State):
    vending_machine: VendingMachine
    current_selection: Selection

    def __init__(self, vending_machine: VendingMachine):
        self.vending_machine = vending_machine


def timed_process_working_imitation():
    pass


class ProductDeliveredState(VendingMachineState):
    def process(self):
        print('[ProductDeliveredState]')
        # Определение следующего состояния
        next_state = IdleState(self.vending_machine)

        # Задание следующего состояния
        next_state.current_selection = self.current_selection
        self.vending_machine.change_state(next_state)

        timed_process_working_imitation()
        self.vending_machine.process_current_state()
        return


class PaymentUnsuccessfulState(VendingMachineState):
    def process(self):
        # Если оплата не прошла, то возврат к предыдущему состоянию
        print('[PaymentUnsuccessfulState]')
        next_state = ProductSelectedState(self.vending_machine)

        next_state.current_selection = self.current_selection
        self.vending_machine.change_state(next_state)

        timed_process_working_imitation()
        self.vending_machine.process_current_state()
        return


class PaymentSuccessfulState(VendingMachineState):
    def process(self):
        print('[PaymentSuccessfulState]')

        # Определение следующего состояния
        next_state = ProductDeliveredState(self.vending_machine)

        # Задание следующего состояния
        next_state.current_selection = self.current_selection
        self.vending_machine.change_state(next_state)

        timed_process_working_imitation()
        self.vending_machine.process_current_state()


class ProductSelectedState(VendingMachineState):
    # process Payment processing

    next_state: VendingMachineState = None

    def process(self):
        print('[ProductSelectedState]')
        input('Press Enter to do payment imitation')

        # Проверка оплаты и определение следующего состояния
        if not self.current_selection.is_paid():
            next_state = PaymentUnsuccessfulState(self.vending_machine)
        else:
            next_state = PaymentSuccessfulState(self.vending_machine)

        # Задание следующего состояния
        next_state.current_selection = self.current_selection
        self.vending_machine.change_state(next_state)

        timed_process_working_imitation()
        self.vending_machine.process_current_state()


class IdleState(VendingMachineState):
    # process Product selecting
    def process(self):
        print('[IdleState]')
        # Получение данных от пользователя
        product_number = input('Please select a drink (number):')

        # Проверка выбора
        self.current_selection = Selection(product_number)
        if not self.current_selection.is_avaliable_and_valid():
            self.process()
            return

        # Определение следующего состояния
        next_state = ProductSelectedState(self.vending_machine)

        # Задание следующего состояния
        next_state.current_selection = self.current_selection
        self.vending_machine.change_state(next_state)

        #timed_process_working_imitation()
        self.vending_machine.process_current_state()
        return

    class DrinksVendingMachine(VendingMachine):
        def __init__(self):
            self.state = IdleState(vending_machine=self)

    print('')
    dvm = DrinksVendingMachine()
    dvm.process_current_state()
