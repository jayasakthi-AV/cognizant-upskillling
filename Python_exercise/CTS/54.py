class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

class Electronics(Product):
    pass

inventory = {
    "Laptop": 5,
    "Mouse": 2
}

low_stock = set()

for item, stock in inventory.items():
    if stock < 3:
        low_stock.add(item)

print("Low Stock Items:", low_stock)