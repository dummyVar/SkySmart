import shop as s

shop = s.Shop(s.Item('Shovel', 1), s.Item('Carrot seeds', 10))
print(shop.list_items())
bought_item = shop.buy('Carrot seeds', 7)
print(f"Bought items: {bought_item.get_name()}: {bought_item.get_amount()}")
shop.sell(s.Item('Hoe', 1), 1)
print(shop.list_items())