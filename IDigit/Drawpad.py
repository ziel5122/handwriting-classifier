import pygame
from PIL import Image

class DrawPad():
    def __init__(self, size, color):
        pygame.init()
        self.pad = pygame.display.set_mode(size)
        pygame.display.set_caption("Drawpad")
        self.pad.fill((255,255,255))
        
        pygame.display.flip()
        
    def draw(self, thickness):
        drawing = False
        last_pos = (0, 0)
        
        try:
            while True:
                event = pygame.event.wait()
                if (event.type == pygame.QUIT): 
                    img_string = pygame.image.tostring(self.pad, "RGBA")
                    self.image = Image.frombytes("RGBA", (300, 300), img_string)
                    raise StopIteration
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    pygame.draw.circle(self.pad, (0, 0, 0), event.pos, thickness)
                    drawing = True
                if (event.type == pygame.MOUSEBUTTONUP):
                    drawing = False
                if (event.type == pygame.MOUSEMOTION):
                    if (drawing):
                        pygame.draw.circle(self.pad, (0, 0, 0), event.pos, thickness)
                        line(self.pad, last_pos, event.pos, thickness)
                    last_pos = event.pos
                pygame.display.flip()
                
        except StopIteration:
            pass
            
        pygame.quit()

    def getImage(self):
        return self.image

def line(screen, start, end, thickness):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    longest = max(abs(dx), abs(dy))
    for i in range (0, longest):
        x = int(start[0] + float(i) / longest * dx)
        y = int(start[1] + float(i) / longest * dy)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), thickness)
