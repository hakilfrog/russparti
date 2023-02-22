class Item:  # look UML
    name: str  # name of item
    price: float = 0.0  # price of item

    def get_cost(self):  # get cost of item
        return self.price


class Coffee(Item):
    price = 6.0  # price of coffee

    def get_cost(self):
        super().get_cost()


class NoneItem(Item):

    def get_cost(self):
        return 0.0


class Component(Item):
    price = 0.0
    item: Item

    def __init__(self, item: Item):
        self.item = item

    def get_cost(self):
        return self.item.get_cost()


class MilkComponent(Component):
    price = 2.0

    def __init__(self, item: Item):
        super().__init__(item)

    def get_cost(self):
        return super().get_cost() + self.price


class SugarComponent(Component):
    price = 1.0

    def get_cost(self):
        pass


class SyrupComponent(Component):
    price = 2.0

    def get_cost(self):
        pass


testcoffee = MilkComponent()
print(testcoffee.get_cost())
