import pygame
from sys import exit
from celltable import Celltable
from renderer import Renderer

class Main:
	__slots__=("scr", "clock", "scr_size", "process_status", "cells_in_row", "renderer")
	def __init__(self,window_width,window_height,cells_in_row):
		self.scr = pygame.display.set_mode((window_width,window_height))
		self.clock = pygame.time.Clock()
		self.renderer = Renderer(self.scr)

		self.scr_size = self.scr.get_size()

		self.process_status = False
		self.cells_in_row = cells_in_row

	def draw_grid(self):
		surf_size = self.scr.get_size()
		x, y = 0, 0
		width = surf_size[0] / self.cells_in_row
		height = surf_size[1] / self.cells_in_row
		x_width, y_height = surf_size[0], surf_size[1]
		print(width, height, x_width, y_height)
		for i in range(self.cells_in_row):
			pygame.draw.line(self.scr, (0, 0, 0), (x, y - 1), (x_width, y - 1))
			y += int(height)      	
		y = 0
		for i in range(self.cells_in_row):
			pygame.draw.line(self.scr, (0, 0, 0), (x - 1, y), (x - 1, y_height))
			x += int(width)

			

	def mainloop(self):
		celltable=Celltable(self.scr,self.cells_in_row)
		while True:
			for i in pygame.event.get():
				if i.type == pygame.QUIT: exit()
				elif i.type == pygame.MOUSEBUTTONDOWN:
					self.process_status = False
					mouse_pos = pygame.mouse.get_pos()
					celltable.update_cell_status_by_click(mouse_pos[0], mouse_pos[1])

			if self.process_status == False:
				key = pygame.key.get_pressed()
				if key[pygame.K_RETURN]:
					self.process_status = True
			else:
				celltable.update_cells_status()

			self.renderer.update_environment(celltable.celltable, self.cells_in_row)	
			pygame.display.update()
			self.clock.tick(30)
main=Main(650,650,50)
main.mainloop()