import copy


class Shop:
    def __init__(self, *items):
        self.stock = list(items)

    def list_items(self):
        output = 'In stock:\n'
        for item in self.stock:
            if item.get_amount() > 0:
                output += f'{item.get_name()}: {item.get_amount()}\n'
        return output

    def buy(self, item_name, amount=1):
        for item in self.stock:
            if item_name == item.get_name():
                item.decrease_amount(amount)
                break
        else:
            raise ValueError('No such item in stock')

        item_copy = copy.deepcopy(item)
        item_copy.set_amount(amount)
        return item_copy

    def sell(self, item, amount=1):
        item.decrease_amount(amount)
        for stock_item in self.stock:
            if stock_item.get_name() == item.get_name():
                stock_item.increase_amount(amount)
                break
        else:
            item_copy = copy.deepcopy(item)
            item_copy.set_amount(amount)
            self.stock.append(item_copy)


class Item:
    def __init__(self, name, amount=1, rarity='common'):
        self.__name = name
        self.__amount = amount
        self.__rarity = rarity

    # protected setters and getters
    def set_amount(self, value):
        if value < 0:
            raise ValueError('Value can not be negative')
        self.__amount = value

    def get_amount(self):
        return self.__amount

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_rarity(self, value):
        self.__rarity = value

    def get_rarity(self):
        return self.__rarity

    def decrease_amount(self, value=1):
        if self.__amount - value >= 0:
            self.__amount -= value
        else:
            raise ValueError('Item amount can not be negative')

    def increase_amount(self, value=1):
        if value < 0:
            raise ValueError('Value can not be negative')
        self.__amount += value
