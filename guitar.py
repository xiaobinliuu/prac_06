class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}): ${self.cost}"

    def get_age(self):
        year = 2021 - self.year
        return year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
