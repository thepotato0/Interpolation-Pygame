import pygame as pg
from pygame import Vector2
from interpolate import *
from easings import *
import sys

pg.init()

s = pg.display.set_mode((1200, 600))
clock = pg.time.Clock()
fps = 60

start_pos = Vector2(100, 100)
end_pos = Vector2(1100, 500)
circ_pos = start_pos.copy()
circ_interp = Interpolated(start_pos, end_pos, duration=2)
running = True

while running:
    dt = clock.tick(fps) / 1000.0
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    circ_pos = circ_interp.interpolate(dt,easing=easeInOutCirc)
    s.fill((255, 255, 255))

    pg.draw.circle(s, color=(255, 0, 0),center=circ_pos, radius=20)
    pg.display.update()

pg.quit()
sys.exit()