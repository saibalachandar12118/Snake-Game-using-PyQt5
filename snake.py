#-------------------------------------------------------------
#-----------------------  Snake ------------------------------
#-------------------------------------------------------------

class Snake():
    def __init__(self):
        # Snake initial body
        self.Intial_snake = [[0,1],[1,1],[2,1]]
        self.reset_direction=[0,1]
        self.snake_array = self.Intial_snake[:]
        self._direction =self.reset_direction[:]
        self._Snake_color = "snake.png"
    @property
    def get_direction (self):
        return self._direction
    
    @property
    def get_snake_color(self):
        return self._Snake_color
    
    def set_direction(self,direction_input):
        self._direction = direction_input

    def set_snake_color(self,custom_color):
        self._Snake_color = custom_color




