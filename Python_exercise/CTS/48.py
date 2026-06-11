class CartItem:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item.price * item.quantity

        gst = total * 0.18
        final_total = total + gst

        print("Total:", total)
        print("GST:", gst)
        print("Final Total:", final_total)

cart = ShoppingCart()

cart.add_item(CartItem(100, 2))
cart.add_item(CartItem(200, 1))

cart.calculate_total()