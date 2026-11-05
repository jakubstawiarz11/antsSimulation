class Ant:
    def __init__(self, position:int, direction:int)->None:
        self.position = position
        self.direction = direction
        self.is_alive = True
        self.next_position = 0

    def move(self):
        if self.is_alive:
            self.position += self.direction

    def reverse_direction(self)->None:
        if self.is_alive:
            self.direction *= -1
