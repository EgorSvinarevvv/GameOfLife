import pygame


class Renderer:

    def __init__(self, scr):
        self.scr = scr

    def draw_grid(self, cells_in_row):
        surf_size = self.scr.get_size()
        x, y = 0, 0
        width = surf_size[0] / cells_in_row
        height = surf_size[1] / cells_in_row
        x_width, y_height = surf_size[0], surf_size[1]
        for i in range(cells_in_row):
            pygame.draw.line(self.scr, (0, 0, 0), (x, y - 1), (x_width, y - 1))
            y += int(height)
        y = 0
        for i in range(cells_in_row):
            pygame.draw.line(self.scr, (0, 0, 0),
                             (x - 1, y), (x - 1, y_height))
            x += int(width)

    def draw_celltable(self, celltable):
        for i in range(len(celltable)):
            for cell in celltable[i]:
                self.draw_cell(cell)

    def draw_cell(self, cell):
        if cell.is_alive == True:
            cell.surf.fill((0, 0, 0))
        else:
            cell.surf.fill((255, 255, 255))
        self.scr.blit(cell.surf, cell.rect)

    def update_environment(self, celltable, cells_in_row):
        self.scr.fill((0, 0, 0))

        self.draw_celltable(celltable)
        self.draw_grid(cells_in_row)
