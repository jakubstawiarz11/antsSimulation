from ant import Ant
import random

class Simulation:
    def __init__(self, size: int = 100) -> None:
        self.size = size
        self.ants: list[Ant] = []
        self.turn =0

    def check_boundaries(self) -> None:
        for ant in self.ants:
            if ant.position > self.size or ant.position < 1:
                ant.is_alive = False
                #self.ants.remove(ant)

    #może potem optymalniej
    def check_collisions(self) -> set[Ant]:
        ants_colliding=set()
        for i in range(len(self.ants)):
            for j in range(i + 1, len(self.ants)):
                ant_a = self.ants[i]
                ant_b = self.ants[j]

                if ant_a.is_alive==True and ant_b.is_alive==True:
                    if ant_a.direction==-ant_b.direction:
                        if ant_a.next_position == ant_b.next_position:
                            ants_colliding.add(ant_a)
                            ants_colliding.add(ant_b)
                        if ant_a.next_position == ant_b.position and ant_b.next_position == ant_a.position:
                            ants_colliding.add(ant_a)
                            ants_colliding.add(ant_b)

        return ants_colliding

    def is_any_ant_alive(self) -> bool:
        for ant in self.ants:
            if ant.is_alive:
                return True
        return False

    def compute_next_position(self) -> None:
        for ant in self.ants:
           ant.next_position=ant.position + ant.direction

    def print_ants(self) -> None:
        print(self.turn)
        for ant in self.ants:
            print(ant.position, ant.direction)
        print("\n")

    # def print_ants(self) -> None:
    #     print(self.turn)
    #     map=[0]*self.size
    #     for ant in self.ants:
    #         if ant.is_alive:
    #             if ant.direction == 1:
    #                 map[ant.position] +=1
    #                 map[ant.position-1] -=1

    def move_ants(self):
        colliding_ants = self.check_collisions()
        for ant in self.ants:
            if not ant.is_alive:
                continue

            if ant in colliding_ants:
                ant.reverse_direction()
            else:
                ant.move()

    def spawn_ants(self, number_of_ants) -> None:
        for i in range(number_of_ants):
            self.ants.append(
                Ant(
                    position=random.randint(1, self.size),
                    direction=random.choice([-1, 1])
                )
            )

    def step(self) -> None:
        if not self.is_any_ant_alive():
            return

        self.compute_next_position()
        self.move_ants()
        self.check_boundaries()
        self.turn += 1


    # def run_simulation(self,number_of_ants) -> None:
    #     for i in range(number_of_ants):
    #         self.ants.append(Ant(position=random.randint(1, self.size), direction=random.choice([-1, 1])))
    #
    #     while self.is_any_ant_alive():
    #
    #         self.compute_next_position()
    #         self.move_ants()
    #         self.check_boundaries()
    #         self.turn += 1
    #
    #         self.print_ants()
