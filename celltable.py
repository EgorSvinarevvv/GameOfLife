import pygame
from cell import Cell


class Celltable:
	__slots__=("scr","scr_size","cells_in_row","celltable")
	def __init__(self,scr,cells_in_row:int):
		self.scr=scr
		self.scr_size=self.scr.get_size()
		self.cells_in_row=cells_in_row

		self.celltable=[]

		self.fill_table()

	def fill_table(self):
		x,y=0,0
		width,height=self.scr_size[0]/self.cells_in_row,self.scr_size[1]/self.cells_in_row
		for i in range(self.cells_in_row):
			self.celltable.append([])
			for j in range(self.cells_in_row):
				self.celltable[-1].append(Cell(self.scr,width,height,x,y,False))
				x+=width
			x=0
			y+=height
		
	def update_cell_status_by_click(self,event_x,event_y):
		for i in range(len(self.celltable)):
			for cell in self.celltable[i]:
				if event_x>cell.rect.x and event_x<cell.rect.x+cell.rect.width:
					if event_y>cell.rect.y and event_y<cell.rect.y+cell.rect.height:
						if cell.is_alive==True:
							cell.is_alive=False
						else:
							cell.is_alive=True
	
	def print_celltable(self):
			result=[]
			for i in range(len(self.celltable)):
				for cell in self.celltable[i]:
					if cell.is_alive==True:
						result.append(1)
					else:
						result.append(0)
			print(result)

	def update_cells_status(self):
		tmp=[[] for i in range(len(self.celltable))]
		# print(tmp)
		for i in range(len(self.celltable)):
			for j in range(len(self.celltable[i])):
				alive_cells_around=0
				is_left_free,is_right_free,is_top_free,is_bot_free=False,False,False,False


				if i>0:
					if self.celltable[i-1][j].is_alive==True:
						alive_cells_around+=1
						is_top_free=True
					else:
						is_top_free=True
				else:
					is_top_free=False

				if i<len(self.celltable)-1:
					if self.celltable[i+1][j].is_alive==True:
						alive_cells_around+=1
						is_bot_free=True
					else:
						is_bot_free=True
				else:
					is_bot_free=False

				if j>0:
					if self.celltable[i][j-1].is_alive==True:
						alive_cells_around+=1
						is_left_free=True
					else:
						is_left_free=True
				else:
					is_left_free=False

				if j<len(self.celltable)-1:
					if self.celltable[i][j+1].is_alive==True:
						alive_cells_around+=1
						is_right_free=True
					else:
						is_right_free=True
				else:
					is_right_free=False

				if is_top_free:
					if is_left_free:
						if self.celltable[i-1][j-1].is_alive==True:
							alive_cells_around+=1
					if is_right_free:
						if self.celltable[i-1][j+1].is_alive==True:
							alive_cells_around+=1
				if is_bot_free:
					if is_left_free:
						if self.celltable[i+1][j-1].is_alive==True:
							alive_cells_around+=1
					if is_right_free:
						if self.celltable[i+1][j+1].is_alive==True:
							alive_cells_around+=1


				if self.celltable[i][j].is_alive==True:
					if alive_cells_around==2 or alive_cells_around==3:
						tmp[i].append(Cell(self.scr,self.celltable[i][j].rect.width,self.celltable[i][j].rect.height,self.celltable[i][j].rect.x,self.celltable[i][j].rect.y,True))
					elif alive_cells_around<2 or alive_cells_around>3:
						tmp[i].append(Cell(self.scr,self.celltable[i][j].rect.width,self.celltable[i][j].rect.height,self.celltable[i][j].rect.x,self.celltable[i][j].rect.y,False))
				else:
					if alive_cells_around==3:
						tmp[i].append(Cell(self.scr,self.celltable[i][j].rect.width,self.celltable[i][j].rect.height,self.celltable[i][j].rect.x,self.celltable[i][j].rect.y,True))
					else:
						tmp[i].append(Cell(self.scr,self.celltable[i][j].rect.width,self.celltable[i][j].rect.height,self.celltable[i][j].rect.x,self.celltable[i][j].rect.y,False))

				
		self.celltable=tmp

