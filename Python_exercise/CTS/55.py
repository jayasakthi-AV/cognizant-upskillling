class Category:
    def __init__(self, name, limit, spent):
        self.name = name
        self.limit = limit
        self.spent = spent

    def check_budget(self):
        if self.spent > self.limit:
            print(self.name, "budget exceeded")
        else:
            print(self.name, "within budget")

food = Category("Food", 5000, 4500)
travel = Category("Travel", 3000, 3500)

food.check_budget()
travel.check_budget()