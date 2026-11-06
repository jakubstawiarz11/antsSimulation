# Example file showing a basic pygame "game loop"
import pygame
from ant import Ant
from simulation import Simulation

def draw_ant(screen, Ant,stick_cells):
    if not Ant.is_alive:
        return
    size = 10

    ant = pygame.Rect(0, 0, size, size)

    ant.center = stick_cells[Ant.position-1].center

    pygame.draw.rect(screen, pygame.Color("blue"), ant)

    if Ant.direction == 1:
        points = [
            (ant.left, ant.top),
            (ant.right, ant.centery),
            (ant.left, ant.bottom)
        ]
    else:
        points = [
            (ant.right, ant.top),
            (ant.left, ant.centery),
            (ant.right, ant.bottom)
        ]

    pygame.draw.polygon(screen, pygame.Color("white"), points)
def start_game(number_of_ants: int):

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1820, 720))
    clock = pygame.time.Clock()
    running = True

    stick_cells=[]
    for a in range(0,100):
        stick_cells.append(pygame.Rect(10+18*a, 100, 10, 5))

    simulation = Simulation(size=100)
    simulation.spawn_ants(number_of_ants)

    elapsed_time = 0
    simulation_interval = 100  # milisekundy

    font_turn = pygame.font.Font(None, 36)

    while running:
        elapsed_time += clock.tick(60)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if elapsed_time >= simulation_interval:
            simulation.step()
            elapsed_time -= simulation_interval

        screen.fill("black")

        # Rysowanie planszy
        for cell in stick_cells:
            pygame.draw.rect(screen, "red", cell)

        # Rysowanie mrówek
        for ant in simulation.ants:
            draw_ant(screen, ant, stick_cells)

        turn_text = font_turn.render(f"Turn: {simulation.turn}", True, "white")
        screen.blit(turn_text, (10, 10))
        screen.blit(turn_text, (10, 10))

        pygame.display.flip()

    pygame.quit()