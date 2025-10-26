
# -------------------------
# FOOD CLASS
# -------------------------
class Food:
    def __init__(self, location=[1,6]):
        self.location = location
        self._food = None
        self._score = 0
        self.name = None

    def food_getter(self):
        return self._food
    
    def food_setter(self,input_food):
        self._food = input_food
        return self._food

    @property
    def score_getter(self):
        return self._score

class Lizard(Food):
    def __init__(self, location=None):
        super().__init__(location)
        self.food_setter("lizard.png")
        self._score = 1
        self.name = "Lizard"

class Rat(Food):
    def __init__(self, location=None):
        super().__init__(location)
        self.food_setter("rat.png")
        self._score = 5
        self.name  ="Rat"


class Egg(Food):
    def __init__(self, location=None):
        super().__init__(location)
        self._food = "egg.png"
        self._score = 3
        self.name = "Egg"

food_items = [Lizard (), Rat(), Egg()]