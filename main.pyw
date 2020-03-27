import pygame
from sys import exit
from celltable import Celltable

class Main:
	__slots__=("scr","clock","scr_size","process_status","cells_in_row")
	def __init__(self,window_width,window_height,cells_in_row):
		self.scr=pygame.display.set_mode((window_width,window_height))
		self.clock=pygame.time.Clock()

		self.scr_size=self.scr.get_size()

		self.process_status=False
		self.cells_in_row=cells_in_row

	def draw_grid(self):
		x,y=0,0
		width,height=self.scr_size[0]/self.cells_in_row,self.scr_size[1]/self.cells_in_row
		x_width,y_height=self.scr_size[0],self.scr_size[1]
		for i in range(self.cells_in_row):
			pygame.draw.line(self.scr,(0,0,0),(x,y-1),(x_width,y-1))
			y+=height
		y=0
		for i in range(self.cells_in_row):
			pygame.draw.line(self.scr,(0,0,0),(x-1,y),(x-1,y_height))
			x+=width

	def mainloop(self):
		celltable=Celltable(self.scr,self.cells_in_row)
		while True:
			for i in pygame.event.get():
				if i.type==pygame.QUIT: exit()
				elif i.type==pygame.MOUSEBUTTONDOWN:
					self.process_status=False
					mouse_pos=pygame.mouse.get_pos()
					celltable.update_cell_status_by_click(mouse_pos[0],mouse_pos[1])

			if self.process_status==False:
				key=pygame.key.get_pressed()
				if key[pygame.K_RETURN]:
					self.process_status=True
				self.scr.fill((255,255,255))
				celltable.draw()
				self.draw_grid()
				pygame.display.update()
				self.clock.tick(30)
			else:
				self.scr.fill((255,255,255))
				celltable.draw()
				# celltable.print_celltable()
				celltable.update_cells_status()
				pygame.display.update()
				self.clock.tick(20)

main=Main(650,650,50)
main.mainloop()