from pico2d import *
import math
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while True:
    x=400
    y=90
    while x<800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x+=2
        delay(0.01)
    while y<600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y+=2
        delay(0.01)
    while x>0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x-=2
        delay(0.01)
    while y>90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y-=2
        delay(0.01)
    while x<400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
        delay(0.01)
    x=400
    t=270
    while t>-90:
        y=210*math.sin(t/360*2*math.pi)+300
        x=210*math.cos(t/360*2*math.pi)+400
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        t-=1
        delay(0.01)
        
close_canvas()
