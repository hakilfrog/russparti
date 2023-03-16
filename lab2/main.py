class Item:  # look UML
    name: str  # name of item
    price: float = 0.0  # price of item

    def get_cost(self):  # get cost of item
        raise NotImplementedError()


class Coffee(Item):
    name = "Coffee"
    price = 6.0  # price of coffee

    def get_cost(self):
        return self.price


class NoneItem(Item):
    name = None

    def get_cost(self):
        return 0.0


class Component(Item):
    name: str
    price: float = 0.0
    item: Item

    def __init__(self, item: Item):
        self.item = item

    def get_cost(self):
        item_cost = self.item.get_cost()
        component_cost = self.get_component_cost()
        return item_cost + component_cost

    def get_component_cost(self):
        raise NotImplementedError()


class MilkComponent(Component):
    name = "Milk"
    price = 2.0

    def __init__(self, item: Item):
        super().__init__(item=item)

    def get_component_cost(self):
        return self.price

    def get_cost(self):
        return super().get_cost()


class SugarComponent(Component):
    name = "Sugar"
    price = 1.0

    def __init__(self, item: Item):
        super().__init__(item=item)

    def get_component_cost(self):
        return self.price

    def get_cost(self):
        return super().get_cost()


class SyrupComponent(Component):
    name = "Syrup"
    price = 2.0

    def __init__(self, item: Item):
        super().__init__(item=item)

    def get_component_cost(self):
        return self.price

    def get_cost(self):
        return super().get_cost()


testcoffee = Coffee()
testcoffee1 = MilkComponent(item=testcoffee)
testcoffee2 = SugarComponent(testcoffee1)
testnocoffee = NoneItem()
testnocoffee1 = SyrupComponent(testnocoffee)
# print(testcoffee.get_cost(), testcoffee.name)
print(testcoffee1.get_cost(), testcoffee.name, testcoffee1.name, )
print(testcoffee2.get_cost(), testcoffee.name, testcoffee1.name, testcoffee2.name)
print(testnocoffee1.get_cost(), testnocoffee1.name, testnocoffee1.item.name)
