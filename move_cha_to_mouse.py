from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
running = True
arrow = 1
while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    character.clip_draw(frame * 100, 100 * arrow, 100, 100, x, y)
    frame = (frame + 1) % 8
    update_canvas()
    delay(0.1)
close_canvas()
