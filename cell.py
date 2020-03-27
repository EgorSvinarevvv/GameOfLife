import pygame

class Cell:
	__slots__=("scr","surf","rect","is_alive")
	def __init__(self,scr,width,height,x,y,is_alive):
		self.scr=scr
		self.surf=pygame.Surface((width,height))
		self.rect=self.surf.get_rect()

		self.rect.x=x
		self.rect.y=y

		self.is_alive=is_alive

	def resize(self, size_coef):
		new_width = self.rect.width * size_coef
		new_height = self.rect.height * size_coef

		self.surf = pygame.Surface((new_width, new_height))
		

	def draw(self):
		if self.is_alive==True:
			self.surf.fill((0,0,0))
		else:

			self.surf.fill((255,255,255))
		self.scr.blit(self.surf,self.rect)

